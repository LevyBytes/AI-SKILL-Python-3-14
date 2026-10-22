# What's New In Python 3.7 / Notable changes in Python 3.7.6 — asyncio-eventloop

### Notable changes in Python 3.7.6

On account of serious security worries, the *reuse_address* parameter of [`asyncio.loop.create_datagram_endpoint()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint) is no longer offered. The reason lies in how the `SO_REUSEADDR` socket option behaves under UDP. For fuller detail, consult the documentation covering `loop.create_datagram_endpoint()`. Kyle Stanley, Antoine Pitrou, and Yury Selivanov delivered this — see [bpo-37228](https://bugs.python.org/issue?@action=redirect&bpo=37228).

[Subject index](INDEX.md) · [Previous source section](notable-changes-in-python-3-7-2.md) · [Next source section](notable-changes-in-python-3-7-10.md) · [Release/subject declaration](summary-release-highlights.md)
