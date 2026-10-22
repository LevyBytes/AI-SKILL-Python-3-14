# Base Protocol

### Base Protocol

Every asyncio protocol may implement the Base Protocol callbacks.

Connection Callbacks

For each successful connection, the connection callbacks fire on every protocol precisely one time. Each of the remaining protocol callbacks may fire only in the span between those two methods.

 BaseProtocol.connection_made(*transport*)

Called when a connection is made.

The *transport* argument is the transport that stands for the connection. Keeping a reference to its transport is the protocol's job.

 BaseProtocol.connection_lost(*exc*)

Called when the connection is lost or closed.

What gets passed is either an exception object or [`None`](https://docs.python.org/3.14/library/constants.html#None). The second case signals a normal EOF arriving, or that this side of the connection aborted or closed it.

Flow Control Callbacks

Transports may invoke the flow control callbacks to pause or resume the writing that the protocol carries out.

See the documentation of the `set_write_buffer_limits()` method for more details.

 BaseProtocol.pause_writing()

Called when the transport's buffer goes over the high watermark.

 BaseProtocol.resume_writing()

Called when the transport's buffer drains below the low watermark.

When the buffer size matches the high watermark exactly, `pause_writing()` does not fire: the size has to climb strictly past it.

In the same way, `resume_writing()` fires once the buffer size sits at or beneath the low watermark. Those boundary conditions matter for keeping behavior correct whenever either mark happens to be zero.

[Subject index](INDEX.md) · [Previous](asyncio-subprocessprotocol-class.md) · [Continue](protocol-data-received-to-protocol-eof-received.md)
