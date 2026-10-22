# Datagram Transports

### Datagram Transports

 DatagramTransport.sendto(*data*, *addr=None*)

Deliver the *data* bytes to the remote peer designated by *addr* (a target address whose meaning depends on the transport). When *addr* is [`None`](https://docs.python.org/3.14/library/constants.html#None), the data goes to the target address supplied at transport creation.

Calling this method won't block; the data is buffered and queued for asynchronous transmission.

Changed in version 3.13: Passing an empty bytes object to this method now sends a zero-length datagram. The flow-control buffer-size computation has likewise been revised to include the datagram header.

 DatagramTransport.abort()

Shut the transport down at once, rather than letting pending operations finish. Any buffered data is discarded. Nothing more will be received. In time the protocol's `protocol.connection_lost()` method gets invoked with [`None`](https://docs.python.org/3.14/library/constants.html#None) passed as the argument.

[Subject index](INDEX.md) · [Previous](writetransport-abort-to-writetransport-write-eof.md) · [Continue](subprocesstransport-get-pid-to-subprocesstransport-close.md)
