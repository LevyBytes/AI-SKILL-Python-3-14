# Python 3.14.0 beta 3 / core and builtins / asyncio

[gh-135371](https://github.com/python/cpython/issues/135371): [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) debugging tools were fixed so they correctly render internal coroutine call stacks together with external task dependencies. Complete execution context is now displayed by the `python -m asyncio ps` and `python -m asyncio pstree` commands. Pablo Galindo authored this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
