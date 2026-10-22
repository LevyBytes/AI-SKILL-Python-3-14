# Transports and Protocols

### Transports and Protocols

Preface

The **low-level** event loop APIs, for instance [`loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection), are the consumers of Transports and Protocols. Built around a callback-driven style, they make it possible to write fast implementations of network or IPC protocols such as HTTP.

In short, libraries and frameworks are the proper home for transports and protocols; high-level asyncio applications should leave them alone.

Both Transports and Protocols are described on this documentation page.

Introduction

Viewed broadly, the transport handles *how* bytes move across the wire, whereas the protocol decides *which* bytes get sent (and, in part, the timing).

To put it differently: a transport abstracts a socket (or a comparable I/O endpoint), and a protocol abstracts an application as seen from the transport's vantage point.

One more framing: taken together, the transport and protocol interfaces specify an abstract interface for doing network I/O and interprocess I/O.

Transport and protocol objects always pair up one-to-one: the protocol invokes transport methods to push data out, and the transport invokes protocol methods to hand over data it has received.

Connection oriented event loop methods (for instance [`loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection)) typically take a *protocol_factory* argument that builds a *Protocol* object for each accepted connection, which a *Transport* object represents. As a rule those methods hand back a tuple of `(transport, protocol)`.

Contents

The sections below appear on this documentation page:

- In the Transports section you'll find the asyncio `BaseTransport`, `ReadTransport`, `WriteTransport`, `Transport`, `DatagramTransport`, and `SubprocessTransport` classes.

- In the Protocols section you'll find the asyncio `BaseProtocol`, `Protocol`, `BufferedProtocol`, `DatagramProtocol`, and `SubprocessProtocol` classes.

- In the Examples section you'll see how transports, protocols, and the low-level event loop APIs are used together.

[Subject index](INDEX.md) · [Continue](transports.md)
