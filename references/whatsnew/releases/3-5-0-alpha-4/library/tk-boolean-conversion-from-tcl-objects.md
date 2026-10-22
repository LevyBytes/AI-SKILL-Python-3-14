# Python 3.5.0 alpha 4 / library / tkinter tkapp getboolean accepts tcl obj while always yielding bool

[bpo-15133](https://bugs.python.org/issue?@action=redirect&bpo=15133): _tkinter.tkapp.getboolean() now accepts Tcl_Obj while always yielding bool. tkinter.BooleanVar now validates the values supplied (it accepts bool, int, str, and Tcl_Obj). tkinter.BooleanVar.get() now invariably yields bool.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
