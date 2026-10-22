# Python 3.7.0 beta 1 / library / queue

[bpo-32574](https://bugs.python.org/issue?@action=redirect&bpo=32574): Correct a memory leak within asyncio.Queue: when the queue has a bounded size and is full, cancelling queue.put() can produce a memory leak. Patch by: Jos?? Melero.

[bpo-14976](https://bugs.python.org/issue?@action=redirect&bpo=14976): Introduce a queue.SimpleQueue class — an unbounded FIFO queue whose put() has a reentrant C implementation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
