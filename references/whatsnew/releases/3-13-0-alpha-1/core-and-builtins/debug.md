# Python 3.13.0 alpha 1 / core and builtins / debug

[gh-106597](https://github.com/python/cpython/issues/106597): A fresh debug layout of offsets now lives on the `_PyRuntimeState`; it helps out-of-process debuggers and profilers locate the offsets of pertinent interpreter structures without caring how Python was built and without needing to copy the headers. Pablo Galindo authored this.

[gh-104584](https://github.com/python/cpython/issues/104584): Brought in a fresh, experimental tracing optimizer and interpreter (a.k.a. "tier 2"). For now it pessimizes, so hold off using it — it is infrastructure that lets us trial optimizing passes. Enable it by passing `-Xuops` or by setting `PYTHONUOPS=1`. For debug output, assign `PYTHONUOPSDEBUG=N`, in which `N` selects a debug level (running 0-4; here 0 emits nothing and 4 floods the log with detail).

[gh-105831](https://github.com/python/cpython/issues/105831): Repair an f-string defect where a debug expression (the `=` sign) sitting on a file's final line caused the debug buffer holding the expression text to come up one character short.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
