# Python 3.14.0 alpha 6 / library / concurrent futures

[gh-128041](https://github.com/python/cpython/issues/128041): Two new methods, [`concurrent.futures.ProcessPoolExecutor.terminate_workers()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor.terminate_workers) and [`concurrent.futures.ProcessPoolExecutor.kill_workers()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor.kill_workers), now let you stop or forcibly kill every running worker process belonging to a given pool. Charles Machalow contributed this in [gh-130849](https://github.com/python/cpython/issues/130849).

[gh-74028](https://github.com/python/cpython/issues/74028): An optional `buffersize` argument now exists on [`concurrent.futures.Executor.map()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor.map), capping how many submitted tasks may have unyielded results at once. Once that buffer fills, walking through the *iterables* halts until something is pulled out of the buffer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
