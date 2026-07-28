# Reproducible minimal FFmpeg build

## Pinned source

- Project: FFmpeg
- Source commit:
  `2aefd64d4840a8555016a59dd7ac826974a307fc`
- Version family: 7.1.5
- Source:
  <https://github.com/FFmpeg/FFmpeg/commit/2aefd64d4840a8555016a59dd7ac826974a307fc>

## Configuration

The workflow cross-compiles Windows x64 shared libraries on Ubuntu using the
distribution's MinGW-w64 toolchain. It deliberately uses:

- `--enable-shared`
- `--disable-static`
- `--disable-autodetect`
- no `--enable-gpl`
- no `--enable-nonfree`
- no external codec libraries

FFmpeg's built-in audio decoders, filters, resampler, PCM encoder, and WAV
muxer remain enabled. This covers the Sound Explorer Hub operations:

- WAV, MP3, FLAC and OGG decoding;
- mono PCM decoding for waveform previews;
- `aresample`, `asetrate`, `atempo`, `areverse` and `aformat` filters;
- PCM signed 16-bit little-endian WAV output.

The workflow records the exact compiler, source commit, configure output,
binary hashes, and PE import list in the artifact.

## Rebuilding

1. Open **Actions** in this repository.
2. Select **Build minimal FFmpeg for Sound Explorer Hub**.
3. Choose **Run workflow**.
4. Download the `seh-ffmpeg-windows-x64-lgpl-shared` artifact.

The workflow is also triggered when its build definition or this document is
updated on the default branch.

The resulting runtime folder contains only `ffmpeg.exe`, its FFmpeg shared
DLLs, license texts, and build metadata.
