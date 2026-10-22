# types: `types.get_original_bases()`

types.get_original_bases(*cls*, */*)

Hand back the tuple of objects that were first supplied as the bases of *cls*, taken before the [`__mro_entries__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__mro_entries__) method ran on any of the bases (per the mechanisms set out in [**PEP 560**](https://peps.python.org/pep-0560/)). This comes in handy when introspecting [Generics](https://docs.python.org/3.14/library/typing.html#user-defined-generics).

When a class carries an `__orig_bases__` attribute, this function returns the value of `cls.__orig_bases__`. When a class lacks the `__orig_bases__` attribute, [`cls.__bases__`](https://docs.python.org/3.14/reference/datamodel.html#type.__bases__) is returned instead.

Examples:

```python
from typing import TypeVar, Generic, NamedTuple, TypedDict

T = TypeVar("T")
class Foo(Generic[T]): ...
class Bar(Foo[int], float): ...
class Baz(list[str]): ...
Eggs = NamedTuple("Eggs", [("a", int), ("b", str)])
Spam = TypedDict("Spam", {"a": int, "b": str})

assert Bar.__bases__ == (Foo, float)
assert get_original_bases(Bar) == (Foo[int], float)

assert Baz.__bases__ == (list,)
assert get_original_bases(Baz) == (list[str],)

assert Eggs.__bases__ == (tuple,)
assert get_original_bases(Eggs) == (NamedTuple,)

assert Spam.__bases__ == (dict,)
assert get_original_bases(Spam) == (TypedDict,)

assert int.__bases__ == (object,)
assert get_original_bases(int) == (object,)

```

Added in version 3.12.

See also

[**PEP 560**](https://peps.python.org/pep-0560/) - Core support for typing module and generic types

[Subject index](INDEX.md) · [Previous](types-new-class-to-types-resolve-bases.md) · [Continue](types-nonetype-class-to-types-asyncgeneratortype.md) · [Owning module, declaration or section: types](types-dynamic-type-creation-and-names-for-built-in-types.md) · [Owning module, declaration or section: Dynamic Type Creation](types-new-class-to-types-resolve-bases.md)
