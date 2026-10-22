# socket — Timeouts and the `connect` method

### Timeouts and the `connect` method

The `connect()` operation answers to the timeout setting too, and the usual advice is to call `settimeout()` ahead of `connect()`, or else hand a timeout parameter to `create_connection()`. That said, the system network stack might still raise a connection timeout error all its own, no matter what Python socket timeout you've set.

[Subject index](INDEX.md) · [Previous](notes-on-socket-timeouts.md) · [Continue](timeouts-and-the-accept-method.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md)
