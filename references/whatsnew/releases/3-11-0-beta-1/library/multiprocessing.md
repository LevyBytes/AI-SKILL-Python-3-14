# Python 3.11.0 beta 1 / library / multiprocessing

[bpo-47029](https://bugs.python.org/issue?@action=redirect&bpo=47029): Make sure the read end of the pipe behind [`multiprocessing.Queue`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Queue) is closed only *after* buffered data has finished being written to the pipe's write end, which avoids a [`BrokenPipeError`](https://docs.python.org/3.14/library/exceptions.html#BrokenPipeError) during garbage collection and on [`multiprocessing.Queue.close()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Queue.close) calls. Géry Ogam authored the patch.

[gh-91910](https://github.com/python/cpython/issues/91910): Supply the missing f prefix on f-strings within error messages emitted by the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) and [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) modules.

[gh-90622](https://github.com/python/cpython/issues/90622): Within `concurrent.futures.process.ProcessPoolExecutor`, forbid the “fork” multiprocessing start method whenever the fresh `max_tasks_per_child` capability is active, because combining threads with fork can stall the child processes. When no `mp_context` is given under that condition, fall back to the safer “spawn” start method by default.

[bpo-46720](https://bugs.python.org/issue?@action=redirect&bpo=46720): Extend [`multiprocessing.set_executable()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.set_executable) so it accepts path-like objects on Windows, matching what Unix-like systems already allow. Géry Ogam authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
