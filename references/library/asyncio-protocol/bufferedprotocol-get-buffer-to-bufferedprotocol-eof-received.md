# Buffered Streaming Protocols

### Buffered Streaming Protocols

Added in version 3.7.

You can pair Buffered Protocols with any event loop method that handles Streaming Protocols.

With `BufferedProtocol` implementations, the receive buffer can be allocated and controlled by hand. The event loop is then free to reuse the protocol's buffer, sparing it needless data copies. For protocols that take in large volumes of data, this can yield a marked performance gain. Carefully built protocol implementations are able to cut buffer allocations down substantially.

On `BufferedProtocol` instances the callbacks below are invoked:

 BufferedProtocol.get_buffer(*sizehint*)

Called to allocate a new receive buffer.

*sizehint* is the suggested lower bound on the size of the buffer you return. Returning a buffer smaller or larger than *sizehint* indicates is fine. With a value of -1, any buffer size goes. Returning a buffer of zero size is an error.

`get_buffer()` must return an object implementing the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects).

 BufferedProtocol.buffer_updated(*nbytes*)

Called when the buffer was updated with the received data.

*nbytes* gives the count, in bytes, of everything written into the buffer.

 BufferedProtocol.eof_received()

See the documentation of the `protocol.eof_received()` method.

Across a single connection, `get_buffer()` may fire any number of times. Yet `protocol.eof_received()` fires no more than once, and should it fire, neither `get_buffer()` nor `buffer_updated()` will fire afterward.

State machine:

```none
start -> connection_made
    [-> get_buffer
        [-> buffer_updated]?
    ]*
    [-> eof_received]?
-> connection_lost -> end

```

[Subject index](INDEX.md) · [Previous](protocol-data-received-to-protocol-eof-received.md) · [Continue](datagram-protocol-receive-and-error-callbacks.md)
