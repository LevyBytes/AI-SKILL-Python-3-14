# Python 3.6.6 release candidate 1 / library / fixed race within sslprotocol connection made asyncio sslproto kicking off handshake right

[bpo-33674](https://bugs.python.org/issue?@action=redirect&bpo=33674): Fixed a race within SSLProtocol.connection_made() in asyncio.sslproto by kicking off the handshake right away rather than via call_soon(). Formerly data_received() might fire ahead of the handshake beginning, which left the handshake stuck or broken.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
