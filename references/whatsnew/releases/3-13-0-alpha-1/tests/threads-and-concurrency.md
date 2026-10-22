# Python 3.13.0 alpha 1 / tests / threads and concurrency

[gh-108388](https://github.com/python/cpython/issues/108388): Divided test_multiprocessing_fork, test_multiprocessing_forkserver, and test_multiprocessing_spawn into test packages. Every package holds 4 sub-tests: processes, threads, manager, and misc. This permits running additional tests in parallel and thereby trims the overall test duration. Victor Stinner authored the patch.

[gh-110167](https://github.com/python/cpython/issues/110167): Resolved a test_socket deadlock that struck when the server timed out while its client thread kept running. The fix avoids holding a lock while invoking cleanup callbacks inside doCleanups(). One cleanup callback blocks until the client wraps up, and the client itself could deadlock if it had called addCleanup() under those circumstances. Victor Stinner authored the patch.

[gh-110031](https://github.com/python/cpython/issues/110031): Bypass the test_threading tests that combine thread and fork when Python is compiled using Address Sanitizer (ASAN). Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
