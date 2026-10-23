# dataclasses - Post-init processing

Thrown whenever an automatically supplied [`__setattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setattr__) or [`__delattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delattr__) runs against a dataclass declared using `frozen=True`. This exception derives from [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

### Post-init processing

 dataclasses.__post_init__()

If this method is present on the class, the synthesized [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) invokes it, typically through the `self.__post_init__()` form. Should the class declare any `InitVar` fields, though, those values are forwarded to `__post_init__()` following the sequence in which they appear in the class body. When no `__init__()` method gets synthesized, `__post_init__()` is left uncalled.

One of its handy applications is computing field values that are derived from the value of one or several other fields. To illustrate:

```python
@dataclass
class C:
    a: float
    b: float
    c: float = field(init=False)

    def __post_init__(self):
        self.c = self.a + self.b

```

The [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) that `@dataclass` produces never invokes the `__init__()` of any parent class. Where a parent defines an `__init__()` that needs invoking, the usual practice is to route that invocation through a `__post_init__()` method:

```python
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

@dataclass
class Square(Rectangle):
    side: float

    def __post_init__(self):
        super().__init__(self.side, self.side)

```

Keep in mind, though, that the `__init__()` synthesized for a dataclass usually requires no such manual call, because a subclassed dataclass already initializes every field belonging to any parent that is itself a dataclass.

Consult the init-only variables material further down for techniques to feed arguments into `__post_init__()`. The note covering the way `replace()` treats `init=False` fields is also worth reviewing.

[Subject index](INDEX.md) · [Continue](class-variables.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md) · [Owning module, declaration or section: dataclasses.FrozenInstanceError](dataclasses-kw-only-to-dataclasses-frozeninstanceerror.md) · [Preceding source contract and version conditions](dataclasses-kw-only-to-dataclasses-frozeninstanceerror.md)
