# Python 3.12.0 beta 1 / library / urllib request

[gh-81403](https://github.com/python/cpython/issues/81403): When a cached FTP instance gets reused, [`urllib.request.CacheFTPHandler`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.CacheFTPHandler) no longer throws `URLError`. To support reusing an FTP instance correctly, ftplib's endtransfer method now invokes voidresp to drain the connection.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
