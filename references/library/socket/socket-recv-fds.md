# socket: `socket.recv_fds()`

socket.recv_fds(*sock*, *bufsize*, *maxfds*[, *flags*])

Read at most *maxfds* file descriptors arriving on an `AF_UNIX` socket *sock*. Return `(msg, list(fds), flags, addr)`. See `recvmsg()` for how the remaining parameters are documented.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Unix platforms supporting `recvmsg()` and `SCM_RIGHTS` mechanism.

Added in version 3.9.

Note

Any truncated integers at the end of the list of file descriptors.

[Subject index](INDEX.md) · [Previous](socket-if-nameindex-to-socket-send-fds.md) · [Continue](socket-socket-class.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Other functions](socket-close-to-socket-gethostname.md)
