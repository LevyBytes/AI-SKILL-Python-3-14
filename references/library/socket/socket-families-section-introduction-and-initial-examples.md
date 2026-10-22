# socket — Socket families — Section introduction and initial examples

### Socket families

Which socket families this module supports hinges on the system together with the build options.

A particular socket object's required address format is chosen for you, derived from the address family that was named when the object was created. The various socket addresses look like this:

- When an `AF_UNIX` socket is bound to a file system node, its address shows up as a string encoded with the file system encoding and the `'surrogateescape'` error handler (see [**PEP 383**](https://peps.python.org/pep-0383/)). An address living in Linux's abstract namespace comes back as a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) whose first byte is null; keep in mind that sockets here can talk to ordinary file system sockets, so software meant for Linux may have to handle both address kinds. Either kind of address may be passed in as an argument using a string or a bytes-like object.

Changed in version 3.3: Up to this point, `AF_UNIX` socket paths had been taken to be UTF-8 encoded.

Changed in version 3.5: A writable [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is accepted as of this release.

- The `AF_INET` address family takes a pair `(host, port)`, in which *host* is a string holding either a hostname in internet domain notation such as `'daring.cwi.nl'` or an IPv4 address such as `'100.50.200.5'`, and *port* is an integer.

  - With IPv4 addresses, two extra forms may stand in for a host address: `''` stands for `INADDR_ANY`, which binds to every interface, and the string `'<broadcast>'` stands for `INADDR_BROADCAST`. Since this does not carry over to IPv6, steer clear of these forms if your Python programs are meant to support IPv6.

- The `AF_INET6` address family takes a four-tuple `(host, port, flowinfo, scope_id)`, where *flowinfo* and *scope_id* correspond to the `sin6_flowinfo` and `sin6_scope_id` members of `struct sockaddr_in6` in C. Purely for backward compatibility, `socket` module methods let you leave out *flowinfo* and *scope_id*. Be aware, though, that dropping *scope_id* may make working with scoped IPv6 addresses troublesome.

Changed in version 3.7: With multicast addresses (where *scope_id* matters), *address* must not include a `%scope_id` (or `zone id`) segment. Since that detail is redundant, leaving it off is safe and is the recommended choice.

- `AF_NETLINK` sockets are represented as pairs `(pid, groups)`.

- There is Linux-only TIPC support by way of the `AF_TIPC` address family. As an open protocol that is not IP-based, TIPC was built for networking within clustered computer setups. A tuple represents an address, and which fields it has depends on the address type. In its general form the tuple is `(addr_type, v1, v2, v3 [, scope])`, where:

  - *addr_type* is one of `TIPC_ADDR_NAMESEQ`, `TIPC_ADDR_NAME`, or `TIPC_ADDR_ID`.

  - *scope* is one of `TIPC_ZONE_SCOPE`, `TIPC_CLUSTER_SCOPE`, and `TIPC_NODE_SCOPE`.

  - When *addr_type* is `TIPC_ADDR_NAME`, *v1* holds the server type, *v2* holds the port identifier, and *v3* should be 0.

When *addr_type* is `TIPC_ADDR_NAMESEQ`, *v1* holds the server type, *v2* holds the lower port number, and *v3* holds the upper port number.

When *addr_type* is `TIPC_ADDR_ID`, *v1* holds the node, *v2* holds the reference, and *v3* should be set to 0.

- The `AF_CAN` address family takes a tuple `(interface, )`, in which *interface* is a string naming a network interface such as `'can0'`. Passing the network interface name `''` lets you receive packets from every network interface in this family.

  - The `CAN_ISOTP` protocol calls for a tuple `(interface, rx_addr, tx_addr)`, in which the two extra parameters are each an unsigned long integer standing for a CAN identifier (standard or extended).

  - The `CAN_J1939` protocol calls for a tuple `(interface, name, pgn, addr)`, in which the extra parameters are a 64-bit unsigned integer for the ECU name, a 32-bit unsigned integer for the Parameter Group Number (PGN), and an 8-bit integer for the address.

- For the `SYSPROTO_CONTROL` protocol of the `PF_SYSTEM` family you use either a string or a tuple `(id, unit)`. The string names a kernel control that has a dynamically assigned ID. The tuple comes in handy when the ID and unit number of the kernel control are known, or when a registered ID is being used.

Added in version 3.3.

- `AF_BLUETOOTH` supports the following protocols and address formats:

  - `BTPROTO_L2CAP` accepts a tuple `(bdaddr, psm[, cid[, bdaddr_type]])` where:

    - `bdaddr` is a string holding the Bluetooth address.

    -

[Subject index](INDEX.md) · [Previous](socket-low-level-networking-interface.md) · [Continue](bluetooth-protocol-service-multiplexer.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md)
