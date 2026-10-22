# queue — Queue Objects

### Queue Objects

Queue objects (`Queue`, `LifoQueue`, or `PriorityQueue`) expose the public methods laid out below.

 Queue.qsize()

Hand back the queue's approximate size. Mind that qsize() > 0 is no promise that a later get() won't block, nor does qsize() < maxsize promise that put() won't block.

 Queue.empty()

Hand back `True` should the queue be empty, `False` otherwise. Should empty() hand back `True` it's no promise that a later call to put() won't block. In the same way, should empty() hand back `False` it's no promise that a later call to get() won't block.

 Queue.full()

Hand back `True` should the queue be full, `False` otherwise. Should full() hand back `True` it's no promise that a later call to get() won't block. In the same way, should full() hand back `False` it's no promise that a later call to put() won't block.

 Queue.put(*item*, *block=True*, *timeout=None*)

Put *item* into the queue. Should optional args *block* be true and *timeout* be `None` (the default), block as needed until a free slot opens up. Should *timeout* be a positive number, it blocks for at most *timeout* seconds and raises the `Full` exception if no free slot opened up within that span. Otherwise (*block* is false), drop an item on the queue if a free slot is at once available, else raise the `Full` exception (*timeout* is then disregarded).

Raises `ShutDown` should the queue have been shut down.

 Queue.put_nowait(*item*)

Equivalent to `put(item, block=False)`.

 Queue.get(*block=True*, *timeout=None*)

Remove and hand back an item from the queue. Should optional args *block* be true and *timeout* be `None` (the default), block as needed until an item opens up. Should *timeout* be a positive number, it blocks for at most *timeout* seconds and raises the `Empty` exception if no item opened up within that span. Otherwise (*block* is false), hand back an item if one is at once available, else raise the `Empty` exception (*timeout* is then disregarded).

On POSIX systems before 3.0, and across every version on Windows, should *block* be true and *timeout* be `None`, this operation drops into an uninterruptible wait on an underlying lock. The upshot is that no exceptions can fire, and in particular a SIGINT won't set off a [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt).

Raises `ShutDown` should the queue have been shut down and be empty, or should the queue have been shut down immediately.

 Queue.get_nowait()

Equivalent to `get(False)`.

A pair of methods exist to help track whether enqueued tasks have been fully processed by daemon consumer threads.

 Queue.task_done()

Signal that a formerly enqueued task has finished. Used by queue consumer threads. For every `get()` used to pull a task, a later call to `task_done()` informs the queue that the processing on the task has finished.

Should a `join()` be blocking at the moment, it resumes once every item has been processed (meaning a `task_done()` call arrived for each item that had been `put()` into the queue).

Raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) should it be called more times than there were items dropped into the queue.

 Queue.join()

Blocks until every item in the queue has been gotten and processed.

The count of unfinished tasks climbs whenever an item joins the queue. That count falls whenever a consumer thread calls `task_done()` to signal the item was pulled and all work on it has finished. Once the count of unfinished tasks falls to zero, `join()` unblocks.

[Subject index](INDEX.md) · [Previous](queue-empty-to-queue-shutdown.md) · [Continue](waiting-for-task-completion.md) · [Owning module, declaration or section: queue](queue-queue-class.md)
