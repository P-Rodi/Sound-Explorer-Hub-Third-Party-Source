# Release source archive

The GitHub Release for each matching Sound Explorer Hub version contains one
archive named:

`Sound_Explorer_Hub_v<version>_Third_Party_Source.zip`

The archive contains:

- the exact FFmpeg source snapshot and build metadata used for the Windows
  runtime;
- official source archives for the LGPL Qt/PySide6 modules distributed with
  the application;
- source archives for the remaining Python runtime and packaging components;
- `SOURCE_COMPONENTS.json` with upstream links and SHA-256 checksums;
- `SHA256SUMS.txt` covering every file in the source archive.

The archive intentionally contains no Sound Explorer Hub application source
code. It exists to satisfy third-party license obligations and make the
redistributed libraries independently auditable and rebuildable.
