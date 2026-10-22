# socket.socket: `accept()`, `bind()`, `close()`, `connect()`, `connect_ex()`, `detach()`, `dup()`, `fileno()`, `get_inheritable()`, `getpeername()`

accept()

Take an incoming connection. Beforehand, the socket has to be bound to an address and set to listen for connections. What comes back is a pair `(conn, address)`, in which *conn* is a *new* socket object you use to exchange data over the connection, and *address* is the address bound to the socket at the connection's far end.

The newly created socket is [non-inheritable](https://docs.python.org/3.14/library/os.html#fd-inheritance).

Changed in version 3.4: The socket is now non-inheritable.

Changed in version 3.5: Should the system call be interrupted while the signal handler raises nothing, the method retries that system call rather than throwing an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception (consult [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

 bind(*address*)

Attach the socket to *address*. It must not have been bound already. Which form *address* takes is determined by the address family — see Socket families.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.bind` with arguments `self`, `address`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 close()

Flag the socket as closed. Its backing system resource (for instance, a file descriptor) is closed too, but only after every file object produced by `makefile()` has been closed. From that point onward, any further operation on the socket object raises an error. Once the queued data has drained, the far end receives nothing more.

Garbage collection closes sockets on its own, yet calling `close()` on them explicitly — or wrapping them in a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement — is the recommended practice.

Changed in version 3.6: An [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) now gets raised whenever the backing `close()` call hits an error.

Note

Although `close()` frees the resource tied to a connection, it does not always tear the connection down right away. To shut the connection down promptly, invoke `shutdown()` ahead of `close()`.

 connect(*address*)

Open a connection to a remote socket located at *address*. Which form *address* takes is determined by the address family — see Socket families.

Should a signal interrupt the connection attempt while the socket is blocking or has a timeout and the signal handler raises nothing, the method holds on until the connection finishes or, on timeout, raises a [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError). With non-blocking sockets, the method throws an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception when a signal interrupts the connection (or whatever exception the signal handler itself raises).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.connect` with arguments `self`, `address`.

Changed in version 3.5: Rather than throwing an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception, the method now holds until the connection finishes when a signal interrupts it, provided the signal handler raises nothing and the socket is blocking or has a timeout (consult the [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 connect_ex(*address*)

Behaves like `connect(address)`, except it hands back an error indicator instead of throwing an exception for failures reported by the C-level `connect()` call (other troubles, like “host not found,” may still raise exceptions). That indicator is `0` when the operation worked; otherwise it holds the value of the `errno` variable. This proves handy for things such as asynchronous connects.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.connect` with arguments `self`, `address`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 detach()

Move the socket object into a closed state while leaving its underlying file descriptor open. That file descriptor is handed back and remains available for other uses.

Added in version 3.2.

 dup()

Duplicate the socket.

The newly created socket is [non-inheritable](https://docs.python.org/3.14/library/os.html#fd-inheritance).

Changed in version 3.4: The socket is now non-inheritable.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 fileno()

Hand back the socket's file descriptor (a small integer), or -1 when it fails. It comes in handy with [`select.select()`](https://docs.python.org/3.14/library/select.html#select.select).

On Windows, the small integer this method yields is not accepted wherever a file descriptor would be (for example, [`os.fdopen()`](https://docs.python.org/3.14/library/os.html#os.fdopen)). On Unix no such restriction applies.

 get_inheritable()

Read the [inheritable flag](https://docs.python.org/3.14/library/os.html#fd-inheritance) on the socket's file descriptor or socket's handle: `True` when child processes may inherit the socket, `False` when they may not.

Added in version 3.4.

 getpeername()

Hand back the remote address the socket has connected to. For example, it lets you discover the port number of a remote IPv4/v6 socket. Which form the returned address takes depends on the address family — see Socket families. Certain systems lack support for this function.

[Subject index](INDEX.md) · [Previous](socket-socket-class.md) · [Continue](socket-socket-getsockname-to-socket-socket-recvfrom.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: socket.socket](socket-socket-class.md) · [Owning module, declaration or section: Socket Objects](socket-socket-class.md)
