# Python 3.6.1 release candidate 1 / tests / socket

[bpo-28683](https://bugs.python.org/issue?@action=redirect&bpo=28683): Repair the tests that call bind() on a unix socket, which raise PermissionError for a non-root user on Android.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
