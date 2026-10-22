# Python 3.9.0 alpha 4 / c api / threads

[bpo-39511](https://bugs.python.org/issue?@action=redirect&bpo=39511): The [`PyThreadState_Clear()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_Clear) function now triggers the `PyThreadState.on_delete` callback. Earlier, that took place inside [`PyThreadState_Delete()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_Delete).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
