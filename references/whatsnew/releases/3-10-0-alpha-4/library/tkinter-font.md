# Python 3.10.0 alpha 4 / library / tkinter font

[bpo-42759](https://bugs.python.org/issue?@action=redirect&bpo=42759): Corrected the equality comparison of `tkinter.Variable` together with [`tkinter.font.Font`](https://docs.python.org/3.14/library/tkinter.font.html#tkinter.font.Font). Two such objects tied to distinct Tcl interpreters now always compare as unequal, even when they share a name.

[bpo-35728](https://bugs.python.org/issue?@action=redirect&bpo=35728): Gave [`tkinter.font.nametofont()`](https://docs.python.org/3.14/library/tkinter.font.html#tkinter.font.nametofont) a root parameter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
