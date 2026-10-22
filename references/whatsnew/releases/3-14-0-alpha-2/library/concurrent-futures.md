# Python 3.14.0 alpha 2 / library / concurrent futures

[gh-125451](https://github.com/python/cpython/issues/125451): Resolve a deadlock arising when [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) shuts down at the same time as an error while feeding a job into a worker process.

[gh-124694](https://github.com/python/cpython/issues/124694): A new [`concurrent.futures.InterpreterPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor) has landed, letting you execute code across several isolated interpreters. With it you sidestep the constraints that CPU-bound threads face under the GIL. Eric Snow contributed the patch.

This work bears no relation to [**PEP 734**](https://peps.python.org/pep-0734/).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
