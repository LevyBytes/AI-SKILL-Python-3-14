# bz2.BZ2Compressor: `compress()`, `flush()`

compress(*data*)

Feed data to the compressor object. Hands back a chunk of compressed data where it can, or else an empty byte string.

After you have finished feeding data to the compressor, invoke the `flush()` method to wrap up the compression process.

 flush()

Wrap up the compression process. Hands back whatever compressed data remains in internal buffers.

Once this method has run, the compressor object can no longer be used.

[Subject index](INDEX.md) · [Previous](bz2-bz2compressor-class.md) · [Continue](bz2-bz2decompressor-class-to-bz2-bz2decompressor-decompress.md) · [Owning module, declaration or section: bz2](bz2-support-for-bzip2-compression.md) · [Owning module, declaration or section: bz2.BZ2Compressor](bz2-bz2compressor-class.md) · [Owning module, declaration or section: Incremental (de)compression](bz2-bz2compressor-class.md)
