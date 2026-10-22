# Python 3.9.0 alpha 5 / core and builtins / threads and concurrency

[bpo-40010](https://bugs.python.org/issue?@action=redirect&bpo=40010): Make signal handling faster in multithreaded programs. Whenever a thread other than the main one receives a signal, the bytecode evaluation loop stops breaking at every bytecode instruction to test for pending signals that cannot be handled. Only the main thread of the main interpreter is allowed to handle signals.

Up to now, the bytecode evaluation loop kept breaking at each instruction right up until the main thread handled signals.

[bpo-39776](https://bugs.python.org/issue?@action=redirect&bpo=39776): Resolve a race condition under which threads spawned by PyGILState_Ensure() might receive a duplicate id.

Anything depending on tstate->id is affected, like the contextvar caching machinery, which under heavy thread load could hand back stale cached objects (seen in embedded scenarios).

[bpo-38091](https://bugs.python.org/issue?@action=redirect&bpo=38091): Adjust the import deadlock detection code so it stops deadlocking itself.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
