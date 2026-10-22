# Python 3.8.0 alpha 1 / library / tkinter

[bpo-32857](https://bugs.python.org/issue?@action=redirect&bpo=32857): Within [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter), `after_cancel(None)` now raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) rather than canceling the earliest scheduled function. Patch by Cheryl Sabella.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
