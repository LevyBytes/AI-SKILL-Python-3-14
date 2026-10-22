# asyncio.llapi.index: Event-loop DNS, connections and event-handler routes

DNS

| `await` `loop.getaddrinfo()` | Asynchronous version of `socket.getaddrinfo()`. |
| --- | --- |
| `await` `loop.getnameinfo()` | Asynchronous version of `socket.getnameinfo()`. |

Networking and IPC

| `await` `loop.create_connection()` | Open a TCP connection. |
| --- | --- |
| `await` `loop.create_server()` | Create a TCP server. |
| `await` `loop.create_unix_connection()` | Open a Unix socket connection. |
| `await` `loop.create_unix_server()` | Create a Unix socket server. |
| `await` `loop.connect_accepted_socket()` | Wrap a `socket` into a `(transport, protocol)` pair. |
| `await` `loop.create_datagram_endpoint()` | Open a datagram (UDP) connection. |
| `await` `loop.sendfile()` | Send a file over a transport. |
| `await` `loop.start_tls()` | Upgrade an existing connection to TLS. |
| `await` `loop.connect_read_pipe()` | Wrap a read end of a pipe into a `(transport, protocol)` pair. |
| `await` `loop.connect_write_pipe()` | Wrap a write end of a pipe into a `(transport, protocol)` pair. |

Sockets

| `await` `loop.sock_recv()` | Receive data from the `socket`. |
| --- | --- |
| `await` `loop.sock_recv_into()` | Receive data from the `socket` into a buffer. |
| `await` `loop.sock_recvfrom()` | Receive a datagram from the `socket`. |
| `await` `loop.sock_recvfrom_into()` | Receive a datagram from the `socket` into a buffer. |
| `await` `loop.sock_sendall()` | Send data to the `socket`. |
| `await` `loop.sock_sendto()` | Send a datagram via the `socket` to the given address. |
| `await` `loop.sock_connect()` | Connect the `socket`. |
| `await` `loop.sock_accept()` | Accept a `socket` connection. |
| `await` `loop.sock_sendfile()` | Send a file over the `socket`. |
| `loop.add_reader()` | Start watching a file descriptor for read availability. |
| `loop.remove_reader()` | Stop watching a file descriptor for read availability. |
| `loop.add_writer()` | Start watching a file descriptor for write availability. |
| `loop.remove_writer()` | Stop watching a file descriptor for write availability. |

Unix Signals

| `loop.add_signal_handler()` | Add a handler for a `signal`. |
| --- | --- |
| `loop.remove_signal_handler()` | Remove a handler for a `signal`. |

Subprocesses

| `loop.subprocess_exec()` | Spawn a subprocess. |
| --- | --- |
| `loop.subprocess_shell()` | Spawn a subprocess from a shell command. |

Error Handling

| `loop.call_exception_handler()` | Call the exception handler. |
| --- | --- |
| `loop.set_exception_handler()` | Set a new exception handler. |
| `loop.get_exception_handler()` | Get the current exception handler. |
| `loop.default_exception_handler()` | The default exception handler implementation. |

Examples

- [Using asyncio.new_event_loop() and loop.run_forever()](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio-example-lowlevel-helloworld).

- [Using loop.call_later()](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio-example-call-later).

- Using `loop.create_connection()` to implement [an echo-client](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-example-tcp-echo-client-protocol).

- Using `loop.create_connection()` to [connect a socket](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-example-create-connection).

- [Using add_reader() to watch an FD for read events](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio-example-watch-fd).

- [Using loop.add_signal_handler()](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio-example-unix-signals).

- [Using loop.subprocess_exec()](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-example-subprocess-proto).

[Subject index](INDEX.md) · [Previous](event-loop-methods-loop-stop-to-loop-get-task-factory.md) · [Continue](transports.md) · [Owning module, declaration or section: Event Loop Methods](event-loop-methods-loop-stop-to-loop-get-task-factory.md)
