# Special Attributes of `GenericAlias` objects

#### Special Attributes of `GenericAlias` objects

Every parameterized generic exposes a set of special read-only attributes.

 genericalias.__origin__

This attribute refers back to the generic class in its non-parameterized form:

```python
>>> list[int].__origin__
<class 'list'>

```

 genericalias.__args__

The value here is a `tuple` (which can have just one element) holding the generic types that were handed to the originating [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__) of the generic class:

```python
>>> dict[str, list[int]].__args__
(<class 'str'>, list[int])

```

 genericalias.__parameters__

The value here is a tuple computed on demand (and possibly empty) of the distinct type variables that appear in `__args__`:

```python
>>> from typing import TypeVar

>>> T = TypeVar('T')
>>> list[T].__parameters__
(~T,)

```

Note

After substitution a `GenericAlias` object carrying [`typing.ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec) parameters might end up with an inaccurate `__parameters__`, because `typing.ParamSpec` is meant chiefly for static type checking.

 genericalias.__unpacked__

A boolean whose value is true when the alias was unpacked through the `*` operator (refer to [`TypeVarTuple`](https://docs.python.org/3.14/library/typing.html#typing.TypeVarTuple)).

Added in version 3.11.

See also

[**PEP 484**](https://peps.python.org/pep-0484/) - Type Hints

Presenting Python’s mechanism for type annotations.

[**PEP 585**](https://peps.python.org/pep-0585/) - Type Hinting Generics In Standard Collections

Presenting the option to parameterize standard-library classes directly, so long as they define the special class method [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__).

[Generics](https://docs.python.org/3.14/library/typing.html#generics), [user-defined generics](https://docs.python.org/3.14/library/typing.html#user-defined-generics) and [`typing.Generic`](https://docs.python.org/3.14/library/typing.html#typing.Generic)

Guidance covering how to write generic classes that accept runtime parameterization and remain legible to static type-checkers.

Added in version 3.9.

[Subject index](INDEX.md) · [Previous](shelve-shelf-to-weakref-weakvaluedictionary.md) · [Continue](union-type.md)
