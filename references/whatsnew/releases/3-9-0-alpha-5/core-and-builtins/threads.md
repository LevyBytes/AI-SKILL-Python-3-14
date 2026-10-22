# Python 3.9.0 alpha 5 / core and builtins / threads

[bpo-40010](https://bugs.python.org/issue?@action=redirect&bpo=40010): Make pending calls faster in multithreaded programs. Whenever a thread other than the main one queues a pending call ([`Py_AddPendingCall()`](https://docs.python.org/3.14/c-api/threads.html#c.Py_AddPendingCall)), the bytecode evaluation loop stops breaking at every bytecode instruction to test for pending calls that cannot run. Only the main thread is allowed to run pending calls.

Up to now, the bytecode evaluation loop kept breaking at each instruction right up until the main thread ran pending calls.

[bpo-39984](https://bugs.python.org/issue?@action=redirect&bpo=39984): When [`Py_AddPendingCall()`](https://docs.python.org/3.14/c-api/threads.html#c.Py_AddPendingCall) gets called within a subinterpreter, the function is now queued for that subinterpreter to run rather than running from the main interpreter. Every subinterpreter now keeps its own list of scheduled calls.

[bpo-39877](https://bugs.python.org/issue?@action=redirect&bpo=39877): Stop the random [`PyEval_RestoreThread()`](https://docs.python.org/3.14/c-api/threads.html#c.PyEval_RestoreThread) crash on exit when daemon threads exist. It now reaches the `_PyRuntime` variable directly rather than going through `tstate->interp->runtime`, because `tstate` may dangle once [`Py_Finalize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Finalize) has run. Furthermore, the daemon thread now departs before attempting to acquire the GIL.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
