# Python 3.14.0 beta 1 / core and builtins / asyncio

[gh-91048](https://github.com/python/cpython/issues/91048): A new `python -m asyncio ps PID` command-line interface lets you examine asyncio tasks inside a live Python process, presenting a flat table of await relationships. There is also a tree-view variant, `python -m asyncio pstree PID`. Both help when debugging async code. Pablo Galindo, ??ukasz Langa, Yury Selivanov, and Marta Gomez Macias wrote this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
