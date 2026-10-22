# bz2: `bz2.BZ2Compressor`

### Incremental (de)compression

 *class *bz2.BZ2Compressor(*compresslevel=9*)

Build a fresh compressor object. You can put this object to use for compressing data incrementally. Where you want one-shot compression, reach for the `compress()` function instead.

*compresslevel*, where supplied, has to be an integer between `1` and `9`. The default is `9`.

[Subject index](INDEX.md) · [Previous](de-compression-of-files.md) · [Continue](bz2-bz2compressor-compress-to-bz2-bz2compressor-flush.md) · [Owning module, declaration or section: bz2](bz2-support-for-bzip2-compression.md)
