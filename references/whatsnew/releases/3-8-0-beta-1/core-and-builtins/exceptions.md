# Python 3.8.0 beta 1 / core and builtins / exceptions

[bpo-1875](https://bugs.python.org/issue?@action=redirect&bpo=1875): A [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) now surfaces when a code block destined to be optimized away (for instance, if conditions that never hold) carries syntax errors. Pablo Galindo wrote the patch.

[bpo-36829](https://bugs.python.org/issue?@action=redirect&bpo=36829): When no traceback is currently active, [`PyErr_WriteUnraisable()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_WriteUnraisable) now builds a traceback object. It additionally invokes [`PyErr_NormalizeException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_NormalizeException) together with [`PyException_SetTraceback()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyException_SetTraceback) so the exception value gets normalized. Any resulting error is swallowed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
