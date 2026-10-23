# dataclasses - Inheritance

### Inheritance

As the `@dataclass` decorator constructs the dataclass, it walks every one of the class's parents in reverse MRO order (in other words, beginning from [`object`](https://docs.python.org/3.14/library/functions.html#object)), and whenever it encounters a dataclass it copies that parent's fields into an ordered mapping of fields. Once all the parent fields have been folded in, the class contributes its own fields to that same ordered mapping. Every synthesized method draws on this merged, computed ordered mapping of fields. Since the fields follow insertion order, a subclass shadows its parents. Here is an example:

```python
@dataclass
class Base:
    x: Any = 15.0
    y: int = 0

@dataclass
class C(Base):
    z: int = 10
    x: int = 15

```

The resulting field sequence runs `x`, `y`, `z` in that order. For `x`, the type ends up being [`int`](https://docs.python.org/3.14/library/functions.html#int), matching the declaration in class `C`.

The [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) that gets synthesized for `C` takes the following shape:

```python
def __init__(self, x: int = 15, y: int = 0, z: int = 10):

```

[Subject index](INDEX.md) · [Previous](frozen-instances.md) · [Continue](re-ordering-of-keyword-only-parameters-in-init.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md)
