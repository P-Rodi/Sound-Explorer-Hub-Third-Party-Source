# Sound Explorer Hub 1.4.42 - Third-Party Source

This archive contains corresponding and reference source material for the
third-party components distributed with the Sound Explorer Hub 1.4.42 Windows
x64 portable package.

It does not contain the proprietary Sound Explorer Hub application source.

## Layout

- `sources/` - upstream source archives;
- `build-information/ffmpeg/` - the exact FFmpeg build recipe, configuration
  log and metadata used for the runtime shipped with the application;
- `SOURCE_COMPONENTS.json` - component versions, distributed-binary licensing
  basis, complete-source licensing summaries, upstream locations and source
  archive checksums;
- `SHA256SUMS.txt` - SHA-256 checksums for all files in this archive.

The minimal FFmpeg build can be reproduced with the workflow and instructions
in `build-information/ffmpeg/`.

The archive contains two distinct FFmpeg source packages:

- FFmpeg 7.1.3 corresponds to the shared libraries supplied by the PySide6
  Qt Multimedia runtime;
- the exact `2aefd64d...` snapshot corresponds to Sound Explorer Hub's
  separate minimal command-line FFmpeg runtime.

These are complete upstream source archives. They therefore contain optional
source files under GPL or other per-file licenses even when those features were
not enabled in the binaries distributed with Sound Explorer Hub. The exact
minimal FFmpeg build configuration is preserved under
`build-information/ffmpeg/`.

Project source repository:
https://github.com/P-Rodi/Sound-Explorer-Hub-Third-Party-Source

Sound Explorer Hub application source code is not covered by the licenses of
these separate third-party components and is not included.
