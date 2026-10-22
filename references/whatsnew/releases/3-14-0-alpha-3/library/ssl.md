# Python 3.14.0 alpha 3 / library / ssl

[gh-127257](https://github.com/python/cpython/issues/127257): Within [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl), any system call failure that OpenSSL flags via `ERR_LIB_SYS` now surfaces as an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

[gh-127331](https://github.com/python/cpython/issues/127331): [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) is now able to display descriptions for the errors introduced in OpenSSL 3.4.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
