# zlib: Decompression setup and streaming state

zlib.decompress(*data*, */*, *wbits=MAX_WBITS*, *bufsize=DEF_BUF_SIZE*)

Expands the bytes held in *data* and returns a bytes object holding the recovered data. The *wbits* parameter hinges on the format of *data* and is covered further down. When *bufsize* is supplied it sets the output buffer's starting size. Throws the `error` exception should anything go wrong.

The *wbits* parameter sets the history buffer's size (the “window size”) plus the header and trailer format that is expected. It resembles the parameter used by `compressobj()` but takes a wider span of values:

- +8 to +15: Expresses the window size as a base-two logarithm. The input has to carry a zlib header and trailer.

- 0: Works out the window size on its own from the zlib header. This has only been available since zlib 1.2.3.5.

- −8 to −15: Treats the magnitude of *wbits* as the window-size logarithm. The input has to be a bare stream lacking any header or trailer.

- +24 to +31 = 16 + (8 to 15): Reads the value's lowest 4 bits as the window-size logarithm. The input has to carry a gzip header and trailer.

- +40 to +47 = 32 + (8 to 15): Reads the value's lowest 4 bits as the window-size logarithm and accepts either the zlib or the gzip format on its own.

While a stream is being decompressed, the window size has to be at least as large as the one used when the stream was first compressed; choosing too small a value can trigger an `error` exception. The default *wbits* setting maps to the largest window size and demands that a zlib header and trailer be present.

The *bufsize* gives the starting size of the buffer that holds decompressed data. The buffer grows on demand whenever more room is needed, so this number need not be exact; tweaking it merely trims a handful of `malloc()` calls.

Changed in version 3.6: both *wbits* and *bufsize* are now accepted as keyword arguments.

 zlib.decompressobj(*wbits=MAX_WBITS*[, *zdict*])

Hands back a decompression object meant for expanding data streams too big to keep in memory all at once.

The *wbits* parameter sets the history buffer's size (the “window size”) plus the header and trailer format that is expected. Its meaning matches what was described for decompress().

The *zdict* parameter names a ready-made compression dictionary. When given, it has to be the very dictionary the compressor relied on while producing the data now being decompressed.

Note

When *zdict* is a mutable object (a [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray), say), leave its contents untouched between the `decompressobj()` call and the decompressor's first `decompress()` call.

Changed in version 3.3: Added the *zdict* parameter.

These methods are available on compression objects:

 Compress.compress(*data*)

Compresses *data* and yields a bytes object holding compressed output covering at least some of what *data* contained. Append this to whatever earlier `compress()` calls already produced. A portion of the input may stay parked in internal buffers awaiting later handling.

 Compress.flush([*mode*])

Every bit of queued input gets handled and a bytes object holding the leftover compressed output comes back. You may pick *mode* from the constants `Z_NO_FLUSH`, `Z_PARTIAL_FLUSH`, `Z_SYNC_FLUSH`, `Z_FULL_FLUSH`, `Z_BLOCK`, or `Z_FINISH`, with `Z_FINISH` as the default. Every constant apart from `Z_FINISH` keeps the door open for compressing more bytestrings, whereas `Z_FINISH` seals the compressed stream so no further data may be compressed. Once you call `flush()` with *mode* set to `Z_FINISH`, calling `compress()` again is impossible; deleting the object is then the only sensible move.

 Compress.copy()

Hands back a duplicate of the compression object. It comes in handy for compressing several data sets that begin with the same shared prefix.

Changed in version 3.8: Added [`copy.copy()`](https://docs.python.org/3.14/library/copy.html#copy.copy) and [`copy.deepcopy()`](https://docs.python.org/3.14/library/copy.html#copy.deepcopy) support to compression objects.

These methods and attributes are available on decompression objects:

 Decompress.unused_data

A bytes object carrying whatever bytes lie beyond the end of the compressed data. Put differently, it stays `b""` right up until the final byte holding compression data becomes available. When the entire bytestring proved to be compressed data, it equals `b""`, an empty bytes object.

 Decompress.unconsumed_tail

A bytes object carrying whatever data the most recent `decompress()` call left unprocessed because it ran past the uncompressed-data buffer's limit. The zlib machinery has not yet looked at this data, so you must hand it (perhaps with more data appended) to a later `decompress()` call to obtain proper output.

 Decompress.eof

A boolean reporting whether the end of the compressed data stream has been hit.

It lets you tell a well-formed compressed stream apart from one that is truncated or incomplete.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](zlib-error-to-zlib-crc32.md) · [Continue](decompress-decompress-to-zlib-z-fixed.md) · [Owning module, declaration or section: zlib](zlib-error-to-zlib-crc32.md)
