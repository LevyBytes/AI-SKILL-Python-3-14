# Python 3.13.0 beta 1 / library / typing

[gh-117516](https://github.com/python/cpython/issues/117516): Introduces [`typing.TypeIs`](https://docs.python.org/3.14/library/typing.html#typing.TypeIs), which realizes [**PEP 742**](https://peps.python.org/pep-0742/). Jelle Zijlstra contributed the patch.

[gh-118168](https://github.com/python/cpython/issues/118168): Repairs faulty argument substitution whenever [`typing.Unpack`](https://docs.python.org/3.14/library/typing.html#typing.Unpack) is combined with the builtin [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple). With certain invalid types, `typing.Unpack` now raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). The patch came from Jelle Zijlstra.

[gh-118660](https://github.com/python/cpython/issues/118660): Give [`typing.ContextManager`](https://docs.python.org/3.14/library/typing.html#typing.ContextManager) and [`typing.AsyncContextManager`](https://docs.python.org/3.14/library/typing.html#typing.AsyncContextManager) an optional second type parameter standing for the return types of [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) and [`__aexit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aexit__) in turn. That parameter defaults to `bool | None`.

[gh-118648](https://github.com/python/cpython/issues/118648): Supply type parameter defaults for [`typing.Generator`](https://docs.python.org/3.14/library/typing.html#typing.Generator) and [`typing.AsyncGenerator`](https://docs.python.org/3.14/library/typing.html#typing.AsyncGenerator).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
