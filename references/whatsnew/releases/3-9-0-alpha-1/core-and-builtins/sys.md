# Python 3.9.0 alpha 1 / core and builtins / sys

[bpo-37316](https://bugs.python.org/issue?@action=redirect&bpo=37316): Corrected the [`PySys_Audit()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_Audit) call within [`mmap.mmap`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap).

[bpo-37467](https://bugs.python.org/issue?@action=redirect&bpo=37467): Corrected [`sys.excepthook()`](https://docs.python.org/3.14/library/sys.html#sys.excepthook) plus `PyErr_Display()` whenever a filename happens to be a bytes string. Take, for example, a SyntaxError exception whose filename attribute is a bytes string.

[bpo-37392](https://bugs.python.org/issue?@action=redirect&bpo=37392): Deleted the `sys.getcheckinterval()` and `sys.setcheckinterval()` functions. They had been deprecated ever since Python 3.2. Reach instead for [`sys.getswitchinterval()`](https://docs.python.org/3.14/library/sys.html#sys.getswitchinterval) and [`sys.setswitchinterval()`](https://docs.python.org/3.14/library/sys.html#sys.setswitchinterval). The `check_interval` field of the `PyInterpreterState` structure was likewise removed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
