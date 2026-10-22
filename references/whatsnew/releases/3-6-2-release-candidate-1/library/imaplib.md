# Python 3.6.2 release candidate 1 / library / imaplib

[bpo-30329](https://bugs.python.org/issue?@action=redirect&bpo=30329): On shutdown(SHUT_RDWR), imaplib and poplib now trap the Windows socket WSAEINVAL error (code 10022): An invalid operation was attempted. SSL connections occasionally trigger this error.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
