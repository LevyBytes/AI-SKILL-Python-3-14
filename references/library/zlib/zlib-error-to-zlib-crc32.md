# zlib: Checksums and compression constructors

## zlib - Compression compatible with gzip

### `zlib` - Compression compatible with **gzip**

---

When your program needs to compress data, the routines this module exposes handle both compression and decompression by drawing on the [zlib library](https://www.zlib.net).

It counts as an [optional module](https://docs.python.org/3.14/glossary.html#term-optional-module). Should your build of CPython lack it, check with whoever supplied Python to you for documentation. And if you are that supplier yourself, refer to [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements).

The routines in zlib come with plenty of options and frequently must be called in a set sequence. This page makes no effort to catalog every combination; turn to the [zlib manual](https://www.zlib.net/manual.html) for definitive details.

To read or write `.gz` files, turn instead to the [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip) module.

This module exposes the exception and functions listed below:

 *exception *zlib.error

The error thrown when compression or decompression goes wrong.

 zlib.adler32(*data*[, *value*])

Works out an Adler-32 checksum over *data*. (An Adler-32 checksum offers reliability close to a CRC32 yet runs considerably faster.) What you get back is an unsigned 32-bit integer. When *value* is supplied it serves as the checksum's starting point; without it, the default starting value of 1 applies. Supplying *value* lets you build a running checksum across several inputs joined end to end. This algorithm carries no cryptographic strength, so keep it away from authentication or digital signatures. Built specifically to serve as a checksum, it also makes a poor general-purpose hash.

Changed in version 3.0: The result is always unsigned.

 zlib.compress(*data*, */*, *level=Z_DEFAULT_COMPRESSION*, *wbits=MAX_WBITS*)

Squeezes the bytes held in *data* and returns a bytes object holding the compressed result. The *level* is an integer between `0` and `9`, or `-1`, that sets how aggressively to compress; consult `Z_BEST_SPEED` (`1`), `Z_BEST_COMPRESSION` (`9`), `Z_NO_COMPRESSION` (`0`), and the default `Z_DEFAULT_COMPRESSION` (`-1`) to learn what these settings mean.

The *wbits* argument governs how large the history buffer (the “window size”) grows while data is compressed, plus whether a header and trailer get attached to the output. Several value ranges are accepted, with the default being `15` (`MAX_WBITS`):

- +9 to +15: Gives the window size as a base-two logarithm, so the window spans from 512 up to 32768. Higher numbers compress more tightly while consuming additional memory. The emitted output carries a zlib-style header and trailer.

- −9 to −15: Treats the magnitude of *wbits* as the window-size logarithm and emits a bare output stream lacking any header or closing checksum.

- +25 to +31 = 16 + (9 to 15): Reads the value's lowest 4 bits as the window-size logarithm and adds a simple **gzip** header plus a closing checksum to the output.

Throws the `error` exception should anything go wrong.

Changed in version 3.6: *level* is now accepted as a keyword parameter as well.

Changed in version 3.11: The *wbits* parameter can now be supplied to choose window bits along with the compression type.

 zlib.compressobj(*level=Z_DEFAULT_COMPRESSION*, *method=DEFLATED*, *wbits=MAX_WBITS*, *memLevel=DEF_MEM_LEVEL*, *strategy=Z_DEFAULT_STRATEGY*[, *zdict*])

Hands back a compression object suited to compressing data streams too large to hold in memory all at once.

The *level* sets the compression level – an integer running from `0` to `9` or `-1`. Refer to `Z_BEST_SPEED` (`1`), `Z_BEST_COMPRESSION` (`9`), `Z_NO_COMPRESSION` (`0`), and the default `Z_DEFAULT_COMPRESSION` (`-1`) for the meaning of these settings.

The *method* names the compression algorithm. At present `DEFLATED` is the sole accepted value.

The *wbits* parameter dictates the history buffer's size (the “window size”) along with which header and trailer format applies. Its meaning matches what was described for compress().

The *memLevel* argument fixes how much memory the internal compression state consumes. Permitted values run from `1` to `9`. Bigger numbers spend more memory yet run quicker and yield smaller output.

The *strategy* tunes the compression algorithm. Acceptable choices are `Z_DEFAULT_STRATEGY`, `Z_FILTERED`, `Z_HUFFMAN_ONLY`, `Z_RLE` and `Z_FIXED`.

The *zdict* supplies a ready-made compression dictionary. It is a run of bytes (for instance a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object) holding subsequences likely to show up often in the data being compressed. Place the subsequences you expect most frequently toward the dictionary's tail.

Changed in version 3.3: Introduced the *zdict* parameter together with keyword-argument support.

 zlib.crc32(*data*[, *value*])

Works out a CRC (Cyclic Redundancy Check) checksum over *data*. What you get back is an unsigned 32-bit integer. When *value* is supplied it acts as the checksum's starting point; otherwise the starting value defaults to 0. Supplying *value* lets you maintain a running checksum spanning several inputs joined end to end. This algorithm carries no cryptographic strength, so steer clear of it for authentication or digital signatures. Designed purely as a checksum, it also serves poorly as a general hash.

Changed in version 3.0: The result is always unsigned.

[Subject index](INDEX.md) · [Continue](zlib-decompress-to-decompress-eof.md)
