# Python 3.10.0 beta 1 / tests / socket

[bpo-43842](https://bugs.python.org/issue?@action=redirect&bpo=43842): Resolved a race condition affecting the SMTP test in test_logging. A file descriptor (socket) is no longer closed from a separate thread while asyncore.loop() is still polling it. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
