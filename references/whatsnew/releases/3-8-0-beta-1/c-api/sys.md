# Python 3.8.0 beta 1 / c api / sys

[bpo-36728](https://bugs.python.org/issue?@action=redirect&bpo=36728): The `PyEval_ReInitThreads()` function is now gone from the C API. There should be no explicit call to it: rely on [`PyOS_AfterFork_Child()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork_Child) instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
