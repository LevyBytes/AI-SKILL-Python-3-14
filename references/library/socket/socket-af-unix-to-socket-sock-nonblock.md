# socket: `socket.AF_UNIX`, `socket.AF_INET`, `socket.AF_INET6`, `socket.AF_UNSPEC`, `socket.SOCK_STREAM`, `socket.SOCK_DGRAM`, `socket.SOCK_RAW`, `socket.SOCK_RDM`, `socket.SOCK_SEQPACKET`, `socket.SOCK_CLOEXEC`, `socket.SOCK_NONBLOCK`

### Constants

The AF_* and SOCK_* constants are now `AddressFamily` and `SocketKind` [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) collections.

Added in version 3.4.

 socket.AF_UNIX

 socket.AF_INET

 socket.AF_INET6

These constants stand for the address (and protocol) families and serve as the first argument to `socket()`. Should the `AF_UNIX` constant be undefined, that protocol is unsupported. Depending on the system, further constants may be on hand.

 socket.AF_UNSPEC

`AF_UNSPEC` signals that `getaddrinfo()` ought to return socket addresses for whatever address family — IPv4, IPv6, or anything else — that can be used.

 socket.SOCK_STREAM

 socket.SOCK_DGRAM

 socket.SOCK_RAW

 socket.SOCK_RDM

 socket.SOCK_SEQPACKET

These constants stand for the socket types and serve as the second argument to `socket()`. Depending on the system, further constants may be on hand. (In general, only `SOCK_STREAM` and `SOCK_DGRAM` seem broadly useful.)

 socket.SOCK_CLOEXEC

 socket.SOCK_NONBLOCK

When defined, these two constants can be OR'd with the socket types, letting you set certain flags atomically (which sidesteps possible race conditions and the need for separate calls).

See also

[Secure File Descriptor Handling](https://udrepper.livejournal.com/20407.html) for a more thorough explanation.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27.

Added in version 3.2.

 SO_*

[Subject index](INDEX.md) · [Previous](socket-error-to-socket-timeout.md) · [Continue](socket-somaxconn-to-socket-can-bcm.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md)
