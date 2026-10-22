# Process Control

### Process Control

 void Py_FatalError(const char *message)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Emit a fatal error message and terminate the process. No cleanup happens. Reserve this routine for situations where a detected condition would make continuing to use the Python interpreter unsafe; for instance, when the object administration looks corrupted. On Unix, the standard C library routine `abort()` is invoked, which will try to write out a `core` file.

A macro stands in for the `Py_FatalError()` function and automatically records the name of the active function, except when the `Py_LIMITED_API` macro happens to be defined.

Changed in version 3.9: Log the function name automatically.

 void Py_Exit(int status)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Terminate the running process. This invokes [`Py_FinalizeEx()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_FinalizeEx) and afterward invokes the standard C library routine `exit(status)`. Should `Py_FinalizeEx()` report an error, the exit status becomes 120.

Changed in version 3.6: Errors from finalization no longer ignored.

 int Py_AtExit(void (*func)())

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Register a cleanup function for [`Py_FinalizeEx()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_FinalizeEx) to invoke. That cleanup function is called with no arguments and ought to return no value. No more than 32 cleanup functions may be registered. On a successful registration, `Py_AtExit()` yields `0`; otherwise it yields `-1`. Whichever cleanup function was registered last runs first. Every cleanup function runs at most a single time. Given that Python’s internal finalization will already have finished before the cleanup function, *func* should not call any Python APIs.

See also

[`PyUnstable_AtExit()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.PyUnstable_AtExit) for passing a `void *data` argument.

[Subject index](INDEX.md) · [Previous source contract](pysys-audit-to-pysys-addaudithook.md)
