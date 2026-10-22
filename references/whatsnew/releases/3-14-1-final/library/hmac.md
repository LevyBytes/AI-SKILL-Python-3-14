# Python 3.14.1 final / library / hmac

[gh-140120](https://github.com/python/cpython/issues/140120): A memory leak in [`hmac`](https://docs.python.org/3.14/library/hmac.html#module-hmac), present while it relied on the hacl-star backend, was repaired. `@ashm-dev` found it with AddressSanitizer.

[gh-136912](https://github.com/python/cpython/issues/136912): [`hmac.digest()`](https://docs.python.org/3.14/library/hmac.html#hmac.digest) now copes correctly with sizable keys plus messages, dropping back to the pure Python implementation whenever that is needed. Bénédikt Tran supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
