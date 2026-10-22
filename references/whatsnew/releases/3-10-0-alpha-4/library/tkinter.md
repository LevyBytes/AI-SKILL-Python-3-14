# Python 3.10.0 alpha 4 / library / tkinter

[bpo-15303](https://bugs.python.org/issue?@action=redirect&bpo=15303): [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) now handles widgets whose boolean value is False.

[bpo-42630](https://bugs.python.org/issue?@action=redirect&bpo=42630): When a default root window is needed but has not been built yet (or cannot be built on its own), [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) functions and constructors now raise [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) carrying a clear message rather than the cryptic [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) or [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
