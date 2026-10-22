# Python 3.12.0 alpha 1 / library / inspect

[gh-83901](https://github.com/python/cpython/issues/83901): The [`Signature.bind`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature.bind) error text for absent keyword-only arguments is improved.

[gh-96073](https://github.com/python/cpython/issues/96073): Within [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect), the overzealous swapping of “`typing.`” while formatting annotations is corrected.

[gh-97799](https://github.com/python/cpython/issues/97799): `dataclass` turns to [`inspect.get_annotations()`](https://docs.python.org/3.14/library/inspect.html#inspect.get_annotations) when inspecting the annotations present on class objects.

[gh-84753](https://github.com/python/cpython/issues/84753): [`inspect.iscoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction), [`inspect.isgeneratorfunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.isgeneratorfunction), together with [`inspect.isasyncgenfunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.isasyncgenfunction), at last yield `True` for duck-typed objects that behave like functions, such as instances of [`unittest.mock.AsyncMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.AsyncMock).

This brings [`inspect.iscoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction) into line with how `asyncio.iscoroutinefunction()` behaves. Mehdi ABAAKOUK supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
