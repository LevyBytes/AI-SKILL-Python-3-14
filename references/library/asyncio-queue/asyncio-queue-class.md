# Queue: `asyncio.Queue`

### Queue

 *class *asyncio.Queue(*maxsize=0*)

A first in, first out (FIFO) queue.

Should *maxsize* be zero or negative, the queue has no size limit at all. When it is an integer above `0`, `await put()` will block once the queue fills to *maxsize*, staying blocked until `get()` takes an item out.

In contrast to the standard library's threading [`queue`](https://docs.python.org/3.14/library/queue.html#module-queue), this queue's size is always knowable and comes back from a call to the `qsize()` method.

Changed in version 3.10: Removed the *loop* parameter.

This class is [not thread safe](https://docs.python.org/3.14/library/asyncio-dev.html#asyncio-multithreading).

[Subject index](INDEX.md) · [Previous](queues.md) · [Continue](asyncio-queue-empty-to-asyncio-queue-task-done.md)
