# lzma: `lzma.compress()`, `lzma.decompress()`

lzma.compress(*data*, *format=FORMAT_XZ*, *check=-1*, *preset=None*, *filters=None*)

Compress *data* (a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object); the compressed result comes back as a `bytes` object.

Refer to `LZMACompressor` above for what the *format*, *check*, *preset* and *filters* arguments mean.

 lzma.decompress(*data*, *format=FORMAT_AUTO*, *memlimit=None*, *filters=None*)

Decompress *data* (a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object); the uncompressed result comes back as a `bytes` object.

Where *data* joins together several separate compressed streams, every one of those streams is decompressed and the joined-up results are returned.

Refer to `LZMADecompressor` above for what the *format*, *memlimit* and *filters* arguments mean.

[Subject index](INDEX.md) · [Previous](lzma-decompressor-contract.md) · [Continue](lzma-is-check-supported.md) · [Owning module, declaration or section: lzma](lzma-lzmaerror.md) · [Owning module, declaration or section: Compressing and decompressing data in memory](lzma-lzmacompressor-class.md)
