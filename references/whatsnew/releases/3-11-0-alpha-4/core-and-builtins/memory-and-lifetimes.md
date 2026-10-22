# Python 3.11.0 alpha 4 / core and builtins / memory and lifetimes

[bpo-45953](https://bugs.python.org/issue?@action=redirect&bpo=45953): Within _PyRuntimeState.interpreters the principal interpreter is now allocated statically (forming part of _PyRuntime). The same holds for every interpreter’s starting thread state. The upshot is reduced allocation while the runtime initializes, along with improved memory locality for these crucial state objects.

[bpo-46347](https://bugs.python.org/issue?@action=redirect&bpo=46347): Plug a memory leak inside PyEval_EvalCodeEx.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
