# lzma.LZMACompressor: `compress()`, `flush()`

compress(*data*)

Compress *data* (a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object); the return is a `bytes` object holding compressed output covering at least a portion of the input. A part of *data* might be held in an internal buffer, ready for later `compress()` and `flush()` calls. You should join the returned data onto whatever earlier `compress()` calls produced.

 flush()

Wrap up the compression run, handing back a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object that holds whatever still sits in the compressor’s internal buffers.

Once this method runs, the compressor can no longer be used.

[Subject index](INDEX.md) · [Previous](lzma-lzmacompressor-class.md) · [Continue](lzma-decompressor-contract.md) · [Owning module, declaration or section: lzma](lzma-lzmaerror.md) · [Owning module, declaration or section: lzma.LZMACompressor](lzma-lzmacompressor-class.md) · [Owning module, declaration or section: Compressing and decompressing data in memory](lzma-lzmacompressor-class.md)
