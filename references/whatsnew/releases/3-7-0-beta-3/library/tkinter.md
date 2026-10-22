# Python 3.7.0 beta 3 / library / tkinter

[bpo-32857](https://bugs.python.org/issue?@action=redirect&bpo=32857): Within [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter), `after_cancel(None)` now raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) rather than canceling the first scheduled function. Patch by Cheryl Sabella.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
