# socket.socket: `getsockname()`, `getsockopt()`, `getblocking()`, `gettimeout()`, `ioctl()`, `listen()`, `makefile()`, `recv()`, `recvfrom()`

getsockname()

Hand back the socket's own address. For example, it lets you discover the port number of an IPv4/v6 socket. Which form the returned address takes depends on the address family — see Socket families.

 getsockopt(*level*, *optname*[, *buflen*])

Hand back the value of the specified socket option (consult the Unix man page *[getsockopt(2)](https://manpages.debian.org/getsockopt(2))*). This module defines the relevant symbolic constants (SO_* and so on). When *buflen* is omitted, the option is taken to be an integer, and the function returns its integer value. When *buflen* is supplied, it gives the maximum length of the buffer into which the option is received, and that buffer is handed back as a bytes object. Decoding what the buffer holds is left to the caller (the optional built-in [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module offers one way to decode C structures packed as byte strings).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 getblocking()

Hand back `True` when the socket is in blocking mode and `False` when it is non-blocking.

This amounts to the same thing as testing `socket.gettimeout() != 0`.

Added in version 3.7.

 gettimeout()

Hand back the timeout in seconds (float) tied to socket operations, or `None` when no timeout has been set. It mirrors the most recent call to `setblocking()` or `settimeout()`.

 ioctl(*control*, *option*)

Here the `ioctl()` method offers only a narrow interface onto the WSAIoctl system interface. Consult the [Win32 documentation](https://msdn.microsoft.com/en-us/library/ms741621%28VS.85%29.aspx) for further details.

Elsewhere, the general-purpose [`fcntl.fcntl()`](https://docs.python.org/3.14/library/fcntl.html#fcntl.fcntl) and [`fcntl.ioctl()`](https://docs.python.org/3.14/library/fcntl.html#fcntl.ioctl) functions are available; each takes a socket object as its first argument.

At present the only control codes handled are `SIO_RCVALL`, `SIO_KEEPALIVE_VALS`, and `SIO_LOOPBACK_FAST_PATH`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

Changed in version 3.6: `SIO_LOOPBACK_FAST_PATH` was added.

 listen([*backlog*])

Allow a server to take connections. When *backlog* is given, its value has to be 0 or greater (anything lower is clamped to 0); it sets how many unaccepted connections the system permits before it turns away new ones. When omitted, a sensible default value is selected.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

Changed in version 3.5: The *backlog* parameter is now optional.

 makefile(*mode='r'*, *buffering=None*, ***, *encoding=None*, *errors=None*, *newline=None*)

Hand back a [file object](https://docs.python.org/3.14/glossary.html#term-file-object) tied to the socket. Precisely which type is returned hinges on the arguments handed to `makefile()`. Those arguments carry the same interpretation they have for the built-in [`open()`](https://docs.python.org/3.14/library/functions.html#open) function, save that *mode* accepts only `'r'` (default), `'w'`, `'b'`, or some mix of these.

The socket has to be in blocking mode; a timeout is permitted, but the file object's internal buffer can be left inconsistent if a timeout fires.

Closing the file object that `makefile()` returns will not close the original socket unless every other file object has already been closed and `socket.close()` has been invoked on the socket object.

Note

On Windows, the file-like object that `makefile()` builds cannot serve anywhere a file object backed by a file descriptor is required, such as the stream arguments to [`subprocess.Popen()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen).

 recv(*bufsize*[, *flags*])

Read data off the socket. What comes back is a bytes object carrying the data received. Use *bufsize* to cap how much data is read in a single call. When an empty bytes object is returned, the client has disconnected. For the sense of the optional *flags* argument, consult the Unix manual page *[recv(2)](https://manpages.debian.org/recv(2))*; it defaults to zero.

Changed in version 3.5: Should the system call be interrupted while the signal handler raises nothing, the method retries that system call rather than throwing an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception (consult [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

 recvfrom(*bufsize*[, *flags*])

Read data off the socket. What comes back is a pair `(bytes, address)`, where *bytes* is a bytes object carrying the data received and *address* is the address of the socket that sent it. For the sense of the optional *flags* argument, consult the Unix manual page *[recv(2)](https://manpages.debian.org/recv(2))*; it defaults to zero. Which form *address* takes is determined by the address family — see Socket families.

Changed in version 3.5: Should the system call be interrupted while the signal handler raises nothing, the method retries that system call rather than throwing an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception (consult [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

Changed in version 3.7: With a multicast IPv6 address, the first element of *address* no longer carries the `%scope_id` part; to obtain the complete IPv6 address, call `getnameinfo()`.

[Subject index](INDEX.md) · [Previous](socket-socket-accept-to-socket-socket-getpeername.md) · [Continue](socket-socket-recvmsg-to-socket-socket-send.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: socket.socket](socket-socket-class.md) · [Owning module, declaration or section: Socket Objects](socket-socket-class.md)
