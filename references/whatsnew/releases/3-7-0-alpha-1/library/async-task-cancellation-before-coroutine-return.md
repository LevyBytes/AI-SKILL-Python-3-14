# Python 3.7.0 alpha 1 / library / scenario where task cancel could disregarded task s coroutine executing

[bpo-30048](https://bugs.python.org/issue?@action=redirect&bpo=30048): A scenario where `Task.cancel()` could be disregarded — when the task's coroutine was executing and then returned without a further `await` — was corrected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
