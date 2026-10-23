# asyncio - Streams

### Streams

High-level APIs for dealing with network IO.

| `await` `open_connection()` | Establish a TCP connection. |
| --- | --- |
| `await` `open_unix_connection()` | Establish a Unix socket connection. |
| `await` `start_server()` | Start a TCP server. |
| `await` `start_unix_server()` | Start a Unix socket server. |
| `StreamReader` | A high-level async/await object for taking in network data. |
| `StreamWriter` | A high-level async/await object for pushing out network data. |

Examples

- [Example TCP client](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio-example-stream).

- See also the [streams APIs](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio-streams) documentation.

[Subject index](INDEX.md) · [Previous](subprocesses.md) · [Continue](synchronization.md)
