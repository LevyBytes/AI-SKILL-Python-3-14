# Python 3.5.0 alpha 4 / core and builtins / threads and concurrency

[bpo-23309](https://bugs.python.org/issue?@action=redirect&bpo=23309): Sidestep a shutdown deadlock that occurs when a daemon thread is aborted while holding a lock on a buffered I/O object, and the main thread then attempts to operate on that same I/O object (often stdout or stderr). Instead, a fatal error gets emitted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
