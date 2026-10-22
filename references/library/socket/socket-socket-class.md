# socket: `socket.socket`

### Socket Objects

 *class *socket.socket(*family=AF_INET*, *type=SOCK_STREAM*, *proto=0*, *fileno=None*)

Build a fresh socket from the supplied address family, socket type, and protocol number. For the address family, choose `AF_INET` (the default), `AF_INET6`, `AF_UNIX`, `AF_CAN`, `AF_PACKET`, or `AF_RDS`. For the socket type, pick `SOCK_STREAM` (the default), `SOCK_DGRAM`, `SOCK_RAW`, or another of the `SOCK_` constants. Typically the protocol number is zero and can simply be left out; however, when the address family is `AF_CAN`, supply one of `CAN_RAW`, `CAN_BCM`, `CAN_ISOTP`, or `CAN_J1939` for the protocol.

When *fileno* is provided, the *family*, *type*, and *proto* values are inferred automatically from that file descriptor. You can override this inference by passing explicit *family*, *type*, or *proto* arguments. Doing so changes only Python's view of things — for example, what `socket.getpeername()` reports — rather than the underlying OS resource. In contrast to `socket.fromfd()`, supplying *fileno* yields the very same socket rather than a copy. That behavior can be handy when closing a detached socket through `socket.close()`.

The newly created socket is [non-inheritable](https://docs.python.org/3.14/library/os.html#fd-inheritance).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.__new__` with arguments `self`, `family`, `type`, `protocol`.

Changed in version 3.3: Added both the AF_CAN and the AF_RDS families.

Changed in version 3.4: The CAN_BCM protocol was added.

Changed in version 3.4: The returned socket is now non-inheritable.

Changed in version 3.7: The CAN_ISOTP protocol was added.

Changed in version 3.7: Whenever the `SOCK_NONBLOCK` or `SOCK_CLOEXEC` bit flags are set on *type*, they get stripped out, so `socket.type` won't show them. Those flags are nonetheless forwarded to the platform's underlying `socket()` call. As a result,

```python
sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM | socket.SOCK_NONBLOCK)

```

will still produce a non-blocking socket on operating systems that honor `SOCK_NONBLOCK`, yet `sock.type` ends up reported as `socket.SOCK_STREAM`.

Changed in version 3.9: The CAN_J1939 protocol was added.

Changed in version 3.10: The IPPROTO_MPTCP protocol was added.

The methods listed below belong to socket objects. With the exception of `makefile()`, each maps to a Unix system call that applies to sockets.

Changed in version 3.2: Added support for the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol; leaving the context manager has the same effect as a `close()` call.

[Subject index](INDEX.md) · [Previous](socket-recv-fds.md) · [Continue](socket-socket-accept-to-socket-socket-getpeername.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md)
