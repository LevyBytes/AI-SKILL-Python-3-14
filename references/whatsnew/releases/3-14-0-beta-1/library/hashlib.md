# Python 3.14.0 beta 1 / library / hashlib

[gh-122179](https://github.com/python/cpython/issues/122179): During non-blocking I/O with no data ready, [`hashlib.file_digest()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.file_digest) now raises [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError). Previously the digest gained spurious null bytes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
