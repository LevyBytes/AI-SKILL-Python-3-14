# What’s New In Python 3.8 / Notable changes in Python 3.8.1 - asyncio-eventloop

### Notable changes in Python 3.8.1

Owing to serious security worries, support for the *reuse_address* parameter on [`asyncio.loop.create_datagram_endpoint()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint) has been dropped. The cause traces back to how the `SO_REUSEADDR` socket option behaves over UDP. The documentation for `loop.create_datagram_endpoint()` spells out the particulars. (The work here came from Kyle Stanley, Antoine Pitrou, and Yury Selivanov under [bpo-37228](https://bugs.python.org/issue?@action=redirect&bpo=37228).)

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-8-changes-in-the-c-api-demos-and-tools.md) · [Next source section](notable-changes-in-python-3-8-2.md) · [Release/subject declaration](assignment-expressions.md)
