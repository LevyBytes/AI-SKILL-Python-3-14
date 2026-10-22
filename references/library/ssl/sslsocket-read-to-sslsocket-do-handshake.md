# ssl: `SSLSocket.read()`, `SSLSocket.write()`, `SSLSocket.do_handshake()`

SSLSocket.read(*len=1024*, *buffer=None*)

Read at most *len* bytes from the SSL socket and hand back the result as a `bytes` instance. When *buffer* is given, read into that buffer instead and hand back how many bytes were read.

When the socket is non-blocking and reading would block, raise `SSLWantReadError` or `SSLWantWriteError`.

Because a re-negotiation may occur at any moment, calling `read()` can trigger write operations as well.

Changed in version 3.5: The socket timeout is not restarted on each receipt or send of bytes. It now caps the entire span allowed to read up to *len* bytes.

Deprecated since version 3.6: Use `recv()` instead of `read()`.

 SSLSocket.write(*data*)

Write *data* to the SSL socket and hand back how many bytes were written. The *data* argument has to be an object that supports the buffer interface.

When the socket is non-blocking and writing would block, raise `SSLWantReadError` or `SSLWantWriteError`.

Because a re-negotiation may occur at any moment, calling `write()` can trigger read operations as well.

Changed in version 3.5: The socket timeout is not restarted on each receipt or send of bytes. It now caps the entire span allowed to write *data*.

Deprecated since version 3.6: Use `send()` instead of `write()`.

Note

The `read()` and `write()` methods are the low-level routines that handle unencrypted, application-level data and convert it to and from encrypted, wire-level data. They depend on a live SSL connection, meaning the handshake finished and `SSLSocket.unwrap()` has not yet been called.

Under normal circumstances you ought to rely on the socket API methods such as [`recv()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recv) and [`send()`](https://docs.python.org/3.14/library/socket.html#socket.socket.send) rather than these.

 SSLSocket.do_handshake(*block=False*)

Carry out the SSL setup handshake.

When *block* is true and the timeout returned by [`gettimeout()`](https://docs.python.org/3.14/library/socket.html#socket.socket.gettimeout) is zero, the socket switches to blocking mode until the handshake finishes.

Changed in version 3.4: When the socket's `context` has its `check_hostname` attribute set to true, the handshake method additionally runs `match_hostname()`.

Changed in version 3.5: The socket timeout is not restarted on each receipt or send of bytes. It now caps the entire duration of the handshake.

Changed in version 3.7: It is OpenSSL that now matches the hostname or IP address while the handshake runs, and `match_hostname()` is no longer called. Should OpenSSL reject a hostname or IP address, the handshake stops early and the peer receives a TLS alert message.

[Subject index](INDEX.md) · [Previous](ssl-sslsocket-class-to-shutdown.md) · [Continue](sslsocket-getpeercert-to-sslsocket-compression.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: ssl.SSLSocket](ssl-sslsocket-class-to-shutdown.md) · [Owning module, declaration or section: SSL sockets](ssl-sslsocket-class-to-shutdown.md)
