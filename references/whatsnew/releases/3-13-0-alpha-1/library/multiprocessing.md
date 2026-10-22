# Python 3.13.0 alpha 1 / library / multiprocessing

[gh-106739](https://github.com/python/cpython/issues/106739): Include the `rtype_cache` within the warning text (on top of the leaked-object type and leaked-object count that the message already carries) so that tracing leaked objects becomes simpler once the multiprocessing resource tracker process spots leaks during shutdown. The extra detail speeds up working out what leaked and why a leaked object never got cleaned up.

[gh-94777](https://github.com/python/cpython/issues/94777): Stopped a hang in [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) `ProcessPoolExecutor` occurring when a child process dies mid-write to the call queue.

[gh-109593](https://github.com/python/cpython/issues/109593): Sidestep a deadlock arising from a reentrant call into the multiprocessing resource tracker. Though improbable, such a reentrant call may occur if a GC pass runs the finalizer for a multiprocessing object like SemLock.

[gh-109649](https://github.com/python/cpython/issues/109649): Across [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing), [`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures), and [`compileall`](https://docs.python.org/3.14/library/compileall.html#module-compileall): swap [`os.cpu_count()`](https://docs.python.org/3.14/library/os.html#os.cpu_count) out for [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count) when picking the default count of worker threads and processes. Fetch the CPU affinity where that is available. Victor Stinner wrote the patch.

[gh-107963](https://github.com/python/cpython/issues/107963): Corrected [`multiprocessing.set_forkserver_preload()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.set_forkserver_preload) so it validates the supplied list of module names. Donghee Na authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
