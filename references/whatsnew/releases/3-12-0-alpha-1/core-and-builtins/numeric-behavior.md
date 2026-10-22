# Python 3.12.0 alpha 1 / core and builtins / numeric behavior

[gh-91079](https://github.com/python/cpython/issues/91079): Split Python recursion checking apart from C recursion checking, which lowers the odds of a C stack overflow and makes raising the recursion limit safe.

[gh-96678](https://github.com/python/cpython/issues/96678): Repair undefined behaviour in C code stemming from null pointer arithmetic.

[gh-94438](https://github.com/python/cpython/issues/94438): Takes into account instructions capable of pushing NULL onto the stack while assigning a frame's line number. Avoids certain (improbable) crashes.

[gh-92914](https://github.com/python/cpython/issues/92914): Rounds the allocated size of lists up to the next even number every time.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
