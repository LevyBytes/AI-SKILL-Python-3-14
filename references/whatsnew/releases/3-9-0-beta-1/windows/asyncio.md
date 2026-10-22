# Python 3.9.0 beta 1 / windows / asyncio

[bpo-39148](https://bugs.python.org/issue?@action=redirect&bpo=39148): IPv6 handling was added for [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) datagram endpoints under ProactorEventLoop. For address families that are unrecognized, the thrown exception becomes ValueError, since the Windows API is not its origin.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
