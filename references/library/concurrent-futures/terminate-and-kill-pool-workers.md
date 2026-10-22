# ProcessPoolExecutor: `terminate_workers()`, `kill_workers()`

terminate_workers()

Try to terminate each live worker process at once by invoking [`Process.terminate`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process.terminate) on every one of them. Behind the scenes it additionally invokes `Executor.shutdown()` so that the rest of the executor's associated resources are released.

Once this method has run, the caller ought to stop handing tasks to the executor.

Added in version 3.14.

 kill_workers()

Try to kill each live worker process at once by invoking [`Process.kill`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process.kill) on every one of them. Behind the scenes it additionally invokes `Executor.shutdown()` so that the rest of the executor's associated resources are released.

Once this method has run, the caller ought to stop handing tasks to the executor.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](concurrent-futures-processpoolexecutor-class.md) · [Continue](processpoolexecutor-example.md) · [Owning module, declaration or section: concurrent.futures.ProcessPoolExecutor](concurrent-futures-processpoolexecutor-class.md) · [Owning module, declaration or section: ProcessPoolExecutor](concurrent-futures-processpoolexecutor-class.md)
