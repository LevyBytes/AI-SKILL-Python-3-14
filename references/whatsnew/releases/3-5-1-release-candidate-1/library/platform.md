# Python 3.5.1 release candidate 1 / library / platform

[bpo-23972](https://bugs.python.org/issue?@action=redirect&bpo=23972): The asyncio datagram create method now lets the reuseport and reuseaddr socket options be configured before the socket is bound. Echoing the existing asyncio create_server method, for datagram sockets the reuseaddr option defaults to True when the O/S is "posix" (other than on the Cygwin platform). Chris Laws wrote the patch.

[bpo-19143](https://bugs.python.org/issue?@action=redirect&bpo=19143): To sidestep compatibility shims, the platform module now obtains the Windows version straight from kernel32.dll.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
