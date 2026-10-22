# lzma: `lzma.LZMACompressor`

### Compressing and decompressing data in memory

 *class *lzma.LZMACompressor(*format=FORMAT_XZ*, *check=-1*, *preset=None*, *filters=None*)

Build a compressor object that lets you compress data piece by piece.

When you simply need to compress one chunk of data more conveniently, refer to `compress()`.

Use the *format* argument to choose which container format applies. The available choices are:

- `FORMAT_XZ`: The `.xz` container format.

This is the default format.

- `FORMAT_ALONE`: The legacy `.lzma` container format.

Compared with `.xz`, this format is more restricted — it offers neither integrity checks nor multiple filters.

- `FORMAT_RAW`: A raw data stream, not using any container format.

With this specifier there are no integrity checks, and you are obliged to always hand over a custom filter chain (for both directions, compression and decompression). On top of that, data compressed this way is not recoverable through `FORMAT_AUTO` (refer to `LZMADecompressor`).

Use the *check* argument to pick which kind of integrity check goes into the compressed data. That check gets consulted at decompression time so corruption can be detected. The available choices are:

- `CHECK_NONE`: No integrity check at all. For both `FORMAT_ALONE` and `FORMAT_RAW` this is the default — and indeed the sole permitted value.

- `CHECK_CRC32`: 32-bit Cyclic Redundancy Check.

- `CHECK_CRC64`: 64-bit Cyclic Redundancy Check. For `FORMAT_XZ`, this serves as the default.

- `CHECK_SHA256`: 256-bit Secure Hash Algorithm.

When the requested check has no support, an `LZMAError` gets raised.

You can dictate the compression settings two ways: as a preset compression level (via the *preset* argument) or spelled out fully as a custom filter chain (via the *filters* argument).

Where you supply the *preset* argument, it ought to be an integer from `0` through `9` (inclusive), and you may OR it together with the constant `PRESET_EXTREME`. With neither *preset* nor *filters* passed, the fallback is `PRESET_DEFAULT` (which is preset level `6`). Larger presets yield tighter output at the cost of a slower compression run.

Note

Beyond the extra CPU load, higher presets also demand far more memory (and the output they create needs more memory to decompress). At preset `9`, say, an `LZMACompressor` object's overhead can climb to roughly 800 MiB. That is why staying with the default preset is normally the wiser choice.

Where the *filters* argument is given, it ought to be a filter chain specifier. Consult Specifying custom filter chains for the particulars.

[Subject index](INDEX.md) · [Previous](lzma-lzmafile-class-to-lzma-lzmafile-peek.md) · [Continue](lzma-lzmacompressor-compress-to-lzma-lzmacompressor-flush.md) · [Owning module, declaration or section: lzma](lzma-lzmaerror.md)
