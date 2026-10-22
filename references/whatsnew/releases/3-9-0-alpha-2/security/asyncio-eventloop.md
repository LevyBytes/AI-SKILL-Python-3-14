# Python 3.9.0 alpha 2 / security / asyncio eventloop

[bpo-37228](https://bugs.python.org/issue?@action=redirect&bpo=37228): Owing to serious security concerns, the *reuse_address* parameter of [`asyncio.loop.create_datagram_endpoint()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint) is no longer honored. The cause is how `SO_REUSEADDR` behaves for UDP. See the documentation of `loop.create_datagram_endpoint()` for the full reasoning. Kyle Stanley, Antoine Pitrou, and Yury Selivanov made this change ([bpo-37228](https://bugs.python.org/issue?@action=redirect&bpo=37228)).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
