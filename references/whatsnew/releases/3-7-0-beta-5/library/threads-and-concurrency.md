# Python 3.7.0 beta 5 / library / threads and concurrency

[bpo-26819](https://bugs.python.org/issue?@action=redirect&bpo=26819): Resolve a race condition involving `ReadTransport.resume_reading` inside the Windows proactor event loop.

- Corrected a failure in `typing.get_type_hints()` triggered when ClassVar arrived as a string forward reference.

[bpo-33674](https://bugs.python.org/issue?@action=redirect&bpo=33674): Repair a race condition within SSLProtocol.connection_made() of asyncio.sslproto: launch the handshake right away instead of going through call_soon(). Formerly data_received() could fire ahead of the handshake's start, leaving the handshake to hang or fail.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
