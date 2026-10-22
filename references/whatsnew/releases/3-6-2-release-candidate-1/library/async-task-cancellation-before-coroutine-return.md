# Python 3.6.2 release candidate 1 / library / resolved situation where task cancel could disregarded while task ran

[bpo-30048](https://bugs.python.org/issue?@action=redirect&bpo=30048): Resolved a situation where `Task.cancel()` could be disregarded while the task ran its coroutine and that coroutine returned without any further `await`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
