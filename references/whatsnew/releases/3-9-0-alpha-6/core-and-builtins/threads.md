# Python 3.9.0 alpha 6 / core and builtins / threads

[bpo-20526](https://bugs.python.org/issue?@action=redirect&bpo=20526): Repair [`PyThreadState_Clear()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_Clear). Since `PyThreadState.frame` is a borrowed reference rather than a strong one, `PyThreadState_Clear()` is forbidden from invoking `Py_CLEAR(tstate->frame)`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
