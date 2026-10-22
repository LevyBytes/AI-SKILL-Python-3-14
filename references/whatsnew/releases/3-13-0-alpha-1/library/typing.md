# Python 3.13.0 alpha 1 / library / typing

[gh-104797](https://github.com/python/cpython/issues/104797): Permitted [`typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol) classes to derive from [`collections.abc.Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer). Jelle Zijlstra authored the patch.

[gh-105280](https://github.com/python/cpython/issues/105280): Resolved a defect under which `isinstance([], collections.abc.Mapping)` might come out as `True` whenever garbage collection fired at an unlucky moment. That fault traced back to how the [`typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol) implementation was reworked in Python 3.12.

[gh-105144](https://github.com/python/cpython/issues/105144): Addressed a fresh regression inside the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module. Under that regression, writing `class Foo(X, typing.Protocol)`, where `X` named a class carrying [`abc.ABCMeta`](https://docs.python.org/3.14/library/abc.html#abc.ABCMeta) for its metaclass, made later `isinstance(1, X)` calls wrongly throw [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Alex Waygood authored the patch.

[gh-104935](https://github.com/python/cpython/issues/104935): Patched defects in how [`typing.runtime_checkable()`](https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable) and [`typing.Generic`](https://docs.python.org/3.14/library/typing.html#typing.Generic) interact, defects brought in alongside the [**PEP 695**](https://peps.python.org/pep-0695/) implementation. Jelle Zijlstra authored the patch.

[gh-104786](https://github.com/python/cpython/issues/104786): Dropped the kwargs-based path for creating [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict)

[gh-104873](https://github.com/python/cpython/issues/104873): Added [`typing.get_protocol_members()`](https://docs.python.org/3.14/library/typing.html#typing.get_protocol_members), which hands back the member set that defines a [`typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol). Also added [`typing.is_protocol()`](https://docs.python.org/3.14/library/typing.html#typing.is_protocol) for testing whether some class counts as a `typing.Protocol`. Jelle Zijlstra authored the patch.

[gh-104874](https://github.com/python/cpython/issues/104874): Wrote docs covering the `__name__` and `__supertype__` attributes on [`typing.NewType`](https://docs.python.org/3.14/library/typing.html#typing.NewType). Jelle Zijlstra authored the patch.

[gh-106309](https://github.com/python/cpython/issues/106309): Mark [`typing.no_type_check_decorator()`](https://docs.python.org/3.14/library/typing.html#typing.no_type_check_decorator) as deprecated. Not a single major type checker ever backed this decorator. Alex Waygood provided the patch.

[gh-105974](https://github.com/python/cpython/issues/105974): Address a bug where a [`typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol) class holding one or more non-callable members would throw [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) once [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) ran against it, even where a custom `__subclasshook__` method existed. Under Python 3.11 and earlier — now brought back — no `TypeError` was thrown in such cases provided a custom `__subclasshook__` method had been defined. Alex Waygood wrote the patch.

[gh-105570](https://github.com/python/cpython/issues/105570): Mark two ways of building [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) classes carrying 0 fields through the functional syntax as deprecated: `TD = TypedDict("TD")` along with `TD = TypedDict("TD", None)`. Each becomes disallowed in Python 3.15. For a `TypedDict` class holding 0 fields, go with either `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})`.

[gh-109653](https://github.com/python/cpython/issues/109653): Shrink the import time of [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) by roughly a third. Alex Waygood authored the patch.

[gh-92871](https://github.com/python/cpython/issues/92871): Deleted the `typing.io` and `typing.re` namespaces, both deprecated since Python 3.8. Every item remains reachable through the main [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module.

[gh-105566](https://github.com/python/cpython/issues/105566): Mark as deprecated the building of a [`typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) class with keyword arguments standing in for the fields (`NT = NamedTuple("NT", x=int, y=str)`). That route becomes disallowed in Python 3.15. Reach instead for the class-based syntax or the functional syntax.

Likewise two ways of building `NamedTuple` classes holding 0 fields through the functional syntax are deprecated and become disallowed in Python 3.15: `NT = NamedTuple("NT")` along with `NT = NamedTuple("NT", None)`. For a `NamedTuple` class carrying 0 fields, go with either `class NT(NamedTuple): pass` or `NT = NamedTuple("NT", [])`.

[gh-105509](https://github.com/python/cpython/issues/105509): [`typing.Annotated`](https://docs.python.org/3.14/library/typing.html#typing.Annotated) is now built as an instance of `typing._SpecialForm` in place of a class. Anyone relying on the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module public API should see no user-facing change.

[gh-108295](https://github.com/python/cpython/issues/108295): Resolved crashes connected to using weakrefs on [`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar).

[gh-106403](https://github.com/python/cpython/issues/106403): Objects of type [`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar), [`typing.ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec), [`typing.ParamSpecArgs`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpecArgs), [`typing.ParamSpecKwargs`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpecKwargs), and [`typing.TypeVarTuple`](https://docs.python.org/3.14/library/typing.html#typing.TypeVarTuple) can hold weak references once more, which undoes a regression that came in with Python 3.12.0 beta 1. Jelle Zijlstra wrote the patch.

[gh-110682](https://github.com/python/cpython/issues/110682): [`runtime-checkable protocols`](https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable) formerly treated `__match_args__` as a protocol member within `__instancecheck__` whenever it appeared on the protocol. From now on this attribute is disregarded should it be present.

[gh-105578](https://github.com/python/cpython/issues/105578): Mark [`typing.AnyStr`](https://docs.python.org/3.14/library/typing.html#typing.AnyStr) as deprecated, with the newer Type Parameter syntax preferred. Refer to PEP 695.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
