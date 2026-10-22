# Python 3.11.0 alpha 1 / library / asyncio eventloop

[bpo-45129](https://bugs.python.org/issue?@action=redirect&bpo=45129): Owing to serious security worries, the *reuse_address* argument of [`asyncio.loop.create_datagram_endpoint()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint), already turned off back in Python 3.9, has now been deleted outright. The trigger is how the `SO_REUSEADDR` socket option acts under UDP.

Hugo van Kemenade supplied this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
