# Python 3.13.0 beta 1 / library / tkinter

[gh-66410](https://github.com/python/cpython/issues/66410): If you set the `tkinter` module global `wantobjects` to `2` ahead of constructing the [`Tk`](https://docs.python.org/3.14/library/tkinter.html#tkinter.Tk) object, or call the `wantobjects()` method of the `Tk` object passing `2`, then arguments to callbacks registered through the [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) module now arrive as assorted Python objects (`int`, `float`, `bytes`, `tuple`) depending on their internal Tcl representation, in place of always being `str`. The default value of `tkinter.wantobjects` is now `2`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
