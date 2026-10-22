# ProcessPoolExecutor: `concurrent.futures.ProcessPoolExecutor`

### ProcessPoolExecutor

An `Executor` subclass, the `ProcessPoolExecutor` class taps a pool of processes for running calls asynchronously. Because `ProcessPoolExecutor` is built on the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) module, it can dodge the [Global Interpreter Lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock); the flip side is that only picklable objects may be passed in for execution and returned out.

Worker subprocesses have to be able to import the `__main__` module. As a result, `ProcessPoolExecutor` won't function within the interactive interpreter.

If a callable handed to a `ProcessPoolExecutor` invokes `Executor` or `Future` methods, a deadlock results.

Keep in mind that the picklability requirements placed on functions and arguments by [`multiprocessing.Process`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process) still hold when you call `submit()` and `map()` on a `ProcessPoolExecutor`. Don't count on a function declared in a REPL, or a lambda, to function here.

 *class *concurrent.futures.ProcessPoolExecutor(*max_workers=None*, *mp_context=None*, *initializer=None*, *initargs=()*, *max_tasks_per_child=None*)

A subclass of `Executor` that runs calls asynchronously across a pool of no more than *max_workers* processes. When *max_workers* is `None` or omitted, it falls back to [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count). Should *max_workers* be `0` or negative, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. Under Windows, *max_workers* may not exceed `61`; otherwise `ValueError` is raised. When *max_workers* is `None`, the value picked tops out at `61`, even where extra processors exist. The *mp_context* argument may be a [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) context or `None`, and it governs how the workers are launched. If *mp_context* is `None` or left out, the default `multiprocessing` context applies. Refer to [Contexts and start methods](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-methods).

The *initializer* parameter is an optional callable invoked as each worker process begins; *initargs* is a tuple of arguments handed to that initializer. If *initializer* throws, every job still pending raises a `BrokenProcessPool`, and so does any further attempt to hand work to the pool.

The optional *max_tasks_per_child* argument caps how many tasks one process may run before it shuts down and is swapped out for a brand-new worker process. The default for *max_tasks_per_child* is `None`, meaning worker processes endure for the pool's whole lifetime. Once a cap is given, the ?spawn? multiprocessing start method becomes the default when no *mp_context* parameter is supplied. This capability cannot be combined with the ?fork? start method.

Note

There are reported bugs tied to the *max_tasks_per_child* feature that, under certain conditions, leave the `ProcessPoolExecutor` hanging. Track how it gets resolved over at [gh-115634](https://github.com/python/cpython/issues/115634).

Changed in version 3.3: Should a worker process die abruptly, a `BrokenProcessPool` error now gets raised. Beforehand the behaviour wasn't defined, and actions on the executor or its futures tended to hang or deadlock.

Changed in version 3.7: Introduced the *mp_context* argument so that users can govern the start_method applied to the pool's worker processes.

Added the *initializer* and *initargs* arguments.

Changed in version 3.11: Introduced the *max_tasks_per_child* argument so that users can govern how long the pool's workers persist.

Changed in version 3.12: Under POSIX, when your application runs several threads and the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) context relies on the `"fork"` start method: the [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) function invoked internally to spawn workers might emit a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Supply a *mp_context* set up with a different start method. Consult the `os.fork()` documentation for a fuller account.

Changed in version 3.13: *max_workers* uses [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count) by default, instead of [`os.cpu_count()`](https://docs.python.org/3.14/library/os.html#os.cpu_count).

Changed in version 3.14: The default process start method (consult [Contexts and start methods](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-methods)) no longer defaults to *fork*. Should you need the *fork* start method with `ProcessPoolExecutor`, you have to pass `mp_context=multiprocessing.get_context("fork")` yourself.

[Subject index](INDEX.md) · [Previous](concurrent-futures-interpreterpoolexecutor-class.md) · [Continue](terminate-and-kill-pool-workers.md)
