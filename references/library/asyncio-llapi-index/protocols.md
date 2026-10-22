# Protocols

### Protocols

These **callback methods** are available for protocol classes to implement:

| `callback` `connection_made()` | Called when a connection is made. |
| --- | --- |
| `callback` `connection_lost()` | Called when the connection is lost or closed. |
| `callback` `pause_writing()` | Called when the transport’s buffer goes over the high water mark. |
| `callback` `resume_writing()` | Called when the transport’s buffer drains below the low water mark. |

Streaming Protocols (TCP, Unix Sockets, Pipes)

| `callback` `data_received()` | Called when some data is received. |
| --- | --- |
| `callback` `eof_received()` | Called when an EOF is received. |

Buffered Streaming Protocols

| `callback` `get_buffer()` | Called to allocate a new receive buffer. |
| --- | --- |
| `callback` `buffer_updated()` | Called when the buffer was updated with the received data. |
| `callback` `eof_received()` | Called when an EOF is received. |

Datagram Protocols

| `callback` `datagram_received()` | Called when a datagram is received. |
| --- | --- |
| `callback` `error_received()` | Called when a previous send or receive operation raises an `OSError`. |

Subprocess Protocols

| `callback` `pipe_data_received()` | Fired once the child process pushes data out through its *stdout* or *stderr* pipe. |
| --- | --- |
| `callback` `pipe_connection_lost()` | Fired once any of the pipes that talk to the child process gets closed. |
| `callback` `process_exited()` | Fired once the child process exits. The `pipe_data_received()` and `pipe_connection_lost()` methods may fire after this one does. |

[Subject index](INDEX.md) · [Previous](transports.md) · [Continue](event-loop-policies.md)
