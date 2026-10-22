# lzma / Compressing and decompressing data in memory: `lzma.LZMADecompressor`, `decompress()`

*class *lzma.LZMADecompressor(*format=FORMAT_AUTO*, *memlimit=None*, *filters=None*)

Build a decompressor object that lets you decompress data piece by piece.

When you would rather decompress a whole compressed stream in one go more conveniently, refer to `decompress()`.

Use the *format* argument to name the container format in play. Its default, `FORMAT_AUTO`, is able to decompress both `.xz` and `.lzma` files. The remaining choices are `FORMAT_XZ`, `FORMAT_ALONE`, and `FORMAT_RAW`.

The *memlimit* argument caps (in bytes) how much memory the decompressor may consume. Once you set it, decompression aborts with an `LZMAError` whenever the input cannot be decompressed inside that memory budget.

The *filters* argument names the filter chain originally applied when the stream now being decompressed was produced. You must pass it when *format* is `FORMAT_RAW`, yet leave it out for any other format. Turn to Specifying custom filter chains for fuller detail on filter chains.

Note

Unlike `decompress()` and `LZMAFile`, this class will not silently cope with inputs that bundle several compressed streams. Decompressing a multi-stream input via `LZMADecompressor` means spinning up a fresh decompressor per stream.

 decompress(*data*, *max_length=-1*)

Decompress *data* (a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)); uncompressed data comes back as bytes. A part of *data* might be held in an internal buffer, ready for later `decompress()` calls. You should join the returned data onto whatever earlier `decompress()` calls produced.

When *max_length* is nonnegative, no more than *max_length* bytes of decompressed data are returned. Should that ceiling be hit while more output remains available, the `needs_input` attribute flips to `False`. From there, the next `decompress()` call can pass *data* as `b''` to draw out the rest of the output.

Where every byte of input got decompressed and returned (whether because it amounted to fewer than *max_length* bytes, or because *max_length* was negative), the `needs_input` attribute flips to `True`.

Trying to decompress further once the stream's end has been reached raises an [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError). Whatever bytes turn up beyond the stream's end are discarded from processing and stashed in the `unused_data` attribute.

Changed in version 3.5: Added the *max_length* parameter.

 check

The identifier of the integrity check applied by the input stream. It can read `CHECK_UNKNOWN` right up until enough input has been decoded to settle which integrity check is in use.

 eof

`True` if the end-of-stream marker has been reached.

 unused_data

Whatever bytes turn up past the close of the compressed stream.

Until the stream's end has been reached, this holds `b""`.

 needs_input

`False` whenever the `decompress()` method still has more decompressed data to give out before it will need fresh uncompressed input.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](lzma-lzmacompressor-compress-to-lzma-lzmacompressor-flush.md) · [Continue](lzma-compress-to-lzma-decompress.md) · [Owning module, declaration or section: lzma](lzma-lzmaerror.md) · [Owning module, declaration or section: Compressing and decompressing data in memory](lzma-lzmacompressor-class.md)
