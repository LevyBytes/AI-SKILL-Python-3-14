# Python 3.14.1 final / c api / threads

[gh-139653](https://github.com/python/cpython/issues/139653): Introduce the [`PyUnstable_ThreadState_SetStackProtection()`](https://docs.python.org/3.14/c-api/threads.html#c.PyUnstable_ThreadState_SetStackProtection) plus [`PyUnstable_ThreadState_ResetStackProtection()`](https://docs.python.org/3.14/c-api/threads.html#c.PyUnstable_ThreadState_ResetStackProtection) functions, which set both the stack protection base address and the stack protection size of a Python thread state. Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
