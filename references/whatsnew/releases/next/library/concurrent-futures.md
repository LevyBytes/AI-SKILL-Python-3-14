# Python next / library / concurrent futures

[gh-101267](https://github.com/python/cpython/issues/101267): Should a worker process die without warning, [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) now assigns a distinct [`BrokenProcessPool`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.process.BrokenProcessPool) exception to every pending future rather than passing one shared instance to all of them. That shared exception yielded broken tracebacks, because each [`Future.result()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Future.result) invocation re-raised that identical object and tacked yet another traceback copy onto it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
