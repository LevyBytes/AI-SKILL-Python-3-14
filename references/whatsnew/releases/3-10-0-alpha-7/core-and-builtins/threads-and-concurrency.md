# Python 3.10.0 alpha 7 / core and builtins / threads and concurrency

[bpo-43406](https://bugs.python.org/issue?@action=redirect&bpo=43406): Closed a possible race condition in which `PyErr_CheckSignals` attempts to run a non-Python signal handler.

[bpo-43390](https://bugs.python.org/issue?@action=redirect&bpo=43390): For the VM's default signal handlers, CPython now sets the `SA_ONSTACK` flag inside `PyOS_setsig`. This plays better with other in-process code that an extension module or embedding scenario might bring along (Golang's cgo, say), where tiny thread stacks are common and `sigaltstack()` has been used to set up signal handlers. The change is a no-op for the overwhelming majority of processes that never touch sigaltstack.

[bpo-29988](https://bugs.python.org/issue?@action=redirect&bpo=29988): Process asynchronous exceptions and GIL-drop requests only upon returning from a call or at the back edges of loops. This guarantees [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) still runs in with statements, including under interrupts.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
