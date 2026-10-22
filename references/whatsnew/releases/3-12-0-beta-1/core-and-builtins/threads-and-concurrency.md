# Python 3.12.0 beta 1 / core and builtins / threads and concurrency

[gh-103323](https://github.com/python/cpython/issues/103323): Our use of `_PyRuntime.tstate_current` has been swapped out for a thread-local variable. Because this is quite a low-level implementation detail, behavior should be unchanged.

[gh-99113](https://github.com/python/cpython/issues/99113): The GIL can now (optionally) be per-interpreter. That is the core shift behind PEP 684, made feasible thanks to the isolated state every interpreter keeps in the process. Behavior of the main interpreter is left untouched. Similarly, interpreters spun up via `Py_NewInterpreter()` see no change. Obtain an interpreter that owns its GIL by calling `Py_NewInterpreterFromConfig()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
