# Python 3.11.0 alpha 1 / library / zlib

[bpo-44458](https://bugs.python.org/issue?@action=redirect&bpo=44458): `BUFFER_BLOCK_SIZE` is now marked static so that linking collisions are avoided when bz2, lmza or zlib get statically linked.

[bpo-43612](https://bugs.python.org/issue?@action=redirect&bpo=43612): [`zlib.compress()`](https://docs.python.org/3.14/library/zlib.html#zlib.compress) now takes a wbits parameter, letting callers compress data into a raw deflate block lacking zlib headers and trailers in a single step. Formerly that meant instantiating a `zlib.compressobj`. It additionally gives a quicker option than `gzip.compress` once wbits=31 is supplied.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
