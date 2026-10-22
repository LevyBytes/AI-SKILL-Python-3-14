# Python 3.11.0 alpha 7 / library / supply missing terminating nul within length sockaddr un effect potentially

[bpo-44493](https://bugs.python.org/issue?@action=redirect&bpo=44493): Supply the missing terminating NUL within the length of sockaddr_un

The effect was potentially visible when non-abstract AF_UNIX datagram sockets talked to processes built in another programming language.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
