# socket - Socket families

`HV_GUID_ZERO`

  - `HV_GUID_BROADCAST`

  - `HV_GUID_WILDCARD` - Binds on itself and takes connections from every partition.

  - `HV_GUID_CHILDREN` - Binds on itself and takes connections from child partitions.

  - `HV_GUID_LOOPBACK` - Acts as a target pointing at itself.

  - `HV_GUID_PARENT` - As a bind, it takes a connection from the parent partition; as an address target, it connects out to the parent partition.

The `service_id` gives the service identifier of the service that was registered.

Added in version 3.12.

Putting a hostname in the *host* portion of an IPv4/v6 socket address can make the program behave nondeterministically, because Python takes the first address that DNS resolution returns. The socket address resolves into one actual IPv4/v6 address or another, depending on what DNS resolution yields and/or how the host is configured. To get deterministic behavior, put a numeric address in the *host* portion.

Exceptions are raised on all errors. The usual exceptions for invalid argument types and for out-of-memory conditions may be raised. Errors tied to socket or address semantics raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) or one of its subclasses.

You get non-blocking mode through `setblocking()`. A timeout-based generalization of it is available through `settimeout()`.

[Subject index](INDEX.md) · [Previous](packet-socket-address-type-contract.md) · [Continue](module-contents.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Socket families](socket-families-section-introduction-and-initial-examples.md)
