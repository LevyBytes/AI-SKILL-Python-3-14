# typing: `typing.Generic`

#### Building generic types and type aliases

You should not reach for the classes below directly as annotations. What they are meant for is to serve as building blocks when you assemble generic types and type aliases.

Special syntax can produce these objects ([type parameter lists](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) and the [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statement). To remain compatible with Python 3.11 and earlier, they may instead be produced without that dedicated syntax, as shown below.

 *class *typing.Generic

Abstract base class for generic types.

You usually declare a generic type by appending a list of type parameters following the class name:

```python
class Mapping[KT, VT]:
    def __getitem__(self, key: KT) -> VT:
        ...
        # Etc.

```

A class like this implicitly inherits from `Generic`. The [Language Reference](https://docs.python.org/3.14/reference/compound_stmts.html#generic-classes) covers the runtime semantics of this syntax.

You can then put this class to work as shown:

```python
def lookup_name[X, Y](mapping: Mapping[X, Y], key: X, default: Y) -> Y:
    try:
        return mapping[key]
    except KeyError:
        return default

```

In this case the brackets following the function name mark a [generic function](https://docs.python.org/3.14/reference/compound_stmts.html#generic-functions).

To preserve backwards compatibility, you can still declare generic classes by inheriting from `Generic` explicitly. With that approach, the type parameters have to be declared on their own:

```python
KT = TypeVar('KT')
VT = TypeVar('VT')

class Mapping(Generic[KT, VT]):
    def __getitem__(self, key: KT) -> VT:
        ...
        # Etc.

```

[Subject index](INDEX.md) · [Previous](typing-unpack.md) · [Continue](typing-typevar-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
