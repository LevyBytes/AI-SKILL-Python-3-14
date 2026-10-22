# Python 3.12.0 alpha 4 / windows / asyncio protocol

[gh-99941](https://github.com/python/cpython/issues/99941): Guarantee that [`asyncio.Protocol.data_received()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.Protocol.data_received) gets handed an immutable [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object as documented, rather than a [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
