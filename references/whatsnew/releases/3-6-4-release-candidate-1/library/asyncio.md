# Python 3.6.4 release candidate 1 / library / asyncio

[bpo-31970](https://bugs.python.org/issue?@action=redirect&bpo=31970): Lower the runtime cost incurred by asyncio's debug mode.

[bpo-31632](https://bugs.python.org/issue?@action=redirect&bpo=31632): Corrected the set_protocol() method belonging to class _SSLProtocolTransport within the asyncio module. The method had been updating an incorrect reference to the protocol.

[bpo-32015](https://bugs.python.org/issue?@action=redirect&bpo=32015): Repaired the asyncio looping that happened when the socket reconnected while an async read/write to or from that socket was pending.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
