# Python 3.14.0 alpha 1 / library / dataclasses

[gh-123935](https://github.com/python/cpython/issues/123935): Repairs parent-slot detection for dataclasses descending from classes that carry `__dictoffset__`.

[gh-113878](https://github.com/python/cpython/issues/113878): A *doc* parameter is added to [`dataclasses.field()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.field), letting a value be kept and surfaced as documentation / metadata. When `@dataclass(slots=True)` applies, that string lands in the [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__) dict. If not, the string only shows up on the matching [`dataclasses.Field`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.Field) object.

To make this work, the `__slots__` representation in dataclasses shifts from a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) to a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) whenever documentation / metadata exists.

[gh-118974](https://github.com/python/cpython/issues/118974): Introduce a `decorator` parameter on [`dataclasses.make_dataclass()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.make_dataclass) so callers can tailor how dataclasses are built functionally.

[gh-119180](https://github.com/python/cpython/issues/119180): While implementing [**PEP 649**](https://peps.python.org/pep-0649/) together with [**PEP 749**](https://peps.python.org/pep-0749/), introduce a fresh module named `annotationlib`. Also add handling for unresolved forward references within annotations across [`dataclasses`](https://docs.python.org/3.14/library/dataclasses.html#module-dataclasses), [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict), and [`typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple).

[gh-124176](https://github.com/python/cpython/issues/124176): Brings [`dataclasses.dataclass()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass) support to [`unittest.mock.create_autospec()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.create_autospec). From here on `create_autospec` looks for candidate dataclasses and calls the [`dataclasses.fields()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.fields) function to gather the spec data.

[gh-90562](https://github.com/python/cpython/issues/90562): Adjusts dataclasses so that a zero-argument super() works whenever `slots=True` is given. The mechanism is to rewrite every reference to `__class__` so it targets the freshly minted class.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
