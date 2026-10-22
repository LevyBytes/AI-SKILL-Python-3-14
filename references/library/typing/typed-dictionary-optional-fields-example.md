# typing — Other special directives — Code example: class Point2D(TypedDict, total=False):

```python
class Point2D(TypedDict, total=False):
    x: Required[int]
    y: Required[int]
    label: str

# Alternative syntax
Point2D = TypedDict('Point2D', {
    'x': Required[int],
    'y': Required[int],
    'label': str
}, total=False)

```

Through the class-based syntax, a `TypedDict` type may inherit from one or several other `TypedDict` types. Usage:

```python
class Point3D(Point2D):
    z: int

```

Three items belong to `Point3D`: `x`, `y` and `z`. That matches the following definition:

```python
class Point3D(TypedDict):
    x: int
    y: int
    z: int

```

Aside from `Generic`, a `TypedDict` is not allowed to inherit from a non-`TypedDict` class. For example:

```python
class X(TypedDict):
    x: int

class Y(TypedDict):
    y: int

class Z(object): pass  # A non-TypedDict class

class XY(X, Y): pass  # OK

class XZ(X, Z): pass  # raises TypeError

```

A `TypedDict` can be generic:

```python
class Group[T](TypedDict):
    key: T
    group: list[T]

```

For a generic `TypedDict` that stays compatible with Python 3.11 or earlier, explicitly inherit from `Generic`:

```python
T = TypeVar("T")

class Group(TypedDict, Generic[T]):
    key: T
    group: list[T]

```

A `TypedDict` lends itself to introspection through [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) (consult [Annotations Best Practices](https://docs.python.org/3.14/howto/annotations.html#annotations-howto) for fuller guidance on annotation best practices) plus the attributes below:

[Subject index](INDEX.md) · [Previous](typing-typeddict-class.md) · [Continue](other-special-directives-typing-typeddict.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: typing.TypedDict](typing-typeddict-class.md) · [Owning module, declaration or section: Other special directives](type-construction-directives.md)
