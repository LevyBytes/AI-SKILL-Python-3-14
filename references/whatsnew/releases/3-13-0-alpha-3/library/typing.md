# Python 3.13.0 alpha 3 / library / typing

[gh-113320](https://github.com/python/cpython/issues/113320): Resolved a Python 3.12 regression under which [`Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol) classes left unmarked as [`runtime-checkable`](https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable) would be needlessly introspected, possibly raising exceptions should the protocol hold problematic members. Alex Waygood supplied this patch.

[gh-111874](https://github.com/python/cpython/issues/111874): During creation of a [`typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) class, make sure [`__set_name__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__) fires on every object that defines `__set_name__` and sits among the values of the `NamedTuple` class's class dictionary. Alex Waygood wrote the patch.

[gh-74690](https://github.com/python/cpython/issues/74690): For [`runtime-checkable protocols`](https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable) carrying only a single callable member, [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) checks gain about 20% in speed. The matching [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) checks for those protocols become roughly 10% faster. Alex Waygood wrote the patch.

[gh-112618](https://github.com/python/cpython/issues/112618): Correct a caching defect tied to [`typing.Annotated`](https://docs.python.org/3.14/library/typing.html#typing.Annotated). `Annotated[str, True]` is no longer identical to `Annotated[str, 1]`.

[gh-112509](https://github.com/python/cpython/issues/112509): Repair corner cases where a key might appear simultaneously in the `__required_keys__` and `__optional_keys__` attributes of a [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict). Jelle Zijlstra wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
