# multiprocessing / Pipes and Queues: `multiprocessing.SimpleQueue`, `close()`, `empty()`, `get()`, `put()`

*class *multiprocessing.SimpleQueue

A pared-down `Queue` type, almost equivalent to a locked `Pipe`.

Building an object of this kind can fix the global start method in place. Consult Global start method for the fuller picture.

 close()

Close the queue: release internal resources.

Once a queue is closed, it must not be touched again. As an example, the `get()`, `put()` and `empty()` methods can no longer be called.

Added in version 3.9.

 empty()

Give back `True` when the queue holds nothing, `False` otherwise.

Always raises an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) if the SimpleQueue is closed.

 get()

Take an item off the queue and give it back.

 put(*item*)

Place *item* onto the queue.

[Subject index](INDEX.md) · [Previous](process-queue-contract-and-feeder-lifecycle.md) · [Continue](joinable-process-queue.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Pipes and Queues](multiprocessing-pipe.md)
