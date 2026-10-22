# Python 3.5.2 release candidate 1 / library / distutils

[bpo-20900](https://bugs.python.org/issue?@action=redirect&bpo=20900): The distutils register command now decodes HTTP responses properly. The earliest patch came from ingrid.

- A fresh release of typing.py brings in several additional classes and capabilities: @overload outside stubs, Reversible, DefaultDict, Text, ContextManager, Type[], NewType(), TYPE_CHECKING, plus many bug fixes (be aware that a number of the newer features are not yet supported by mypy or other static analyzers). On top of that, the classes for [**PEP 492**](https://peps.python.org/pep-0492/) (Awaitable, AsyncIterable, AsyncIterator) were added (they actually landed in 3.5.1 yet were never called out).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
