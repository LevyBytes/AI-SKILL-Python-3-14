# StreamWriter: `start_tls()`, `is_closing()`, `wait_closed()`

`*async *start_tls(*sslcontext*, ***, *server_hostname=None*, *ssl_handshake_timeout=None*, *ssl_shutdown_timeout=None*)`

Promote an already-open stream-based connection to TLS.

Parameters:

- *sslcontext*: a set-up instance of [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext).

- *server_hostname*: assigns or overrides the host name to be checked against the target server's certificate.

- *ssl_handshake_timeout* gives, in seconds, how long to await completion of the TLS handshake before the connection is aborted. It is `60.0` seconds when `None` (default).

- *ssl_shutdown_timeout* gives, in seconds, how long to await completion of the SSL shutdown before the connection is aborted. It is `30.0` seconds when `None` (default).

Added in version 3.11.

Changed in version 3.12: Added the *ssl_shutdown_timeout* parameter.

 is_closing()

Return `True` when the stream has closed or is partway through closing.

Added in version 3.7.

 `*async *wait_closed()`

Hold off until the stream has closed.

Call it after `close()` to hang on until the underlying connection has closed, which guarantees all data is flushed before, say, the program exits.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](asyncio-streamwriter-write-to-asyncio-streamwriter-drain.md) · [Continue](tcp-echo-client-using-streams.md) · [Owning module, declaration or section: asyncio.StreamWriter](asyncio-streamwriter-class.md) · [Owning module, declaration or section: StreamWriter](asyncio-streamwriter-class.md)
