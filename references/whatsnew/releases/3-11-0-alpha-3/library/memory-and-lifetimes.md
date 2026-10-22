# Python 3.11.0 alpha 3 / library / memory and lifetimes

[bpo-37658](https://bugs.python.org/issue?@action=redirect&bpo=37658): Correct a case where, under particular conditions, `asyncio.wait_for()` could let a coroutine finish successfully yet neglect to return its result, with the potential to cause memory leaks or further problems.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
