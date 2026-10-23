# What's New In Python 3.6 / Notable changes in Python 3.6.10 - asyncio-eventloop

### Notable changes in Python 3.6.10

On account of serious security worries, support for the *reuse_address* parameter of [`asyncio.loop.create_datagram_endpoint()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint) has been dropped. The reason traces back to how the `SO_REUSEADDR` socket option acts over UDP. To learn more, refer to the documentation covering `loop.create_datagram_endpoint()`. (Contributed by Kyle Stanley, Antoine Pitrou, and Yury Selivanov in [bpo-37228](https://bugs.python.org/issue?@action=redirect&bpo=37228).)

[Subject index](INDEX.md) · [Previous source section](notable-changes-in-python-3-6-7.md) · [Next source section](notable-changes-in-python-3-6-13.md) · [Release/subject declaration](summary-release-highlights.md)
