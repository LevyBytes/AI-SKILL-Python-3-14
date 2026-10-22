# Python 3.7.0 alpha 4 / library / socket

[bpo-32331](https://bugs.python.org/issue?@action=redirect&bpo=32331): Adjust socket.settimeout() and socket.setblocking() so socket.type stays untouched. Adjust the socket.socket() constructor to clear any bit flags placed on the socket's type. Only OSes carrying SOCK_NONBLOCK and/or SOCK_CLOEXEC see this change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
