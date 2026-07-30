# Sound Explorer Hub - Third-Party Source

This public repository provides corresponding source, reproducible build
information, notices, and checksums for LGPL/GPL components distributed with
the proprietary **Sound Explorer Hub** Windows application.

It does **not** contain the Sound Explorer Hub application source code.

## Release mapping

Each application release has a matching release here with the same version
tag. For example:

- application: `Sound_Explorer_Hub_v1.4.42.zip`
- corresponding source: release tag `v1.4.42`
- source archive:
  `Sound_Explorer_Hub_v1.4.42_Third_Party_Source.zip`

Open
[Releases](https://github.com/P-Rodi/Sound-Explorer-Hub-Third-Party-Source/releases)
and download the archive matching the application version.

The source archive maps every covered binary to its source archive, version,
distributed-binary licensing basis, complete-source licensing summary,
original URL, and SHA-256 checksum. Complete upstream source archives may
contain optional files under licenses that were not enabled in the distributed
binary; the manifest distinguishes those cases explicitly. Its structure is described in
[RELEASE_ARCHIVE.md](RELEASE_ARCHIVE.md), while
[SOURCE_COMPONENTS.json](SOURCE_COMPONENTS.json) records the exact upstream
versions, URLs and checksums for release 1.4.42.

## Minimal FFmpeg build

Sound Explorer Hub uses a dedicated minimal FFmpeg build for decoding audio,
generating waveforms, and exporting modified audio as PCM WAV. The build:

- is based on an exact FFmpeg commit;
- uses dynamic/shared FFmpeg DLLs;
- enables no optional GPL or non-free components in the distributed binary;
- uses no external codec libraries;
- is built by the public GitHub Actions workflow in this repository.

See [FFMPEG_BUILD.md](FFMPEG_BUILD.md) and
[`.github/workflows/build-minimal-ffmpeg.yml`](.github/workflows/build-minimal-ffmpeg.yml).

## Licenses

The scripts and original documentation in this repository are licensed under
the MIT License. Third-party source code and binaries retain their respective
upstream licenses. The applicable license texts and notices are included in
each corresponding-source release archive.

This repository is maintained to satisfy open-source distribution obligations
without publishing the proprietary Sound Explorer Hub application code.
