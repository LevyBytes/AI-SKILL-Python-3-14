# Python 3.14.4 final / library / ssl

[gh-146080](https://github.com/python/cpython/issues/146080): [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl): corrects a crash whenever an SNI callback attempts to use an SSL object that was already garbage-collected. Bénédikt Tran supplied the patch.

[gh-144833](https://github.com/python/cpython/issues/144833): Corrected a use-after-free within [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) whenever `SSL_new()` hands back NULL inside `newPySSLSocket()`. The error had been reported via a dangling pointer once the object was already freed.

[gh-142516](https://github.com/python/cpython/issues/142516): [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl): reference leaks affecting [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) objects are now corrected. Bénédikt Tran supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
