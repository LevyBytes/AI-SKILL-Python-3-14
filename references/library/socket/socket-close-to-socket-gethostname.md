# socket: `socket.close()`, `socket.getaddrinfo()`, `socket.getfqdn()`, `socket.gethostbyname()`, `socket.gethostbyname_ex()`, `socket.gethostname()`

#### Other functions

A range of additional network-related services is provided by the `socket` module:

 socket.close(*fd*)

Shut down a socket file descriptor. It behaves like [`os.close()`](https://docs.python.org/3.14/library/os.html#os.close) but applies to sockets. On certain platforms (Windows above all) `os.close()` cannot handle socket file descriptors.

Added in version 3.7.

 socket.getaddrinfo(*host*, *port*, *family=AF_UNSPEC*, *type=0*, *proto=0*, *flags=0*)

This function wraps the C function `getaddrinfo` of the underlying system.

Convert the *host*/*port* pair into a list of 5-tuples carrying every argument required to build a socket connected to that service. *host* may be a domain name, a string form of an IPv4/v6 address, or `None`. *port* may be a string service name like `'http'`, a numeric port, or `None`. Supplying `None` for both *host* and *port* lets you forward `NULL` to the underlying C API.

You can optionally set the *family*, *type*, and *proto* arguments to supply options and narrow the returned address list. Leave them at their defaults (`AF_UNSPEC`, 0, and 0, respectively) to keep the results unrestricted. Details appear in the note below.

The *flags* argument accepts one or more of the `AI_*` constants and shapes how the results are computed and returned. As an example, `AI_NUMERICHOST` turns off domain name resolution and raises an error when *host* is a domain name.

The function returns a list of 5-tuples with the following structure:

`(family, type, proto, canonname, sockaddr)`

Within each tuple, *family*, *type*, and *proto* are integers intended for the `socket()` function. *canonname* holds a string giving the canonical name of the *host* when `AI_CANONNAME` appears among the *flags*; otherwise *canonname* stays empty. *sockaddr* is a tuple that describes a socket address; its layout depends on the *family* returned (with `AF_INET` it is a `(address, port)` 2-tuple, and with `AF_INET6` a `(address, port, flowinfo, scope_id)` 4-tuple), and it is meant to be handed to the `socket.connect()` method.

Note

When you plan to feed `getaddrinfo()` output into socket creation (instead of, say, reading *canonname*), think about narrowing the results by *type* (such as `SOCK_STREAM` or `SOCK_DGRAM`) and/or *proto* (such as `IPPROTO_TCP` or `IPPROTO_UDP`) that your application supports.

How the call behaves with default *family*, *type*, *proto*, and *flags* values varies by system.

A great many systems (for instance, most Linux setups) hand back a sorted list of every matching address. As a rule these addresses ought to be attempted in order until a connection works (potentially in parallel, for example via a [Happy Eyeballs](https://en.wikipedia.org/wiki/Happy_Eyeballs) algorithm). Here, restricting *type* and/or *proto* can cut out failing or unusable connection attempts.

Certain systems, though, hand back only one address. (Such a report came, for example, from Solaris and AIX setups.) On such systems, restricting *type* and/or *proto* helps guarantee that the single address is usable.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.getaddrinfo` with arguments `host`, `port`, `family`, `type`, `protocol`.

The example below retrieves address details for a hypothetical TCP connection to `example.org` on port 80 (your system may show different results when IPv6 is disabled):

```python
>>> socket.getaddrinfo("example.org", 80, proto=socket.IPPROTO_TCP)
[(socket.AF_INET6, socket.SOCK_STREAM,
 6, '', ('2606:2800:220:1:248:1893:25c8:1946', 80, 0, 0)),
 (socket.AF_INET, socket.SOCK_STREAM,
 6, '', ('93.184.216.34', 80))]

```

Changed in version 3.2: you may now supply the parameters as keyword arguments.

Changed in version 3.7: with IPv6 multicast addresses, the string standing for an address omits the `%scope_id` portion.

 socket.getfqdn([*name*])

Give back a fully qualified domain name for *name*. When *name* is left out or empty, it is taken to mean the local host. To determine the fully qualified name, the function inspects the hostname from `gethostbyaddr()`, then any host aliases that exist. It picks the first name that contains a period. When no fully qualified domain name can be found and *name* was supplied, that *name* comes back unchanged. When *name* was empty or matched `'0.0.0.0'`, the hostname from `gethostname()` is returned.

 socket.gethostbyname(*hostname*)

Convert a host name into IPv4 address form. The IPv4 address comes back as a string like `'100.50.200.5'`. When the host name is already an IPv4 address, it is returned unchanged. Refer to `gethostbyname_ex()` for a fuller interface. Because `gethostbyname()` cannot resolve IPv6 names, use `getaddrinfo()` instead when you need IPv4/v6 dual stack support.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.gethostbyname` with argument `hostname`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 socket.gethostbyname_ex(*hostname*)

Convert a host name into IPv4 address form through the extended interface. It hands back a 3-tuple `(hostname, aliaslist, ipaddrlist)`: here *hostname* names the host’s main host name, *aliaslist* gives a (possibly empty) collection of additional host names tied to that same address, and *ipaddrlist* enumerates the IPv4 addresses belonging to that interface on that host (often, but not always, a lone address). Because `gethostbyname_ex()` cannot resolve IPv6 names, use `getaddrinfo()` instead when you need IPv4/v6 dual stack support.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.gethostbyname` with argument `hostname`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 socket.gethostname()

Give back a string holding the hostname of the machine on which the Python interpreter is running right now.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.gethostname` with no arguments.

Note: since `gethostname()` will not always give the fully qualified domain name, reach for `getfqdn()` to obtain it.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

[Subject index](INDEX.md) · [Previous](socket-socketpair-to-socket-fromshare.md) · [Continue](socket-gethostbyaddr-to-socket-inet-ntoa.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md)
