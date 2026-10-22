# dataclasses — Re-ordering of keyword-only parameters in `__init__()`

### Re-ordering of keyword-only parameters in `__init__()`

Once the set of parameters that [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) requires has been worked out, every keyword-only parameter is shifted so it follows all of the ordinary (non-keyword-only) ones. Python's implementation of keyword-only parameters demands this: they are required to sit after the non-keyword-only parameters.

Within this example the keyword-only fields are `Base.y`, `Base.w`, and `D.t`, whereas `Base.x` together with `D.z` are ordinary fields:

```python
@dataclass
class Base:
    x: Any = 15.0
    _: KW_ONLY
    y: int = 0
    w: int = 1

@dataclass
class D(Base):
    z: int = 10
    t: int = field(kw_only=True, default=0)

```

The `__init__()` that gets synthesized for `D` comes out as:

```python
def __init__(self, x: Any = 15.0, z: int = 10, *, y: int = 0, w: int = 1, t: int = 0):

```

Observe that the parameter sequence differs from the field listing: those originating in ordinary fields come first, trailed by the ones originating in keyword-only fields.

Among the keyword-only parameters themselves, their mutual order is preserved within the rearranged `__init__()` parameter list.

[Subject index](INDEX.md) · [Previous](inheritance.md) · [Continue](default-factory-functions.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md)
