# Python 3.13.0 alpha 1 / core and builtins / threads and concurrency

[gh-104812](https://github.com/python/cpython/issues/104812): The "pending call" machinery henceforth functions for every interpreter, not the main one alone, and executes across all threads rather than only the main thread. A handful of calls remain restricted to the main thread, hence to the main interpreter. Neither signal handling nor the current public C-API (`Py_AddPendingCall()`) is touched by this change, as both continue to address the main thread exclusively. The new behavior is intended purely for internal consumption for the time being, given that the fallout of using it is not yet well understood beyond a few tightly bounded scenarios. The change finally delivers the capability envisioned back when the state was turned per-interpreter several years earlier.

[gh-109793](https://github.com/python/cpython/issues/109793): When a subinterpreter is torn down during runtime finalization, the main thread no longer quits too early. This mattered especially because, once triggered, the Python process would invariably exit with a 0 exitcode even after a failure.

[gh-110455](https://github.com/python/cpython/issues/110455): The `assert(tstate->thread_id > 0)` statement is now guarded by `#ifndef HAVE_PTHREAD_STUBS`. That lets pydebug builds function on WASI, which (for now) has no thread support.

[gh-105716](https://github.com/python/cpython/issues/105716): The situation where subinterpreters carry background threads is now handled correctly. Previously those threads got in the way of cleaning them up and destroying them, and also blocked running a second script.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
