# typing: `typing.TypeAlias`

typing.TypeAlias

Special annotation for explicitly declaring a type alias.

For example:

```python
from typing import TypeAlias

Factors: TypeAlias = list[int]

```

`TypeAlias` proves especially handy on earlier Python releases for annotating aliases built on forward references, given that type checkers may struggle to tell these apart from ordinary variable assignments:

```python
from typing import Generic, TypeAlias, TypeVar

T = TypeVar("T")

# "Box" does not exist yet,
# so we have to use quotes for the forward reference on Python <3.12.
# Using ``TypeAlias`` tells the type checker that this is a type alias declaration,
# not a variable assignment to a string.
BoxOfStrings: TypeAlias = "Box[str]"

class Box(Generic[T]):
    @classmethod
    def make_box_of_strings(cls) -> BoxOfStrings: ...

```

See [**PEP 613**](https://peps.python.org/pep-0613/) for more details.

Added in version 3.10.

Deprecated since version 3.12: `TypeAlias` gives way to the [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statement, which yields instances of `TypeAliasType` and handles forward references natively. Bear in mind that although `TypeAlias` and `TypeAliasType` share a purpose and look alike by name, they are separate things, and `TypeAliasType` is not what `TypeAlias` is an instance of. There is no plan on the books to drop `TypeAlias`, yet shifting over to `type` statements is the recommended path.

[Subject index](INDEX.md) · [Previous](typing-self.md) · [Continue](typing-union-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Special types](typing-any-to-typing-anystr.md)
