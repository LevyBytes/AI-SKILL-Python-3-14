# zlib: Flush modes and zlib version constants

zlib.Z_NO_FLUSH

Flush mode `0`. No special flushing behavior.

Added in version 3.6.

 zlib.Z_PARTIAL_FLUSH

Flush mode `1`. Pushes out as much output as it can.

 zlib.Z_SYNC_FLUSH

Flush mode `2`. Every bit of output is pushed out and lined up on a byte boundary.

 zlib.Z_FULL_FLUSH

Flush mode `3`. Every bit of output is pushed out and the compression state is cleared.

 zlib.Z_FINISH

Flush mode `4`. Every queued input is handled and nothing further is anticipated.

 zlib.Z_BLOCK

Flush mode `5`. A deflate block is rounded off and emitted.

You only get this constant when Python was built against zlib 1.2.2.2 or newer.

Added in version 3.6.

 zlib.Z_TREES

Flush mode `6`, used with inflate operations. Tells inflate to come back once it reaches the next deflate block boundary.

You only get this constant when Python was built against zlib 1.2.3.4 or newer.

Added in version 3.6.

The constants below expose details about the version of the zlib library currently in use:

 zlib.ZLIB_VERSION

The version string for the zlib library the module was built with. It can differ from the zlib library that actually runs at execution time, which you read from `ZLIB_RUNTIME_VERSION`.

 zlib.ZLIB_RUNTIME_VERSION

The version string for the zlib library the interpreter has genuinely loaded.

Added in version 3.3.

 zlib.ZLIBNG_VERSION

The version string for the zlib-ng library used to build the module, provided zlib-ng was the one in play. Where it exists, the `ZLIB_VERSION` and `ZLIB_RUNTIME_VERSION` constants mirror the zlib API version that zlib-ng furnishes.

Where zlib-ng did not build the module, this constant is missing entirely.

Added in version 3.14.

See also

Module [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip)

For reading and writing files in **gzip** format.

[https://www.zlib.net](https://www.zlib.net)

The home page of the zlib library.

[https://www.zlib.net/manual.html](https://www.zlib.net/manual.html)

The zlib manual lays out the meaning and use of the library's numerous functions.

Should gzip (de)compression become a performance bottleneck, the [python-isal](https://github.com/pycompression/python-isal) package accelerates (de)compression through a largely compatible API.

[Subject index](INDEX.md) · [Previous](decompress-decompress-to-zlib-z-fixed.md) · [Owning module, declaration or section: zlib](zlib-error-to-zlib-crc32.md)
