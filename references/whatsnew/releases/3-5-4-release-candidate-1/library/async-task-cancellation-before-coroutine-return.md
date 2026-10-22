# Python 3.5.4 release candidate 1 / library / repaired situation where task cancel could disregarded while task runs

[bpo-30048](https://bugs.python.org/issue?@action=redirect&bpo=30048): Repaired the situation where `Task.cancel()` could be disregarded while the task runs a coroutine and that coroutine returns without any further `await`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
