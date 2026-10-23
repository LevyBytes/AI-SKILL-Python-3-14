# socket - Notes on socket timeouts

### Notes on socket timeouts

Any socket object sits in one of three modes: blocking, non-blocking, or timeout. By default every socket starts out in blocking mode, though a call to `setdefaulttimeout()` can change that.

- Under *blocking mode*, an operation blocks right through to completion, or until the system hands back an error (a connection-timed-out error, say).

- Under *non-blocking mode*, an operation fails (with an error that is, regrettably, system-dependent) whenever it can't finish straight away: the [`select`](https://docs.python.org/3.14/library/select.html#module-select) module's functions let you learn when, and whether, a socket is ready to be read from or written to.

- Under *timeout mode*, an operation fails if it can't finish inside the timeout set for the socket (a `timeout` exception is raised) or if the system hands back an error.

Note

Down at the operating system level, sockets in *timeout mode* are placed in non-blocking mode internally. On top of that, file descriptors and socket objects pointing at the same network endpoint share the blocking and timeout modes between them. This implementation quirk can show through if, for instance, you choose to work with a socket's `fileno()`.

[Subject index](INDEX.md) · [Previous](socket-sockettype-class.md) · [Continue](timeouts-and-the-connect-method.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md)
