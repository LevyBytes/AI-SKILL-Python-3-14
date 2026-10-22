# Python 3.6.0 alpha 1 / library / socket

[bpo-26685](https://bugs.python.org/issue?@action=redirect&bpo=26685): An OSError is now raised when closing a socket fails.

[bpo-25951](https://bugs.python.org/issue?@action=redirect&bpo=25951): SSLSocket.sendall() now hands back None, matching what is explicitly documented for ordinary socket objects. Aviv Palivoda contributed the patch.

[bpo-26227](https://bugs.python.org/issue?@action=redirect&bpo=26227): Under Windows, the hostname returned by the socket module's getnameinfo(), gethostbyaddr() and gethostbyname_ex() functions is now decoded using the ANSI code page in place of UTF-8.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
