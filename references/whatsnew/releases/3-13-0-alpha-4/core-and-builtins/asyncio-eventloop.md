# Python 3.13.0 alpha 4 / core and builtins / asyncio eventloop

[gh-114887](https://github.com/python/cpython/issues/114887): Loosen the socket-type check in [`create_datagram_endpoint()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint) so that every non-stream socket is accepted, which repairs a regression around raw-socket compatibility.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
