# Python 3.7.0 beta 5 / library / asyncio buffered protocol switching

[bpo-33654](https://bugs.python.org/issue?@action=redirect&bpo=33654): Repair transport.set_protocol() so it permits switching between asyncio.Protocol and asyncio.BufferedProtocol. Repair loop.start_tls() so it operates with asyncio.BufferedProtocols.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
