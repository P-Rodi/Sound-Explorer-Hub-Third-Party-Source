#!/usr/bin/env python3
"""Build a verified third-party source archive for a Sound Explorer Hub release."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import zipfile
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def copy_verified_sources(manifest_path: Path, downloads: Path, output: Path) -> None:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    sources = output / "sources"
    sources.mkdir(parents=True, exist_ok=True)
    for component in manifest["components"]:
        filename = component["source_file"]
        source = downloads / filename
        if not source.is_file():
            raise FileNotFoundError(f"Missing source archive: {source}")
        actual = sha256(source)
        expected = component["sha256"].lower()
        if actual != expected:
            raise RuntimeError(
                f"SHA-256 mismatch for {filename}: expected {expected}, got {actual}"
            )
        shutil.copy2(source, sources / filename)


def write_hash_manifest(root: Path) -> None:
    destination = root / "SHA256SUMS.txt"
    files = sorted(
        path for path in root.rglob("*") if path.is_file() and path != destination
    )
    lines = [
        f"{sha256(path)}  {path.relative_to(root).as_posix()}" for path in files
    ]
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def create_zip(source_root: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        destination.unlink()
    with zipfile.ZipFile(
        destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for path in sorted(source_root.rglob("*")):
            if path.is_file():
                archive.write(
                    path,
                    Path(source_root.name, path.relative_to(source_root)).as_posix(),
                )


def verify_zip(destination: Path, root_name: str) -> None:
    with zipfile.ZipFile(destination, "r") as archive:
        broken = archive.testzip()
        if broken is not None:
            raise RuntimeError(f"ZIP CRC verification failed for {broken}")
        checksum_name = f"{root_name}/SHA256SUMS.txt"
        lines = archive.read(checksum_name).decode("utf-8").splitlines()
        for line in lines:
            expected, relative = line.split("  ", 1)
            payload = archive.read(f"{root_name}/{relative}")
            actual = hashlib.sha256(payload).hexdigest()
            if actual != expected:
                raise RuntimeError(
                    f"ZIP SHA-256 mismatch for {relative}: "
                    f"expected {expected}, got {actual}"
                )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--downloads", type=Path, required=True)
    parser.add_argument("--ffmpeg-build-info", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--zip", type=Path, required=True)
    args = parser.parse_args()

    repository = Path(__file__).resolve().parents[1]
    output = args.output_dir.resolve()
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    copy_verified_sources(
        repository / "SOURCE_COMPONENTS.json", args.downloads.resolve(), output
    )
    shutil.copy2(repository / "SOURCE_COMPONENTS.json", output)
    shutil.copy2(repository / "SOURCE_ARCHIVE_README.md", output / "README.md")
    shutil.copy2(repository / "LICENSE", output / "REPOSITORY_LICENSE.txt")

    ffmpeg_destination = output / "build-information" / "ffmpeg"
    shutil.copytree(args.ffmpeg_build_info.resolve(), ffmpeg_destination)
    write_hash_manifest(output)
    create_zip(output, args.zip.resolve())
    verify_zip(args.zip.resolve(), output.name)

    print(f"Archive: {args.zip.resolve()}")
    print(f"SHA256:  {sha256(args.zip.resolve())}")
    print(f"Size:    {args.zip.resolve().stat().st_size} bytes")
    print("Verified: ZIP CRC and all internal SHA-256 checksums")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
