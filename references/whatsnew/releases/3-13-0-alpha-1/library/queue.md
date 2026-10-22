# Python 3.13.0 alpha 1 / library / queue

[gh-107219](https://github.com/python/cpython/issues/107219): Resolved a race condition inside `concurrent.futures`. Whenever a process in the process pool was killed abruptly (while its future was running or pending), close the write end of the connection. If the call queue is stuck sending bytes to a worker process, closing that write end interrupts the send, allowing the queue to be closed. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
