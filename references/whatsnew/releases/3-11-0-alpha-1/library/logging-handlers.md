# Python 3.11.0 alpha 1 / library / logging handlers

[bpo-42378](https://bugs.python.org/issue?@action=redirect&bpo=42378): Resolves the problem of the log file getting clobbered whenever [`logging.FileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.FileHandler) runs inside [`atexit`](https://docs.python.org/3.14/library/atexit.html#module-atexit) with *filemode* equal to `'w'`. Be aware this means the *atexit* message goes unlogged should the log stream already be closed because logging has shut down.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
