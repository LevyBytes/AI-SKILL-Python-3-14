# Python 3.13.0 alpha 3 / library / tkinter

[gh-75666](https://github.com/python/cpython/issues/75666): Correct how the [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) widget's `unbind()` method behaves when given two arguments. Formerly, `widget.unbind(sequence, funcid)` wiped out the current binding for *sequence*, leaving *sequence* unbound, and removed the *funcid* command. Now only *funcid* is stripped from the binding for *sequence*, the other commands stay, and the *funcid* command is deleted. *sequence* ends up unbound solely when *funcid* happened to be the final bound command.

[gh-113877](https://github.com/python/cpython/issues/113877): Resolved the [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) method `winfo_pathname()` under 64-bit Windows.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
