# Python 3.8.0 beta 1 / library / thread

[bpo-37076](https://bugs.python.org/issue?@action=redirect&bpo=37076): [`_thread.start_new_thread()`](https://docs.python.org/3.14/library/_thread.html#thread.start_new_thread) now records an uncaught exception thrown by the function through [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook) in place of [`sys.excepthook()`](https://docs.python.org/3.14/library/sys.html#sys.excepthook), giving the hook visibility of the function that raised.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
