# test.support.socket_helper`test.support.socket_helper` - Utilities for socket tests

### `test.support.socket_helper` - Utilities for socket tests

The `test.support.socket_helper` module offers support for socket tests.

Added in version 3.9.

 test.support.socket_helper.IPV6_ENABLED

Holds `True` when IPv6 is turned on for this host, and `False` if not.

 test.support.socket_helper.find_unused_port(*family=socket.AF_INET*, *socktype=socket.SOCK_STREAM*)

Hands back a free port appropriate for binding. It does this by making a temporary socket sharing the family and type of the `sock` parameter (the default being [`AF_INET`](https://docs.python.org/3.14/library/socket.html#socket.AF_INET), [`SOCK_STREAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_STREAM)), then binding that to the given host address (defaulting to `0.0.0.0`) with the port at 0, which draws a free ephemeral port from the OS. Afterward the temporary socket is closed and removed, and the ephemeral port is handed back.

For any test in which a server socket has to stay bound to a specific port across the test, use either this function or `bind_port()`. The choice between them hinges on whether the calling code builds a Python socket itself, or whether a free port must be handed to a constructor or given to an outside program (for example, the `-accept` argument for openssl's s_server mode). Wherever you can, favor `bind_port()` ahead of `find_unused_port()`. Relying on a hard-coded port is frowned upon, since it can prevent several copies of the test from running at once, which troubles buildbots.

 test.support.socket_helper.bind_port(*sock*, *host=HOST*)

Binds the socket to an open port and yields that port number. It leans on ephemeral ports so as to guarantee the port we use is unbound. This matters because numerous tests might run at once, particularly inside a buildbot setting. The method throws an exception when the `sock.family` is [`AF_INET`](https://docs.python.org/3.14/library/socket.html#socket.AF_INET) and the `sock.type` is [`SOCK_STREAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_STREAM) while the socket carries `SO_REUSEADDR` or `SO_REUSEPORT`. Tests must never apply these socket options to TCP/IP sockets. The lone reason to apply them is to test multicasting across several UDP sockets.

On top of that, when the `SO_EXCLUSIVEADDRUSE` socket option exists (that is, on Windows), it gets applied to the socket. That keeps anyone else from binding to our host/port across the test.

 test.support.socket_helper.bind_unix_socket(*sock*, *addr*)

Binds a Unix socket, and raises [`unittest.SkipTest`](https://docs.python.org/3.14/library/unittest.html#unittest.SkipTest) whenever [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError) is raised.

 @test.support.socket_helper.skip_unless_bind_unix_socket

A decorator for running tests that depend on a working `bind()` for Unix sockets.

 test.support.socket_helper.transient_internet(*resource_name*, ***, *timeout=30.0*, *errnos=()*)

A context manager that raises `ResourceDenied` whenever assorted internet-connection problems surface as exceptions.

[Subject index](INDEX.md) · [Previous](../test-support/test-matcher-class-and-value-matching.md) · [Continue](../test-support-script-helper/interpreter-test-environment-and-package-helpers.md)
