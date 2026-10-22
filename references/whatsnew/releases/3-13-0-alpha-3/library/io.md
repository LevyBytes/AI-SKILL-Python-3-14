# Python 3.13.0 alpha 3 / library / io

[gh-111049](https://github.com/python/cpython/issues/111049): Fix a crash arising during garbage collection of the [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) buffer object.

[bpo-35928](https://bugs.python.org/issue?@action=redirect&bpo=35928): Following `read()` and `write()`, [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) now manages the decoding buffer correctly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
