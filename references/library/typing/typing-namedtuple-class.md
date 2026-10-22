# typing: `typing.NamedTuple`

*class *typing.NamedTuple

Typed version of [`collections.namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple).

Usage:

```python
class Employee(NamedTuple):
    name: str
    id: int

```

This is equivalent to:

```python
Employee = collections.namedtuple('Employee', ['name', 'id'])

```

Supply a default for a field by assigning to it within the body of the class:

```python
class Employee(NamedTuple):
    name: str
    id: int = 3

employee = Employee('Guido')
assert employee.id == 3

```

Any field that has a default value must be placed after every field that lacks one.

You can fetch the per-field types by calling [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) on the produced class. (The `_fields` attribute holds the field names and the `_field_defaults` attribute holds the default values; both belong to the [`namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) API.)

Docstrings and methods are also allowed on `NamedTuple` subclasses:

```python
class Employee(NamedTuple):
    """Represents an employee."""
    name: str
    id: int = 3

    def __repr__(self) -> str:
        return f'<Employee {self.name}, id={self.id}>'

```

`NamedTuple` subclasses can be generic:

```python
class Group[T](NamedTuple):
    key: T
    group: list[T]

```

Backward-compatible usage:

```python
# For creating a generic NamedTuple on Python 3.11
T = TypeVar("T")

class Group(NamedTuple, Generic[T]):
    key: T
    group: list[T]

# A functional syntax is also supported
Employee = NamedTuple('Employee', [('name', str), ('id', int)])

```

Changed in version 3.6: The [**PEP 526**](https://peps.python.org/pep-0526/) variable annotation syntax became supported.

Changed in version 3.6.1: Default values, methods, and docstrings became supported.

Changed in version 3.8: Rather than being `OrderedDict` instances, the `_field_types` and `__annotations__` attributes are now ordinary dictionaries.

Changed in version 3.9: The `_field_types` attribute was dropped in favor of the more standard `__annotations__` attribute, which carries the same information.

Changed in version 3.9: `NamedTuple` became a function instead of a class. As shown above, it can still serve as a class base.

Changed in version 3.11: Generic namedtuples became supported.

Changed in version 3.14: Within methods of `NamedTuple` subclasses, calling [`super()`](https://docs.python.org/3.14/library/functions.html#super) (along with the `__class__` [closure variable](https://docs.python.org/3.14/glossary.html#term-closure-variable)) is not supported and raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Deprecated since version 3.13, will be removed in version 3.15: Building NamedTuple classes with the undocumented keyword-argument form (`NT = NamedTuple("NT", x=int)`) is deprecated and becomes disallowed in 3.15. Reach for the class-based syntax or the functional syntax in its place.

Deprecated since version 3.13, will be removed in version 3.15: With the functional syntax for creating a NamedTuple class, omitting a value for the 'fields' parameter (`NT = NamedTuple("NT")`) is deprecated. Likewise, supplying `None` for the 'fields' parameter (`NT = NamedTuple("NT", None)`) is deprecated. Python 3.15 will reject both. For a NamedTuple class holding 0 fields, write `class NT(NamedTuple): pass` or `NT = NamedTuple("NT", [])`.

[Subject index](INDEX.md) · [Previous](type-construction-directives.md) · [Continue](typing-newtype-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Other special directives](type-construction-directives.md)
