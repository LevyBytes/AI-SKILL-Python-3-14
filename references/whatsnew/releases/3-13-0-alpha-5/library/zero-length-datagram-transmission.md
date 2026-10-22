# Python 3.13.0 alpha 5 / library / handed empty bytes object datagramtransport sendto will transmit zero length datagrams

[gh-113812](https://github.com/python/cpython/issues/113812): When handed an empty bytes object, `DatagramTransport.sendto()` will now transmit zero-length datagrams. Buffer-size calculations for transport flow control now also include the datagram header.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
