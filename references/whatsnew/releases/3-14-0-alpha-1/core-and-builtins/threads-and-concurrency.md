# Python 3.14.0 alpha 1 / core and builtins / threads and concurrency

[gh-120198](https://github.com/python/cpython/issues/120198): Stop a crash arising when several threads read from and write to one object's same `__class__` concurrently.

[gh-120384](https://github.com/python/cpython/issues/120384): Close an array out of bounds crash inside `list_ass_subscript`, reachable through some carefully crafted input. That includes simultaneously mutating one list — say, one thread doing a slice assignment as a second thread empties it.

[gh-118844](https://github.com/python/cpython/issues/118844): Repair the build breakage that happened when both `--disable-gil` and `--enable-experimental-jit` were configured together.

[gh-117657](https://github.com/python/cpython/issues/117657): Repair data races on the field holding a pointer to the interpreter's main thread that show up inside free-threaded builds.

[gh-123321](https://github.com/python/cpython/issues/123321): Stop a Parser/myreadline race condition from causing a segfault under multi-threaded use. Bar Harel and Amit Wienner supplied the patch.

[gh-123275](https://github.com/python/cpython/issues/123275): Permit [`-X gil=1`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) plus [`PYTHON_GIL=1`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_GIL) on builds that are not free-threaded.

[gh-119369](https://github.com/python/cpython/issues/119369): Resolve a thread-deletion deadlock in the free-threaded build; it surfaced once the GIL got enabled while running.

[gh-119525](https://github.com/python/cpython/issues/119525): Resolve a deadlock around the `_PyType_Lookup()` cache in the free-threaded build whenever the GIL gets switched on dynamically while running.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
