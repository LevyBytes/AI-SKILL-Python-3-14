# Python 3.13.0 alpha 1 / core and builtins / semaphore nested process state

[gh-108520](https://github.com/python/cpython/issues/108520): `multiprocessing.synchronize.SemLock.__setstate__()` was fixed so it correctly sets up `multiprocessing.synchronize.SemLock._is_fork_ctx`. That repairs a regression seen when a SemLock travels across nested processes.

Additionally, `multiprocessing.synchronize.SemLock.is_fork_ctx` was renamed to `multiprocessing.synchronize.SemLock._is_fork_ctx` so that it is not exposed as public API.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
