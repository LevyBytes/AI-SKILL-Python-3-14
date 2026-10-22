# Datagram Protocols

### Datagram Protocols

The protocol factories handed to the [`loop.create_datagram_endpoint()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint) method are what should build Datagram Protocol instances.

 DatagramProtocol.datagram_received(*data*, *addr*)

Invoked upon receipt of a datagram. The *data* parameter is a bytes object holding the arriving payload, while *addr* identifies the peer that sent it; how that address is formatted varies with the transport.

 DatagramProtocol.error_received(*exc*)

Invoked once an earlier send or receive call throws an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError). The *exc* argument holds that `OSError` instance.

Only in unusual situations does this method fire, when the transport (e.g. UDP) notices that some datagram couldn't reach its destination. Often, though, datagrams that can't be delivered are quietly discarded.

Note

Flow control isn't available for datagram protocols on BSD systems (macOS, FreeBSD, etc.), since there's no dependable means of spotting send failures brought on by emitting too many packets.

The socket forever reports itself 'ready', and any surplus packets get discarded. There may or may not be an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) raised with `errno` set to [`errno.ENOBUFS`](https://docs.python.org/3.14/library/errno.html#errno.ENOBUFS); when one is raised, it reaches `DatagramProtocol.error_received()` but is otherwise disregarded.

[Subject index](INDEX.md) · [Previous](bufferedprotocol-get-buffer-to-bufferedprotocol-eof-received.md) · [Continue](subprocess-protocol-pipe-callbacks.md)
