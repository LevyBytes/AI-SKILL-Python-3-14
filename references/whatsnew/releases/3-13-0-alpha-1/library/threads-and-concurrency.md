# Python 3.13.0 alpha 1 / library / threads and concurrency

[gh-104310](https://github.com/python/cpython/issues/104310): During the beta 1 cut we shipped a helper for extension module authors to call while checking their module for multi-interpreter support or operation under a per-interpreter GIL. That helper was renamed from `allowing_all_extensions` over to `_incompatible_extension_module_restrictions`. Its "disable_check" argument now defaults to `False` instead of `True`, lining up better with the fresh function name.

[gh-102024](https://github.com/python/cpython/issues/102024): Cut down on `_idle_semaphore.release()` calls inside `concurrent.futures.thread._worker()`.

[gh-105829](https://github.com/python/cpython/issues/105829): Resolved a concurrent.futures.ProcessPoolExecutor deadlock

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
