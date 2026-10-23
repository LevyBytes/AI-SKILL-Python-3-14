# queue - Terminating queues

### Terminating queues

Once they're no longer wanted, `Queue` objects can be wound down to empty or killed at once via a hard shutdown.

 Queue.shutdown(*immediate=False*)

Drop a `Queue` instance into a shutdown mode.

The queue can grow no further. Later calls to `put()` raise `ShutDown`. Callers of `put()` blocked at the moment get unblocked and will raise `ShutDown` in the formerly blocked thread.

Should *immediate* be false (the default), the queue can be wound down normally with `get()` calls that pull out tasks already loaded.

And should `task_done()` be called for each leftover task, a pending `join()` gets unblocked normally.

Once the queue is empty, later calls to `get()` will raise `ShutDown`.

Should *immediate* be true, the queue is killed at once. The queue gets drained until completely empty and the count of unfinished tasks is cut by the number of tasks drained. Should unfinished tasks be zero, callers of `join()` get unblocked. Blocked callers of `get()` likewise get unblocked and will raise `ShutDown` because the queue is empty.

Take care when pairing `join()` with *immediate* set to true. Doing so unblocks the join even though no work has been done on the tasks, breaking the usual invariant for joining a queue.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](waiting-for-task-completion.md) · [Continue](simplequeue-qsize-to-simplequeue-get-nowait.md) · [Owning module, declaration or section: queue](queue-queue-class.md)
