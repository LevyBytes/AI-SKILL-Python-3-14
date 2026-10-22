# Python 3.14.0 alpha 4 / library / ssl

[gh-127360](https://github.com/python/cpython/issues/127360): Where no descriptive message is available for an [`ssl.SSLError`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLError), the "unknown error" text now surfaces the internal error code (as fetched by `ERR_get_error` and related OpenSSL functions).

[gh-128035](https://github.com/python/cpython/issues/128035): Use [`ssl.HAS_PHA`](https://docs.python.org/3.14/library/ssl.html#ssl.HAS_PHA) to report whether the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module is able to do TLSv1.3 post-handshake client authentication (PHA). Will Childs-Klein supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
