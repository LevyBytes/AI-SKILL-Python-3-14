# What's new in Python 3.14 / Notable changes in 3.14.1

### Notable changes in 3.14.1

- Two new functions, [`PyUnstable_ThreadState_SetStackProtection()`](https://docs.python.org/3.14/c-api/threads.html#c.PyUnstable_ThreadState_SetStackProtection) and [`PyUnstable_ThreadState_ResetStackProtection()`](https://docs.python.org/3.14/c-api/threads.html#c.PyUnstable_ThreadState_ResetStackProtection), let you configure the base address and the size of the stack protection on a Python thread state. (Contributed by Victor Stinner in [gh-139653](https://github.com/python/cpython/issues/139653).)

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-14-changes-in-the-c-api.md) · [Next source section](gc.md) · [Release/subject declaration](summary-release-highlights.md)
