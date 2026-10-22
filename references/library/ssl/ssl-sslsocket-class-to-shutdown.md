# ssl: `ssl.SSLSocket`, `accept()`, `bind()`, `close()`, `connect()`, `detach()`, `fileno()`, `getpeername()`, `getsockopt()`, `gettimeout()`, `listen()`, `makefile()`, `recv()`, `send()`, `sendfile()`, `shutdown()`

### SSL sockets

 *class *ssl.SSLSocket(*socket.socket*)

SSL sockets supply these methods of [Socket Objects](https://docs.python.org/3.14/library/socket.html#socket-objects):

- [`accept()`](https://docs.python.org/3.14/library/socket.html#socket.socket.accept)

- [`bind()`](https://docs.python.org/3.14/library/socket.html#socket.socket.bind)

- [`close()`](https://docs.python.org/3.14/library/socket.html#socket.socket.close)

- [`connect()`](https://docs.python.org/3.14/library/socket.html#socket.socket.connect)

- [`detach()`](https://docs.python.org/3.14/library/socket.html#socket.socket.detach)

- [`fileno()`](https://docs.python.org/3.14/library/socket.html#socket.socket.fileno)

- [`getpeername()`](https://docs.python.org/3.14/library/socket.html#socket.socket.getpeername), [`getsockname()`](https://docs.python.org/3.14/library/socket.html#socket.socket.getsockname)

- [`getsockopt()`](https://docs.python.org/3.14/library/socket.html#socket.socket.getsockopt), [`setsockopt()`](https://docs.python.org/3.14/library/socket.html#socket.socket.setsockopt)

- [`gettimeout()`](https://docs.python.org/3.14/library/socket.html#socket.socket.gettimeout), [`settimeout()`](https://docs.python.org/3.14/library/socket.html#socket.socket.settimeout), [`setblocking()`](https://docs.python.org/3.14/library/socket.html#socket.socket.setblocking)

- [`listen()`](https://docs.python.org/3.14/library/socket.html#socket.socket.listen)

- [`makefile()`](https://docs.python.org/3.14/library/socket.html#socket.socket.makefile)

- [`recv()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recv), [`recv_into()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recv_into) (but passing a non-zero `flags` argument is not allowed)

- [`send()`](https://docs.python.org/3.14/library/socket.html#socket.socket.send), [`sendall()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendall) (with the same limitation)

- [`sendfile()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendfile) (though [`os.sendfile`](https://docs.python.org/3.14/library/os.html#os.sendfile) applies solely to plain-text sockets, and otherwise [`send()`](https://docs.python.org/3.14/library/socket.html#socket.socket.send) is used)

- [`shutdown()`](https://docs.python.org/3.14/library/socket.html#socket.socket.shutdown)

That said, because the SSL (and TLS) protocol layers its own framing on top of TCP, the SSL sockets abstraction may, in some ways, depart from how ordinary OS-level sockets are specified. Pay particular attention to the notes covering non-blocking sockets.

`SSLSocket` instances have to be created through the `SSLContext.wrap_socket()` method.

Changed in version 3.5: The `sendfile()` method was added.

Changed in version 3.5: With `shutdown()`, the socket timeout is not restarted on each receipt or send of bytes. That timeout now caps the entire duration of the shutdown.

Deprecated since version 3.6: Creating a `SSLSocket` instance directly is deprecated; wrap a socket with `SSLContext.wrap_socket()` instead.

Changed in version 3.7: `SSLSocket` instances now have to come from `wrap_socket()`. Prior releases let you build instances straight away, but that path was neither documented nor officially backed.

Changed in version 3.10: Internally, Python has switched to `SSL_read_ex` and `SSL_write_ex`. Those functions let you read and write payloads bigger than 2 GB. A zero-length write no longer triggers a protocol violation error.

SSL sockets carry these extra methods and attributes as well:

[Subject index](INDEX.md) · [Previous](ssl-tlsversion-class-to-tlsversion-tlsv1-3.md) · [Continue](sslsocket-read-to-sslsocket-do-handshake.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)
