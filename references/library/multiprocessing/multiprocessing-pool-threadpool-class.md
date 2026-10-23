# multiprocessing - The `multiprocessing.dummy` module

### The `multiprocessing.dummy` module

`multiprocessing.dummy` mirrors the API of `multiprocessing` while being nothing beyond a wrapper over the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module.

Specifically, the `Pool` function that `multiprocessing.dummy` provides hands back an instance of `ThreadPool`, a `Pool` subclass that supports every one of the same method calls but draws on a pool of worker threads rather than worker processes.

 *class *multiprocessing.pool.ThreadPool([*processes*[, *initializer*[, *initargs*]]])

A thread pool object that steers a pool of worker threads to which jobs can be submitted. `ThreadPool` instances match `Pool` instances fully at the interface level, and their resources too have to be managed properly, either by treating the pool as a context manager or by calling `close()` and `terminate()` by hand.

*processes* is how many worker threads to use. When *processes* is `None`, the number that [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count) returns is used.

When *initializer* is not `None`, each worker process calls `initializer(*initargs)` as it starts.

Unlike `Pool`, *maxtasksperchild* and *context* cannot be provided.

Note

A `ThreadPool` carries the same interface as `Pool`, which is built around a pool of processes and predates the arrival of the [`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures) module. Because of that, it inherits a few operations that make no sense for a thread-backed pool, and it has its own type for conveying the status of asynchronous jobs, `AsyncResult`, which no other library understands.

Users should as a rule favor [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor), whose interface is simpler and was designed around threads from the outset, and which hands back [`concurrent.futures.Future`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Future) instances compatible with many other libraries, [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) among them.

[Subject index](INDEX.md) · [Previous](multiprocessing-get-logger-to-multiprocessing-log-to-stderr.md) · [Continue](programming-guidelines.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
