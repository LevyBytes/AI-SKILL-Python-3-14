# Python 3.13.0 alpha 1 / core and builtins / imports and modules

[gh-104879](https://github.com/python/cpython/issues/104879): Repair a crash when reading the `__module__` attribute on type aliases declared outside a module. Jelle Zijlstra prepared the patch.

[gh-104621](https://github.com/python/cpython/issues/104621): Modules that lack support will from now on consistently refuse to import.

[gh-106719](https://github.com/python/cpython/issues/106719): Stop swallowing arbitrary errors raised by the `__annotations__` getter and setter on the type and module types.

[gh-106210](https://github.com/python/cpython/issues/106210): Dropped the Emscripten import trampoline since Pyodide no longer required it.

[gh-105908](https://github.com/python/cpython/issues/105908): Repaired a defect in which [gh-99111](https://github.com/python/cpython/issues/99111) broke the future import `barry_as_FLUFL` within the Python REPL.

[gh-105340](https://github.com/python/cpython/issues/105340): Surface the comprehension iteration variable in `locals()` when inside a module-scope or class-scope comprehension.

[gh-108716](https://github.com/python/cpython/issues/108716): Deep-freezing of code objects was switched off. Modules remain frozen, which spares a file system search for the common modules.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
