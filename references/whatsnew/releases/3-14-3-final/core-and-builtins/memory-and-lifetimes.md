# Python 3.14.3 final / core and builtins / memory and lifetimes

[gh-144194](https://github.com/python/cpython/issues/144194): Correct the error handling in perf jitdump startup when a memory allocation does not succeed.

[gh-143228](https://github.com/python/cpython/issues/143228): Address a use-after-free in the perf trampoline that appeared when profiling was toggled with threads running, or during interpreter finalization while daemon threads were still active. Reference counting now guarantees a trampoline is not released while any code object might still point at it. Pach by Pablo Galindo

[gh-142664](https://github.com/python/cpython/issues/142664): Address a use-after-free crash in [`memoryview.__hash__`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) that happened when the referenced object's `__hash__` method altered that object or the view itself. Bénédikt Tran authored the patch.

[gh-142776](https://github.com/python/cpython/issues/142776): Close a file descriptor leak in import.c

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
