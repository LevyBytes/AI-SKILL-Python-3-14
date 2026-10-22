# gzip: `gzip.compress()`, `gzip.decompress()`

gzip.compress(*data*, *compresslevel=9*, ***, *mtime=0*)

Compress the *data* and give back a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object holding the compressed data. *compresslevel* and *mtime* carry the identical meaning they have in the `GzipFile` constructor above, except that *mtime* defaults to 0 so the output stays reproducible.

Added in version 3.2.

Changed in version 3.8: Added the *mtime* parameter for reproducible output.

Changed in version 3.11: Speed gets better because all the data is compressed in one pass rather than in a streamed manner. Calls where *mtime* is `0` are routed to [`zlib.compress()`](https://docs.python.org/3.14/library/zlib.html#zlib.compress) for added speed. Under those conditions the output may carry a gzip header “OS” byte holding some value besides 255 “unknown”, as provided by the underlying zlib implementation.

Changed in version 3.13: Whenever this function is used, the gzip header OS byte is now reliably fixed at 255 and thereby restores the behavior that held in 3.10 and before.

Changed in version 3.14: To keep output reproducible, the *mtime* parameter now falls back to 0. Should you want the old behavior of taking the current time, hand `None` to *mtime*.

 gzip.decompress(*data*)

Decompress the *data* and give back a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object holding the uncompressed data. This function can handle multi-member gzip data (several gzip blocks strung together). Where the data is guaranteed to hold just one member, the [`zlib.decompress()`](https://docs.python.org/3.14/library/zlib.html#zlib.decompress) function with *wbits* set to 31 runs faster.

Added in version 3.2.

Changed in version 3.11: Speed gets better because the members are decompressed together in memory rather than in a streamed manner.

[Subject index](INDEX.md) · [Previous](gzip-gzipfile-class-to-gzip-gzipfile-peek.md) · [Continue](examples-of-usage.md) · [Owning module, declaration or section: gzip](gzip-open-to-gzip-badgzipfile.md)
