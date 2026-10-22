# socket.socket: `setsockopt()`, `shutdown()`, `share()`

setsockopt(*level*, *optname*, *value: [int](https://docs.python.org/3.14/library/functions.html#int) | [Buffer](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer)*)

 setsockopt(*level*, *optname*, *None*, *optlen: int*)

Assign the value for the named socket option (consult the Unix manual page *[setsockopt(2)](https://manpages.debian.org/setsockopt(2))*). This module defines the symbolic constants you'll need (SO_* etc. &lt;socket-unix-constants&gt;). What you pass as the value may be an integer, `None`, or a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) standing for a buffer. In that last case, the caller bears responsibility for making sure the bytestring holds the right bits (the optional built-in module [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) shows one way to encode C structures as bytestrings). Once *value* is `None`, the *optlen* argument becomes mandatory. This amounts to invoking the `setsockopt()` C function with `optval=NULL` and `optlen=optlen`.

Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is now accepted.

Changed in version 3.6: the setsockopt(level, optname, None, optlen: int) form was introduced.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 shutdown(*how*)

Close down one half of the connection, or both. With *how* set to `SHUT_RD`, no more receives are permitted. With *how* set to `SHUT_WR`, no more sends are permitted. With *how* set to `SHUT_RDWR`, neither further sends nor receives are permitted.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

 share(*process_id*)

Make a copy of a socket and ready it to be shared with a target process. You have to supply that target process by way of *process_id*. The bytes object this produces can then travel to the target process over some form of interprocess communication, and the socket can be rebuilt there through `fromshare()`. After this method runs, closing the socket is safe, since the operating system has already cloned it for the target process.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Added in version 3.3.

Bear in mind there are no `read()` or `write()` methods here; lean on `recv()` and `send()` minus the *flags* argument instead.

Socket objects additionally carry these (read-only) attributes, which mirror the values handed to the `socket` constructor.

 family

The socket family.

 type

The socket type.

 proto

The socket protocol.

[Subject index](INDEX.md) · [Previous](socket-socket-sendto-to-socket-socket-settimeout.md) · [Continue](socket-sockettype-class.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: socket.socket](socket-socket-class.md) · [Owning module, declaration or section: Socket Objects](socket-socket-class.md)
