# logging.handlers: `logging.handlers.SysLogHandler`

### SysLogHandler

Found in the `logging.handlers` module, the `SysLogHandler` class supports sending logging messages to a remote or local Unix syslog.

 *class *logging.handlers.SysLogHandler(*address=('localhost', SYSLOG_UDP_PORT)*, *facility=LOG_USER*, *socktype=socket.SOCK_DGRAM*, *timeout=None*)

Hands back a fresh instance of the `SysLogHandler` class meant to talk to a remote Unix machine whose address is given by *address* as a `(host, port)` tuple. When *address* is left unspecified, `('localhost', 514)` applies. The address serves to open a socket. As an alternative to a `(host, port)` tuple, you can supply an address as a string, for example '/dev/log'. With such a string, a Unix domain socket carries the message to the syslog. When *facility* is left unspecified, `LOG_USER` applies. The kind of socket opened hinges on the *socktype* argument, whose default of [`socket.SOCK_DGRAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_DGRAM) thereby yields a UDP socket. For a TCP socket instead (handy with the more recent syslog daemons like rsyslog), pass a value of [`socket.SOCK_STREAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_STREAM). When *timeout* is given, it imposes a timeout (in seconds) on the socket operations. This can keep the program from hanging forever should the syslog server be unreachable. By default, *timeout* is `None`, which means no timeout is applied.

Note that if your server isn't listening on UDP port 514, `SysLogHandler` may seem not to work. When that happens, work out which address a domain socket calls for — that varies by system. On Linux, for instance, it's typically '/dev/log', whereas on OS/X it's '/var/run/syslog'. You'll have to inspect your platform and pick the proper address (this check may have to run at runtime should your application need to operate across several platforms). On Windows, you pretty much have to fall back on the UDP option.

Note

On macOS 12.x (Monterey), Apple has altered how their syslog daemon behaves — it no longer listens on a domain socket. As a result, you can't count on `SysLogHandler` working on this system.

See [gh-91070](https://github.com/python/cpython/issues/91070) for more information.

Changed in version 3.2: *socktype* was added.

Changed in version 3.14: *timeout* was added.

[Subject index](INDEX.md) · [Previous](datagram-handler-emission-and-send.md) · [Continue](syslog-handler-lifecycle-and-emission.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)
