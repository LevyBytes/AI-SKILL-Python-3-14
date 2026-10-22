# Python 3.7.0 alpha 1 / library / imaplib

[bpo-30329](https://bugs.python.org/issue?@action=redirect&bpo=30329): On shutdown(SHUT_RDWR), imaplib and poplib now trap the Windows socket WSAEINVAL error (code 10022): An invalid operation was attempted. Such an error shows up occasionally with SSL connections.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
