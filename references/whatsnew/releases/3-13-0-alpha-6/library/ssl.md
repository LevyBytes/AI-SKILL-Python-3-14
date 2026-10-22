# Python 3.13.0 alpha 6 / library / ssl

[gh-115627](https://github.com/python/cpython/issues/115627): Repair the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module's error handling when a peer drops the connection. It now raises an OSError carrying the right error code in place of an EOFError.

[gh-117310](https://github.com/python/cpython/issues/117310): Repaired a rare premature plus surplus `Py_DECREF` that could crash [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) while building a fresh `_ssl._SSLContext`, in the implausible event that CPython was compiled so the default cipher list comes up empty **or** the linked SSL library reports failure out of its C `SSL_CTX_set_cipher_list()` API.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
