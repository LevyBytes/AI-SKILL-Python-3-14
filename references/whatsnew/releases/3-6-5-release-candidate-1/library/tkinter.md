# Python 3.6.5 release candidate 1 / library / tkinter

[bpo-32857](https://bugs.python.org/issue?@action=redirect&bpo=32857): Within [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter), invoking `after_cancel(None)` will now raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) rather than canceling whatever function was scheduled first. Cheryl Sabella authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
