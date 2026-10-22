# multiprocessing.pool.Pool: `apply()`, `apply_async()`, `map()`, `map_async()`, `imap()`, `imap_unordered()`, `starmap()`, `starmap_async()`, `close()`, `terminate()`, `join()`

apply(*func*[, *args*[, *kwds*]])

Call *func* using positional *args* together with keyword *kwds*. It blocks while waiting for the result. Since blocking happens, `apply_async()` is the better fit for parallel work. On top of that, *func* runs in only one of the pool's workers.

 apply_async(*func*[, *args*[, *kwds*[, *callback*[, *error_callback*]]]])

A variant of the `apply()` method that hands back an `AsyncResult` object.

When *callback* is given, it should be a callable accepting one argument. Once the result is ready, *callback* gets applied to it — unless the call failed, in which case *error_callback* gets applied instead.

When *error_callback* is given, it should be a callable accepting one argument. Should the target function fail, *error_callback* gets called with the exception instance.

Callbacks ought to finish at once, or else the thread that handles the results will end up blocked.

 map(*func*, *iterable*[, *chunksize*])

A parallel counterpart of the [`map()`](https://docs.python.org/3.14/library/functions.html#map) built-in function (though it supports only one *iterable* argument; for several iterables see `starmap()`). It blocks until the result is ready.

This method slices the iterable into a set of chunks that it hands to the process pool as separate tasks. You can name the (approximate) size of these chunks by setting *chunksize* to a positive integer.

Note that this can drive up memory usage for very long iterables. Think about using `imap()` or `imap_unordered()` with an explicit *chunksize* option for better efficiency.

 map_async(*func*, *iterable*[, *chunksize*[, *callback*[, *error_callback*]]])

A variant of the `map()` method that hands back an `AsyncResult` object.

When *callback* is given, it should be a callable accepting one argument. Once the result is ready, *callback* gets applied to it — unless the call failed, in which case *error_callback* gets applied instead.

When *error_callback* is given, it should be a callable accepting one argument. Should the target function fail, *error_callback* gets called with the exception instance.

Callbacks ought to finish at once, or else the thread that handles the results will end up blocked.

 imap(*func*, *iterable*[, *chunksize*])

A lazier version of `map()`.

The *chunksize* argument matches the one the `map()` method uses. For very long iterables, a large *chunksize* value can make the job finish **much** quicker than the default value of `1`.

Also, when *chunksize* is `1`, the `next()` method on the iterator that `imap()` returns takes an optional *timeout* parameter: `next(timeout)` raises `multiprocessing.TimeoutError` should the result fail to arrive within *timeout* seconds.

 imap_unordered(*func*, *iterable*[, *chunksize*])

The same as `imap()`, except the ordering of results from the iterator returned should be treated as arbitrary. (The order is guaranteed to be “correct” only when there is just one worker process.)

 starmap(*func*, *iterable*[, *chunksize*])

Like `map()`, except the elements of the *iterable* are expected to be iterables that get unpacked into arguments.

So an *iterable* of `[(1,2), (3, 4)]` yields `[func(1,2), func(3,4)]`.

Added in version 3.3.

 starmap_async(*func*, *iterable*[, *chunksize*[, *callback*[, *error_callback*]]])

A blend of `starmap()` and `map_async()` that walks an *iterable* of iterables and calls *func* with each one unpacked. Hands back a result object.

Added in version 3.3.

 close()

Bars any further tasks from reaching the pool. Once every task is finished, the worker processes will exit.

 terminate()

Halts the worker processes at once without finishing outstanding work. When the pool object is garbage collected, `terminate()` runs right away.

 join()

Wait for the worker processes to exit. You must call `close()` or `terminate()` ahead of using `join()`.

Changed in version 3.3: The context management protocol is now supported by Pool objects – see [Context Manager Types](https://docs.python.org/3.14/library/stdtypes.html#typecontextmanager). [`__enter__()`](https://docs.python.org/3.14/library/stdtypes.html#contextmanager.__enter__) returns the pool object, while [`__exit__()`](https://docs.python.org/3.14/library/stdtypes.html#contextmanager.__exit__) calls `terminate()`.

[Subject index](INDEX.md) · [Previous](multiprocessing-pool-pool-class.md) · [Continue](pool-async-result-contract.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: multiprocessing.pool.Pool](multiprocessing-pool-pool-class.md) · [Owning module, declaration or section: Process Pools](multiprocessing-pool-pool-class.md)
