# Python 3.10.0 alpha 4 / library / exceptions

[bpo-42393](https://bugs.python.org/issue?@action=redirect&bpo=42393): Throw [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) rather than truncating silently within [`socket.ntohs()`](https://docs.python.org/3.14/library/socket.html#socket.ntohs) and [`socket.htons()`](https://docs.python.org/3.14/library/socket.html#socket.htons). That silent truncation had been deprecated back in Python 3.7. Erlend E. Aasland wrote the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
