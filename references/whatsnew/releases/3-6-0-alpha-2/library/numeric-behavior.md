# Python 3.6.0 alpha 2 / library / numeric behavior

[bpo-27186](https://bugs.python.org/issue?@action=redirect&bpo=27186): Brought in os.PathLike and os.fspath() (one piece of [**PEP 519**](https://peps.python.org/pep-0519/)).

- A fresh typing.py edition delivers a number of new classes and capabilities: @overload outside stubs, Reversible, DefaultDict, Text, ContextManager, Type[], NewType(), TYPE_CHECKING, plus a host of bug fixes (be aware some of these new capabilities are still unimplemented in mypy or other static analyzers). Classes for [**PEP 492**](https://peps.python.org/pep-0492/) (Awaitable, AsyncIterable, AsyncIterator) were added as well (they actually shipped in 3.5.1 but went unmentioned).

[bpo-23026](https://bugs.python.org/issue?@action=redirect&bpo=23026): winreg.QueryValueEx() now hands back an integer for the REG_QWORD type.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
