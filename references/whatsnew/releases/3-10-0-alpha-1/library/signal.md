# Python 3.10.0 alpha 1 / library / signal

[bpo-41675](https://bugs.python.org/issue?@action=redirect&bpo=41675): Where the system offers it, [`signal.siginterrupt()`](https://docs.python.org/3.14/library/signal.html#signal.siginterrupt) is now built on `sigaction()` in place of the deprecated `siginterrupt()`. Pablo Galindo contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
