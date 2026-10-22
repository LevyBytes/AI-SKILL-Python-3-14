# socket: `socket.if_nameindex()`, `socket.if_nametoindex()`, `socket.if_indextoname()`, `socket.send_fds()`

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `socket.sethostname` with argument `name`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not Android.

Added in version 3.3.

 socket.if_nameindex()

Returns a list of tuples describing the network interfaces (index int, name string). An [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised should the underlying system call fail.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows, not WASI.

Added in version 3.3.

Changed in version 3.8: Windows support was added.

Note

Under Windows, a single network interface can carry distinct names depending on the context in which it is referenced (every name shown here is illustrative):

- UUID: `{FB605B73-AAC2-49A6-9A2F-25416AEA0573}`

- name: `ethernet_32770`

- friendly name: `vEthernet (nat)`

- description: `Hyper-V Virtual Ethernet Adapter`

It is the second variety of name that this function pulls from the list — here that would be `ethernet_32770`.

 socket.if_nametoindex(*if_name*)

Given an interface name, returns the matching network interface index number. An [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised when no interface carries the supplied name.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows, not WASI.

Added in version 3.3.

Changed in version 3.8: Windows support was added.

See also

An “Interface name” refers to a name of the kind described under `if_nameindex()`.

 socket.if_indextoname(*if_index*)

Given an interface index number, returns the matching network interface name. An [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised when no interface carries the supplied index.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows, not WASI.

Added in version 3.3.

Changed in version 3.8: Windows support was added.

See also

An “Interface name” refers to a name of the kind described under `if_nameindex()`.

 socket.send_fds(*sock*, *buffers*, *fds*[, *flags*[, *address*]])

Transmit the list of file descriptors *fds* across an `AF_UNIX` socket *sock*. Here *fds* is supplied as a sequence of file descriptors. See `sendmsg()` for how the remaining parameters are documented.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Unix platforms supporting `sendmsg()` and `SCM_RIGHTS` mechanism.

Added in version 3.9.

[Subject index](INDEX.md) · [Continue](socket-recv-fds.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Other functions](socket-close-to-socket-gethostname.md) · [Owning module, declaration or section: socket.sethostname](socket-inet-pton-to-socket-sethostname.md) · [Preceding source contract and version conditions](socket-inet-pton-to-socket-sethostname.md)
