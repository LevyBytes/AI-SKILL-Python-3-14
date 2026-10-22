# multiprocessing / Pipes and Queues: `multiprocessing.Queue`, `qsize()`, `empty()`, `full()`, `put()`, `put_nowait()`, `get()`, `get_nowait()`, `close()`, `join_thread()`, `cancel_join_thread()`

*class *multiprocessing.Queue([*maxsize*])

Gives back a process-shared queue built on top of a pipe plus a handful of locks/semaphores. The first time a process puts an item on the queue, a feeder thread spins up to move objects from a buffer into the pipe.

Building an object of this kind can fix the global start method in place. Consult Global start method for the fuller picture.

The familiar [`queue.Empty`](https://docs.python.org/3.14/library/queue.html#queue.Empty) and [`queue.Full`](https://docs.python.org/3.14/library/queue.html#queue.Full) exceptions out of the standard library's [`queue`](https://docs.python.org/3.14/library/queue.html#module-queue) module get raised to flag timeouts.

`Queue` provides every method of [`queue.Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) apart from [`task_done()`](https://docs.python.org/3.14/library/queue.html#queue.Queue.task_done), [`join()`](https://docs.python.org/3.14/library/queue.html#queue.Queue.join), and [`shutdown()`](https://docs.python.org/3.14/library/queue.html#queue.Queue.shutdown).

 qsize()

Give back the queue's approximate size. Owing to multithreading/multiprocessing semantics, this figure is not dependable.

Be aware this may raise [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) on platforms such as macOS where `sem_getvalue()` is unavailable.

 empty()

Give back `True` when the queue holds nothing, `False` otherwise. Owing to multithreading/multiprocessing semantics, this is not dependable.

May raise an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) on closed queues. (not guaranteed)

 full()

Give back `True` when the queue is full, `False` otherwise. Owing to multithreading/multiprocessing semantics, this is not dependable.

 put(*obj*[, *block*[, *timeout*]])

Place obj onto the queue. With the optional *block* argument set to `True` (the default) and *timeout* set to `None` (the default), block as needed until a free slot opens. With *timeout* a positive number, it blocks for at most *timeout* seconds and raises the [`queue.Full`](https://docs.python.org/3.14/library/queue.html#queue.Full) exception if no slot freed up in time. In the other case (*block* is `False`), it puts an item on the queue if a slot is free right away, otherwise raising the `queue.Full` exception (with *timeout* ignored then).

Changed in version 3.8: For a closed queue, an [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) no longer arises; a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised in its place.

 put_nowait(*obj*)

Equivalent to `put(obj, False)`.

 get([*block*[, *timeout*]])

Take an item off the queue and give it back. With the optional *block* argument set to `True` (the default) and *timeout* set to `None` (the default), block as needed until an item becomes available. With *timeout* a positive number, it blocks for at most *timeout* seconds and raises the [`queue.Empty`](https://docs.python.org/3.14/library/queue.html#queue.Empty) exception if nothing became available in time. In the other case (block is `False`), it returns an item if one is free right away, otherwise raising the `queue.Empty` exception (with *timeout* ignored then).

Changed in version 3.8: For a closed queue, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) no longer arises; a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised in its place.

 get_nowait()

Equivalent to `get(False)`.

`multiprocessing.Queue` carries a few extra methods beyond those of [`queue.Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue). Most code has no need for these methods:

 close()

Close the queue: release internal resources.

Once a queue is closed, it must not be touched again. As an example, the `get()`, `put()` and `empty()` methods can no longer be called.

The background thread exits as soon as it has flushed every buffered item into the pipe. This happens automatically when the queue gets garbage collected.

 join_thread()

Join the background thread. Calling this is only valid after `close()` has run. It blocks until the background thread finishes, making sure every byte in the buffer has reached the pipe.

By default, a process that did not create the queue will, on exit, try to join the queue's background thread. A process can call `cancel_join_thread()` so that `join_thread()` becomes a no-op.

 cancel_join_thread()

Keep `join_thread()` from blocking. Specifically, this stops the background thread from being joined automatically when the process exits — see `join_thread()`.

A more descriptive name for this method might be `allow_exit_without_flush()`. It is apt to discard enqueued data, and you almost surely will not need it. It exists solely for cases where you want the current process to quit at once without pausing to flush enqueued data into the underlying pipe, and you are willing to lose data.

Note

The functionality of this class depends on the host operating system having a working shared semaphore implementation. Lacking one, the class's functionality is switched off, and any attempt to instantiate a `Queue` raises an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError). For more information see [bpo-3770](https://bugs.python.org/issue?@action=redirect&bpo=3770). The same applies to every specialized queue type listed below.

[Subject index](INDEX.md) · [Previous](multiprocessing-pipe.md) · [Continue](simple-process-queue.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Pipes and Queues](multiprocessing-pipe.md)
