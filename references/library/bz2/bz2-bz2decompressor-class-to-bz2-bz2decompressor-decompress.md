# bz2 / Incremental (de)compression: `bz2.BZ2Decompressor`, `decompress()`

*class *bz2.BZ2Decompressor

Build a fresh decompressor object. You can put this object to use for decompressing data incrementally. Where you want one-shot compression, reach for the `decompress()` function instead.

Note

This class will not transparently cope with inputs holding several compressed streams, in contrast to `decompress()` and `BZ2File`. Where you need to decompress a multi-stream input using `BZ2Decompressor`, you have to employ a fresh decompressor for every stream.

 decompress(*data*, *max_length=-1*)

Decompress *data* (a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)), handing back uncompressed data as bytes. A portion of *data* may end up buffered internally, for use in subsequent calls to `decompress()`. The returned data ought to be joined onto the output of any earlier calls to `decompress()`.

Where *max_length* is nonnegative, hands back at most *max_length* bytes of decompressed data. Should that limit be hit while further output could still be produced, the `needs_input` attribute gets set to `False`. Under those circumstances, the next call to `decompress()` may pass *data* as `b''` to draw out more of the output.

Where the whole of the input data got decompressed and returned (either because it came to less than *max_length* bytes, or because *max_length* was negative), the `needs_input` attribute gets set to `True`.

Trying to decompress data once the end of stream is reached raises an [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError). Whatever data turns up past the end of the stream gets ignored and stored in the `unused_data` attribute.

Changed in version 3.5: Added the *max_length* parameter.

 eof

`True` if the end-of-stream marker has been reached.

Added in version 3.3.

 unused_data

Data found after the end of the compressed stream.

Should this attribute be read before the end of the stream has been reached, its value comes back as `b''`.

 needs_input

`False` whenever the `decompress()` method still has further decompressed data on hand without yet needing fresh uncompressed input.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](bz2-bz2compressor-compress-to-bz2-bz2compressor-flush.md) · [Continue](bz2-compress-to-bz2-decompress.md) · [Owning module, declaration or section: bz2](bz2-support-for-bzip2-compression.md) · [Owning module, declaration or section: Incremental (de)compression](bz2-bz2compressor-class.md)
