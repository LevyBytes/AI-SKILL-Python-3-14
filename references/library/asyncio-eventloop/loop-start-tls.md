# TLS upgrade

### TLS upgrade

 *async *loop.start_tls(*transport*, *protocol*, *sslcontext*, ***, *server_side=False*, *server_hostname=None*, *ssl_handshake_timeout=None*, *ssl_shutdown_timeout=None*)

Promote a current transport-based connection to TLS.

Build a TLS coder/decoder instance and place it between the *transport* and the *protocol*. That coder/decoder fulfills both the *transport*-facing protocol and the *protocol*-facing transport.

Hand back the two-interface instance that was created. Once *await* completes, the *protocol* must cease using the original *transport* and talk solely to the returned object, since the coder buffers *protocol*-side data and intermittently trades additional TLS session packets with *transport*.

Certain cases (for instance, when the supplied transport is already in the process of closing) may cause this to return `None`.

Parameters:

- *transport* and *protocol* instances that methods like `create_server()` and `create_connection()` return.

- *sslcontext*: a configured instance of [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext).

- *server_side* pass `True` while upgrading a server-side connection (such as one produced by `create_server()`).

- *server_hostname*: assigns or overrides the host name checked against the certificate of the target server.

- *ssl_handshake_timeout* sets, for a TLS connection, how many seconds to await completion of the TLS handshake before the connection is aborted. It is `60.0` seconds when `None` (the default).

- *ssl_shutdown_timeout* sets how many seconds to await completion of the SSL shutdown before the connection is aborted. It is `30.0` seconds when `None` (the default).

Added in version 3.7.

Changed in version 3.11: the *ssl_shutdown_timeout* parameter arrived.

[Subject index](INDEX.md) · [Previous](loop-sendfile.md) · [Continue](loop-add-reader-to-loop-remove-writer.md)
