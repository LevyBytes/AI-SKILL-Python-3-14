# zlib: Streaming decompression methods and compression settings

Decompress.decompress(*data*, *max_length=0*)

Expands *data* and yields a bytes object holding the recovered data that matches at least some of what *string* contained. Append this to whatever earlier `decompress()` calls already produced. Part of the input data may linger in internal buffers awaiting later handling.

When the optional parameter *max_length* is non-zero, the returned value will run no further than *max_length*. As a result some of the compressed input may go unhandled, and the leftover data lands in the attribute `unconsumed_tail`. Hand that bytestring to a later `decompress()` call to carry on with decompression. When *max_length* equals zero the whole input is expanded and `unconsumed_tail` ends up empty.

Changed in version 3.6: *max_length* can be used as a keyword argument.

 Decompress.flush([*length*])

Every bit of queued input gets handled and a bytes object holding the leftover uncompressed output comes back. Once you call `flush()`, calling `decompress()` again is impossible; deleting the object is then the only sensible move.

The optional parameter *length* fixes the output buffer's starting size.

 Decompress.copy()

Hands back a duplicate of the decompression object. It lets you capture the decompressor's state partway through the data stream, which later speeds up random seeks into that stream.

Changed in version 3.8: Added [`copy.copy()`](https://docs.python.org/3.14/library/copy.html#copy.copy) and [`copy.deepcopy()`](https://docs.python.org/3.14/library/copy.html#copy.deepcopy) support to decompression objects.

The constants listed below let you configure how compression and decompression behave:

 zlib.DEFLATED

The deflate algorithm used for compression.

 zlib.MAX_WBITS

The largest permitted window size, given as a power of 2. As an example, a `MAX_WBITS` of `15` yields a window size of `32 KiB`.

 zlib.DEF_MEM_LEVEL

The memory level applied by default to compression objects.

 zlib.DEF_BUF_SIZE

The buffer size applied by default during decompression.

 zlib.Z_NO_COMPRESSION

Compression level `0`; no compression.

Added in version 3.6.

 zlib.Z_BEST_SPEED

Compression level `1`; the quickest, giving the least compression.

 zlib.Z_BEST_COMPRESSION

Compression level `9`; the slowest, giving the most compression.

 zlib.Z_DEFAULT_COMPRESSION

The default compression level (`-1`); a balance struck between speed and compression. At present it matches compression level `6`.

 zlib.Z_DEFAULT_STRATEGY

The strategy used by default, suited to ordinary data.

 zlib.Z_FILTERED

A strategy meant for data coming out of a filter (or predictor).

 zlib.Z_HUFFMAN_ONLY

A strategy that restricts the encoder to Huffman coding alone.

 zlib.Z_RLE

A strategy that caps match distances at one (run-length encoding).

You only get this constant when Python was built against zlib 1.2.0.1 or newer.

Added in version 3.6.

 zlib.Z_FIXED

A strategy that bars the encoder from using dynamic Huffman codes.

You only get this constant when Python was built against zlib 1.2.2.2 or newer.

Added in version 3.6.

[Subject index](INDEX.md) · [Previous](zlib-decompress-to-decompress-eof.md) · [Continue](zlib-z-no-flush-to-zlib-zlibng-version.md) · [Owning module, declaration or section: zlib](zlib-error-to-zlib-crc32.md)
