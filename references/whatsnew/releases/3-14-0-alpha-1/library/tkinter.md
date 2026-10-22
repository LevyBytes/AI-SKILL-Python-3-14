# Python 3.14.0 alpha 1 / library / tkinter

[gh-119614](https://github.com/python/cpython/issues/119614): Stop strings holding embedded null characters from being truncated during some internal [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) operations.

[gh-101830](https://github.com/python/cpython/issues/101830): Reading the string form of a [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) object no longer forces the backing Tcl object into a string on Windows.

[gh-123504](https://github.com/python/cpython/issues/123504): Repaired a reference leak during teardown of [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter).

[gh-112672](https://github.com/python/cpython/issues/112672): Make building [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) against Tcl 9.0 possible.

[gh-125235](https://github.com/python/cpython/issues/125235): On Windows, keep the [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) TCL paths within a venv pointed at the base installation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
