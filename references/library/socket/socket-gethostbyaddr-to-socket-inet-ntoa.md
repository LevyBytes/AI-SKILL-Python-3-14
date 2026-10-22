# socket: Host and service lookup, byte order and IPv4 conversion

socket.gethostbyaddr(*ip_address*)

Hand back a 3-tuple `(hostname, aliaslist, ipaddrlist)`: here *hostname* names the main host name that answers for the given *ip_address*, *aliaslist* gives a (possibly empty) collection of additional host names tied to that same address, and *ipaddrlist* enumerates the IPv4/v6 addresses belonging to that interface on that host (most commonly a lone address). To obtain the fully qualified domain name, call the function `getfqdn()`. `gethostbyaddr()` works with both IPv4 and IPv6.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.gethostbyaddr` with argument `ip_address`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 socket.getnameinfo(*sockaddr*, *flags*)

Convert a socket address *sockaddr* into a 2-tuple `(host, port)`. According to the *flags* in effect, *host* in the result may carry either a fully qualified domain name or a numeric address form. Likewise, *port* may hold a string port name or a numeric port number.

With IPv6 addresses, `%scope_id` is tacked onto the host portion whenever *sockaddr* carries a meaningful *scope_id*. That generally arises with multicast addresses.

Further information on *flags* is available in *[getnameinfo(3)](https://manpages.debian.org/getnameinfo(3))*.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.getnameinfo` with argument `sockaddr`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 socket.getprotobyname(*protocolname*)

Convert an internet protocol name (such as `'icmp'`) into a constant fit for the (optional) third argument of the `socket()` function. You typically only need this for sockets opened in “raw” mode (`SOCK_RAW`); under the ordinary socket modes the right protocol is selected automatically whenever the protocol is left out or set to zero.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 socket.getservbyname(*servicename*[, *protocolname*])

Convert an internet service name plus a protocol name into the port number for that service. The optional protocol name, when supplied, ought to be `'tcp'` or `'udp'`; otherwise every protocol matches.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.getservbyname` with arguments `servicename`, `protocolname`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 socket.getservbyport(*port*[, *protocolname*])

Convert an internet port number plus a protocol name into the service name for that service. The optional protocol name, when supplied, ought to be `'tcp'` or `'udp'`; otherwise every protocol matches.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.getservbyport` with arguments `port`, `protocolname`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 socket.ntohl(*x*)

Turn 32-bit positive integers from network byte order into host byte order. Where the host byte order already equals network byte order, nothing happens; elsewhere a 4-byte swap is carried out.

 socket.ntohs(*x*)

Turn 16-bit positive integers from network byte order into host byte order. Where the host byte order already equals network byte order, nothing happens; elsewhere a 2-byte swap is carried out.

Changed in version 3.10: When *x* will not fit inside a 16-bit unsigned integer, [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised.

 socket.htonl(*x*)

Turn 32-bit positive integers from host byte order into network byte order. Where the host byte order already equals network byte order, nothing happens; elsewhere a 4-byte swap is carried out.

 socket.htons(*x*)

Turn 16-bit positive integers from host byte order into network byte order. Where the host byte order already equals network byte order, nothing happens; elsewhere a 2-byte swap is carried out.

Changed in version 3.10: When *x* will not fit inside a 16-bit unsigned integer, [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised.

 socket.inet_aton(*ip_string*)

Turn an IPv4 address given in dotted-quad string form (such as ‘123.45.67.89’) into 32-bit packed binary form, returned as a bytes object four characters long. This helps when talking to a program built on the standard C library that expects objects of type `in_addr`, the C type for the 32-bit packed binary this function produces.

`inet_aton()` will also take strings carrying fewer than three dots; the Unix manual page *[inet(3)](https://manpages.debian.org/inet(3))* covers the specifics.

Should the IPv4 address string handed to this function be invalid, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised. Bear in mind that precisely what counts as valid hinges on the underlying C implementation of `inet_aton()`.

Because `inet_aton()` lacks IPv6 support, use `inet_pton()` instead when you need IPv4/v6 dual stack support.

 socket.inet_ntoa(*packed_ip*)

Turn a 32-bit packed IPv4 address (a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) four bytes long) into its standard dotted-quad string form (such as ‘123.45.67.89’). This helps when talking to a program built on the standard C library that expects objects of type `in_addr`, the C type for the 32-bit packed binary data this function accepts.

Should the byte sequence handed to this function not be exactly 4 bytes long, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised. Because `inet_ntoa()` lacks IPv6 support, use `inet_ntop()` instead when you need IPv4/v6 dual stack support.

Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is now accepted.

[Subject index](INDEX.md) · [Previous](socket-close-to-socket-gethostname.md) · [Continue](socket-inet-pton-to-socket-sethostname.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Other functions](socket-close-to-socket-gethostname.md)
