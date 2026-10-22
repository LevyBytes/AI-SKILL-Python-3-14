# Python 3.9.0 alpha 2 / tests / files and paths

[bpo-38547](https://bugs.python.org/issue?@action=redirect&bpo=38547): Repair test_pty: when the process happens to be the session leader, closing the master file descriptor triggers a SIGHUP signal, so the tests simply ignore SIGHUP while they run.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
