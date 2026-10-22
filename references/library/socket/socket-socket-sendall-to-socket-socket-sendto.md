# socket.socket: `sendall()`, `sendto()`

sendall(*bytes*[, *flags*])

Push data onto the socket. The socket has to be connected to a remote socket. The optional *flags* argument carries the same meaning it has for `recv()`. In contrast to `send()`, this method keeps pushing data out of *bytes* until either everything has been sent or an error arises. On success `None` is returned. When an error occurs, an exception is raised, and there is no means of learning how much data, if any, made it out.

Changed in version 3.5: Each successful chunk of sent data no longer resets the socket timeout; instead, that timeout now bounds the overall time allowed to transmit every byte.

Changed in version 3.5: Should the system call be interrupted while the signal handler raises nothing, the method retries that system call rather than throwing an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception (consult [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

 sendto(*bytes*, *address*)

[Subject index](INDEX.md) · [Previous](socket-socket-recvmsg-to-socket-socket-send.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: socket.socket](socket-socket-class.md) · [Owning module, declaration or section: Socket Objects](socket-socket-class.md)
