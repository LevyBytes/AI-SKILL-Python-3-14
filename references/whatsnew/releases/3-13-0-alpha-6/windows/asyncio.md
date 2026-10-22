# Python 3.13.0 alpha 6 / windows / asyncio

[gh-91227](https://github.com/python/cpython/issues/91227): Correct the asyncio ProactorEventLoop so that firing a datagram at an address nobody is listening on no longer blocks the loop from getting further datagrams.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
