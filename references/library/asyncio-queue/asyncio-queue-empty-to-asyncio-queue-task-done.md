# Queue: `empty()`, `full()`, `get()`, `get_nowait()`, `join()`, `put()`, `put_nowait()`, `qsize()`, `shutdown()`, `task_done()`

maxsize

Number of items allowed in the queue.

 empty()

Return `True` if the queue is empty, `False` otherwise.

 full()

Return `True` if there are `maxsize` items in the queue.

When the queue started out with `maxsize=0` (the default), `full()` will not ever come back as `True`.

 *async *get()

Takes an item off the queue and hands it back. Where the queue holds nothing, it waits for an item to show up.

Throws `QueueShutDown` when the queue is both shut down and empty, or whenever it was shut down immediately.

 get_nowait()

Return an item if one is immediately available, else raise `QueueEmpty`.

 *async *join()

Block until all items in the queue have been received and processed.

Each item added to the queue bumps the tally of unfinished tasks upward. That tally falls back down every time a consumer coroutine calls `task_done()` to signal it pulled the item out and wrapped up all its work. The moment the unfinished-task tally hits zero, `join()` stops blocking.

 *async *put(*item*)

Places an item onto the queue. Should the queue already be full, it holds off until a slot opens up before inserting the item.

Raises `QueueShutDown` if the queue has been shut down.

 put_nowait(*item*)

Put an item into the queue without blocking.

If no free slot is immediately available, raise `QueueFull`.

 qsize()

Return the number of items in the queue.

 shutdown(*immediate=False*)

Put a `Queue` instance into a shutdown mode.

No further growth is possible for the queue. Any later `put()` call raises `QueueShutDown`. Callers of `put()` that are blocked right now get released and will raise `QueueShutDown` within the task that had been waiting.

With *immediate* left false (the default), you can drain the queue the usual way, using `get()` calls to pull out tasks that were already loaded in.

Then, provided `task_done()` runs for every task still left, a waiting `join()` is released in the ordinary fashion.

After the queue empties out, any subsequent `get()` call raises `QueueShutDown`.

Set *immediate* to true and the queue is killed off at once. It is drained until nothing remains, and the unfinished-task count drops by however many tasks were drained out. Where unfinished tasks reaches zero, `join()` callers are released. On top of that, blocked `get()` callers are freed and will raise `QueueShutDown`, since by then the queue holds nothing.

Tread carefully when pairing `join()` with *immediate* set to true. Doing so releases the join even if none of the tasks have actually been worked on, breaking the invariant a queue join normally upholds.

Added in version 3.13.

 task_done()

Indicate that a formerly enqueued work item is complete.

Queue consumers rely on this. Every `get()` that fetches a work item should be followed by a `task_done()` call, which notifies the queue that work on that item has wrapped up.

Where a `join()` is blocking at the moment, it picks back up once every item has been handled — that is, once a `task_done()` call has landed for each item that was ever `put()` onto the queue.

Throws [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when it is invoked more often than there were items put onto the queue.

[Subject index](INDEX.md) · [Previous](asyncio-queue-class.md) · [Continue](asyncio-priorityqueue-class.md) · [Owning module, declaration or section: asyncio.Queue](asyncio-queue-class.md) · [Owning module, declaration or section: Queue](asyncio-queue-class.md)
