# Python 3.5.4 release candidate 1 / library / imaplib

[bpo-30329](https://bugs.python.org/issue?@action=redirect&bpo=30329): imaplib along with poplib now trap the Windows socket WSAEINVAL error (code 10022) during shutdown(SHUT_RDWR): An invalid operation was attempted. That error shows up now and then over SSL connections.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
