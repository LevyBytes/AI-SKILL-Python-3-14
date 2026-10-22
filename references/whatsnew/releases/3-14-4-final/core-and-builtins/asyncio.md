# Python 3.14.4 final / core and builtins / asyncio

[gh-146308](https://github.com/python/cpython/issues/146308): Resolved a number of error-handling problems inside the `_remote_debugging` module, among them safer checking of remote `int` objects, sharper asyncio task-chain failure reporting, and cache-cleanup repairs that keep allocation failures from leaking or double-freeing metadata. Pablo Galindo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
