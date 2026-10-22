# multiprocessing / Process Pools: `multiprocessing.pool.AsyncResult`, `get()`, `wait()`, `ready()`, `successful()`

*class *multiprocessing.pool.AsyncResult

The class of the result that `Pool.apply_async()` and `Pool.map_async()` hand back.

 get([*timeout*])

Hand back the result once it arrives. When *timeout* is not `None` and the result fails to arrive within *timeout* seconds, `multiprocessing.TimeoutError` is raised. When the remote call raised an exception, that exception gets re-raised by `get()`.

 wait([*timeout*])

Wait until the result is on hand or until *timeout* seconds elapse.

 ready()

Report whether the call has finished.

 successful()

Report whether the call finished without raising an exception. Will raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when the result is not ready.

Changed in version 3.7: When the result is not ready, an [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) no longer arises; a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised in its place.

The following example demonstrates the use of a pool:

[Subject index](INDEX.md) · [Previous](pool-task-submission-and-lifecycle.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Process Pools](multiprocessing-pool-pool-class.md) · [Required continuation of the source contract](process-pool-apply-async-map-imap-and-timeout-example.md)
