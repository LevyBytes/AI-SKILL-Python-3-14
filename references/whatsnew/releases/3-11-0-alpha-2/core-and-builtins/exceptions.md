# Python 3.11.0 alpha 2 / core and builtins / exceptions

[bpo-45716](https://bugs.python.org/issue?@action=redirect&bpo=45716): Sharpen the [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) text shown when `True`, `None` or `False` appear as keywords within a function call. Pablo Galindo wrote the patch.

[bpo-45379](https://bugs.python.org/issue?@action=redirect&bpo=45379): Make the [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) text clearer when an explicit import of a frozen module is attempted while frozen modules are turned off.

[bpo-45292](https://bugs.python.org/issue?@action=redirect&bpo=45292): Carry out [**PEP 654**](https://peps.python.org/pep-0654/). Introduce [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup) plus [`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup). Refresh the traceback display code.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
