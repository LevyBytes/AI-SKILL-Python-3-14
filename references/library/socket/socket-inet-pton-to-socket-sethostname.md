# socket: `socket.inet_pton()`, `socket.inet_ntop()`, `socket.CMSG_LEN()`, `socket.CMSG_SPACE()`, `socket.getdefaulttimeout()`, `socket.setdefaulttimeout()`, `socket.sethostname()`

socket.inet_pton(*address_family*, *ip_string*)

Turn an IP address from its family-specific string form into a packed, binary form. `inet_pton()` comes in handy whenever a library or network protocol expects an object of type `in_addr` (much like `inet_aton()`) or `in6_addr`.

At present the accepted values for *address_family* are `AF_INET` and `AF_INET6`. When the IP address string *ip_string* is invalid, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised. Bear in mind that precisely what counts as valid depends both on the *address_family* value and on the underlying implementation of `inet_pton()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

Changed in version 3.4: Windows support added

 socket.inet_ntop(*address_family*, *packed_ip*)

Turn a packed IP address (a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) of some byte count) into its standard, family-specific string form (such as `'7.10.0.5'` or `'5aef:2b::8'`). `inet_ntop()` comes in handy whenever a library or network protocol yields an object of type `in_addr` (much like `inet_ntoa()`) or `in6_addr`.

At present the accepted values for *address_family* are `AF_INET` and `AF_INET6`. When the bytes object *packed_ip* is not the right length for the given address family, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised for errors coming from the call to `inet_ntop()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

Changed in version 3.4: Windows support added

Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is now accepted.

 socket.CMSG_LEN(*length*)

Give back the full length, excluding trailing padding, of an ancillary data item whose associated data has the given *length*. This figure can frequently serve as the buffer size for `recvmsg()` when receiving one ancillary data item, yet [**RFC 3542**](https://datatracker.ietf.org/doc/html/rfc3542.html) directs portable applications to rely on `CMSG_SPACE()` and so reserve room for padding, even where the item ends the buffer. [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised should *length* fall beyond the range of values that are allowed.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Most Unix platforms.

Added in version 3.3.

 socket.CMSG_SPACE(*length*)

Give back the buffer size that `recvmsg()` needs to receive an ancillary data item whose associated data has the given *length*, together with any trailing padding. To receive multiple items, the necessary buffer space is the total of the `CMSG_SPACE()` values computed for each item’s associated data length. [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised should *length* fall beyond the range of values that are allowed.

Be aware that some systems can support ancillary data yet not offer this function. Be aware too that sizing the buffer from this function’s results may not exactly cap how much ancillary data can be received, because extra data might still fit within the padding region.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

most Unix platforms.

Added in version 3.3.

 socket.getdefaulttimeout()

Give back the default timeout in seconds (float) applied to new socket objects. `None` means new socket objects carry no timeout. At the first import of the socket module, the default stands at `None`.

 socket.setdefaulttimeout(*timeout*)

Assign the default timeout, expressed in seconds (float), that fresh socket objects receive. Upon the socket module’s initial import, this default sits at `None`. Consult `settimeout()` for the accepted values along with what each one signifies.

 socket.sethostname(*name*)

Change the machine’s hostname to *name*. This raises an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when you lack sufficient privileges.

[Subject index](INDEX.md) · [Previous](socket-gethostbyaddr-to-socket-inet-ntoa.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Other functions](socket-close-to-socket-gethostname.md) · [Required continuation of the source contract](socket-if-nameindex-to-socket-send-fds.md)
