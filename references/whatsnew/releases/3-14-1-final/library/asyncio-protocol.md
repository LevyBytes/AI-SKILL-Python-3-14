# Python 3.14.1 final / library / asyncio protocol

[gh-136234](https://github.com/python/cpython/issues/136234): Harden [`asyncio.WriteTransport.writelines()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.WriteTransport.writelines) against a failing connection, by adopting the identical behavior used in [`write()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.WriteTransport.write).

[gh-135444](https://github.com/python/cpython/issues/135444): Adjust [`asyncio.DatagramTransport.sendto()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.DatagramTransport.sendto) so that the datagram header size is counted whenever the data fails to go out.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
