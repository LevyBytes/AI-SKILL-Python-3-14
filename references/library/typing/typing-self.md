# typing: `typing.Self`

typing.Self

Special type to represent the current enclosed class.

For example:

```python
from typing import Self, reveal_type

class Foo:
    def return_self(self) -> Self:
        ...
        return self

class SubclassOfFoo(Foo): pass

reveal_type(Foo().return_self())  # Revealed type is "Foo"
reveal_type(SubclassOfFoo().return_self())  # Revealed type is "SubclassOfFoo"

```

Semantically this annotation matches the following, only expressed far more compactly:

```python
from typing import TypeVar

Self = TypeVar("Self", bound="Foo")

class Foo:
    def return_self(self: Self) -> Self:
        ...
        return self

```

As a rule, whenever something hands back `self`, like in the examples above, reach for `Self` as the return annotation. Had `Foo.return_self` instead been annotated to return `"Foo"`, the type checker would treat the object coming out of `SubclassOfFoo.return_self` as type `Foo` rather than `SubclassOfFoo`.

Other common use cases include:

- [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod)s acting as alternative constructors that yield instances of whatever the `cls` parameter denotes.

- Annotating an [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method which returns self.

Avoid using `Self` for the return annotation when the method offers no guarantee of returning a subclass instance once the class gets subclassed:

```python
class Eggs:
    # Self would be an incorrect return annotation here,
    # as the object returned is always an instance of Eggs,
    # even in subclasses
    def returns_eggs(self) -> "Eggs":
        return Eggs()

```

See [**PEP 673**](https://peps.python.org/pep-0673/) for more details.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](typing-literalstring-to-typing-noreturn.md) · [Continue](typing-typealias.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Special types](typing-any-to-typing-anystr.md)
