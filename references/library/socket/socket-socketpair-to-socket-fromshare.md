# socket - Creating sockets

### Functions

#### Creating sockets

Every function listed here produces socket objects.

To make a new socket on its own, use the `socket` class constructor; consult Socket Objects for the parameters it accepts and a complete writeup.

 socket.socketpair([*family*[, *type*[, *proto*]]])

Construct two connected socket objects from the supplied address family, socket type, and protocol number. The address family, socket type, and protocol number follow the same conventions as the `socket()` function. When the platform defines it, the family defaults to `AF_UNIX`; failing that, it falls back to `AF_INET`.

The sockets just created are [non-inheritable](https://docs.python.org/3.14/library/os.html#fd-inheritance).

Changed in version 3.2: The socket objects handed back now cover the full socket API instead of only part of it.

Changed in version 3.4: The sockets handed back are now non-inheritable.

Changed in version 3.5: Windows support added.

 socket.create_connection(*address*, *timeout=GLOBAL_DEFAULT*, *source_address=None*, ***, *all_errors=False*)

Establish a connection to a TCP service that is listening at the internet *address* (a 2-tuple `(host, port)`) and hand back the socket object. It sits at a higher level than `socket.connect()`: should *host* be a non-numeric hostname, the function attempts resolution under both `AF_INET` and `AF_INET6`, then works through every candidate address in sequence until one connects. That behaviour makes writing clients that handle both IPv4 and IPv6 straightforward.

Supplying the optional *timeout* argument applies that timeout to the socket instance ahead of the connection attempt. With no *timeout* provided, the function falls back to the global default timeout that `getdefaulttimeout()` returns.

When given, *source_address* has to be a 2-tuple `(host, port)` that the socket binds to as its source address prior to connecting. Should host or port be ‘’ or 0 respectively, the OS default behavior takes over.

If the connection cannot be established, an exception propagates. By default that is the exception raised for the final address tried. Setting *all_errors* to `True` instead yields an [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup) gathering the errors from every attempt.

Changed in version 3.2: *source_address* was added.

Changed in version 3.11: *all_errors* was added.

 socket.create_server(*address*, ***, *family=AF_INET*, *backlog=None*, *reuse_port=False*, *dualstack_ipv6=False*)

A convenience helper that builds a TCP socket bound to *address* (a 2-tuple `(host, port)`) and gives back the socket object.

The *family* argument has to be either `AF_INET` or `AF_INET6`. *backlog* is the queue length forwarded to `socket.listen()`; when left unspecified, a sensible default is selected. *reuse_port* governs whether the `SO_REUSEPORT` socket option gets set.

When *dualstack_ipv6* is true, *family* is `AF_INET6`, and the platform allows it, the socket can accept IPv4 alongside IPv6 connections; otherwise it raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). The majority of POSIX platforms together with Windows are expected to provide this capability. With it active, the address that `socket.getpeername()` reports for an incoming IPv4 connection appears as an IPv6 address in IPv4-mapped IPv6 form. A false *dualstack_ipv6* explicitly turns the feature off on platforms (Linux, for instance) that enable it by default. You can combine this parameter with `has_dualstack_ipv6()`:

```python
import socket

addr = ("", 8080)  # all interfaces, port 8080
if socket.has_dualstack_ipv6():
    s = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True)
else:
    s = socket.create_server(addr)

```

Note

Under POSIX platforms the `SO_REUSEADDR` socket option gets enabled so that earlier sockets bound to the same *address*, which are lingering in TIME_WAIT state, can be reused at once.

Added in version 3.8.

 socket.has_dualstack_ipv6()

Yield `True` when the platform can create a TCP socket capable of serving IPv4 and IPv6 connections alike.

Added in version 3.8.

 socket.fromfd(*fd*, *family*, *type*, *proto=0*)

Make a copy of the file descriptor *fd* (an integer such as a file object’s [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method returns) and assemble a socket object around the copy. The address family, socket type, and protocol number match those of the `socket()` function. Although the descriptor ought to point at a socket, that is not verified — later operations on the object can fail if the descriptor is bad. The function is seldom required, yet it lets you query or change socket options on a socket handed to a program as standard input or output (for example, a server launched through the Unix inet daemon). The socket is presumed to be in blocking mode.

The socket just created is [non-inheritable](https://docs.python.org/3.14/library/os.html#fd-inheritance).

Changed in version 3.4: The returned socket is now non-inheritable.

 socket.fromshare(*data*)

Recreate a socket from data produced by the `socket.share()` method. The socket is presumed to be in blocking mode.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Added in version 3.3.

[Subject index](INDEX.md) · [Continue](socket-close-to-socket-gethostname.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md)
