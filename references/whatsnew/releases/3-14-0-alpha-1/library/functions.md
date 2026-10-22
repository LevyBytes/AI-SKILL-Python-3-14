# Python 3.14.0 alpha 1 / library / functions

[gh-119189](https://github.com/python/cpython/issues/119189): Using the `**` operator or [`pow()`](https://docs.python.org/3.14/library/functions.html#pow) with a [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) as the base and an exponent that is neither rational, a float, nor a complex no longer converts the fraction into a float.

[gh-103194](https://github.com/python/cpython/issues/103194): Tkinter is readied for the C API changes coming in Tcl 8.7/9.0, so that `_tkinter.Tcl_Obj` is no longer handed back where a [`bool`](https://docs.python.org/3.14/library/functions.html#bool), [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray), or [`int`](https://docs.python.org/3.14/library/functions.html#int) was expected.

[gh-121450](https://github.com/python/cpython/issues/121450): Hard-coded breakpoints (namely [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) and [`pdb.set_trace()`](https://docs.python.org/3.14/library/pdb.html#pdb.set_trace)) now recycle the latest `Pdb` instance that invoked `Pdb.set_trace()` rather than spinning up a fresh one every time. Consequently, per-instance data such as `display` and `commands` survive between Hard-coded breakpoints.

[gh-123240](https://github.com/python/cpython/issues/123240): Emits audit events for [`input()`](https://docs.python.org/3.14/library/functions.html#input) inside the new REPL.

[gh-120541](https://github.com/python/cpython/issues/120541): Make the prompt shown in the ?less? pager better when [`help()`](https://docs.python.org/3.14/library/functions.html#help) receives a non-string argument.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
