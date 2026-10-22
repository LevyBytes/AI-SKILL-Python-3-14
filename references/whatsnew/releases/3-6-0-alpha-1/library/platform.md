# Python 3.6.0 alpha 1 / library / platform

[bpo-23972](https://bugs.python.org/issue?@action=redirect&bpo=23972): The asyncio datagram create method is updated so the reuseport and reuseaddr socket options may be configured before the socket is bound. As with the existing asyncio create_server method, for datagram sockets the reuseaddr option defaults to True when the O/S is "posix" (the Cygwin platform being the exception). Chris Laws contributed the patch.

[bpo-26513](https://bugs.python.org/issue?@action=redirect&bpo=26513): Corrected how the platform module detects Windows Server.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
