# multiprocessing: `multiprocessing.pool.Pool`

### Process Pools

You can build a pool of processes that will run tasks handed to it through the `Pool` class.

 *class *multiprocessing.pool.Pool([*processes*[, *initializer*[, *initargs*[, *maxtasksperchild*[, *context*]]]]])

A process pool object that steers a group of worker processes able to receive submitted jobs. It supports async results that carry timeouts and callbacks, and it ships a parallel map implementation.

*processes* is how many worker processes to use. When *processes* is `None`, the number that [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count) returns is used.

When *initializer* is not `None`, each worker process calls `initializer(*initargs)` as it starts.

*maxtasksperchild* is how many tasks a worker process can finish before it exits and a fresh worker process takes its place, so that unused resources can be freed. The default *maxtasksperchild* is `None`, meaning worker processes stay alive for as long as the pool does.

*context* lets you name the context used for launching the worker processes. A pool is typically built through the function `multiprocessing.Pool()` or the `Pool()` method of a context object. Either way *context* gets set appropriately. When `None`, calling this function carries the side effect of setting the current global start method should it not already be set. See the `get_context()` function.

Note that only the process which created the pool ought to call the methods of the pool object.

Warning

`multiprocessing.pool` objects hold internal resources that have to be managed properly (as any other resource does) by treating the pool as a context manager or by calling `close()` and `terminate()` by hand. Skipping this can leave the process hanging at finalization.

Note that it is **not correct** to lean on the garbage collector to destroy the pool, since CPython makes no promise that the pool's finalizer will run (see [`object.__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) for more information).

Changed in version 3.2: Added the *maxtasksperchild* parameter.

Changed in version 3.4: Added the *context* parameter.

Changed in version 3.13: *processes* uses [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count) by default, instead of [`os.cpu_count()`](https://docs.python.org/3.14/library/os.html#os.cpu_count).

Note

Worker processes inside a `Pool` normally stay alive for the whole lifetime of the Pool's work queue. A common pattern seen in other systems (Apache, mod_wsgi, and so on) for freeing resources held by workers is to let a worker in a pool finish only a fixed amount of work before exiting, getting cleaned up, and being replaced by a freshly spawned process. The *maxtasksperchild* argument to the `Pool` brings this capability to the end user.

[Subject index](INDEX.md) · [Previous](cleanup.md) · [Continue](pool-task-submission-and-lifecycle.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
