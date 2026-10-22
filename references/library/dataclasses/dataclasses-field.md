# dataclasses: `dataclasses.field()`

`dataclasses.field(***, *default=MISSING*, *default_factory=MISSING*, *init=True*, *repr=True*, *hash=None*, *compare=True*, *metadata=None*, *kw_only=MISSING*, *doc=None*)`

For the ordinary, straightforward use cases, nothing further is needed. Certain dataclass features, however, call for extra per-field detail. To supply that extra detail, you can swap out the plain field default value for a call to the `field()` function provided. For instance:

```python
@dataclass
class C:
    mylist: list[int] = field(default_factory=list)

c = C()
c.mylist += [1, 2, 3]

```

As the example above demonstrates, the `MISSING` value serves as a sentinel object that detects whether the user has supplied certain parameters. This sentinel exists because `None` is itself a legitimate value carrying a separate meaning for some parameters. The `MISSING` value should never be referenced directly by any code.

Here are the parameters accepted by `field()`:

- *default*: When supplied, this becomes the default value for this field. It is necessary because the `field()` call itself takes over the spot the default value would normally occupy.

- *default_factory*: When supplied, it has to be a zero-argument callable invoked whenever a default value is required for this field. One of its uses, among others, is to declare fields whose default values are mutable, as covered below. Supplying both *default* and *default_factory* is an error.

- *init*: When true (the default), this field appears as a parameter on the generated [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method.

- *repr*: When true (the default), this field shows up in the string the generated [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) method returns.

- *hash*: This may be a bool or `None`. When true, this field is folded into the generated [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) method. When false, this field is kept out of the generated `__hash__()`. When `None` (the default), the value of *compare* is used: that would ordinarily be the behavior you want, since a field belongs in the hash whenever it serves comparisons. Setting this to anything besides `None` is discouraged.

A conceivable reason to choose `hash=False` together with `compare=True` is where computing a hash value for a field is costly, that field is required for equality checks, and other fields already feed the type's hash value. Even where a field is left out of the hash, it still factors into comparisons.

- *compare*: When true (the default), this field is folded into the generated equality and comparison methods ([`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__), [`__gt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__gt__), et al.).

- *metadata*: This may be a mapping or `None`. A `None` is handled as an empty dict. The value is wrapped inside [`MappingProxyType()`](https://docs.python.org/3.14/library/types.html#types.MappingProxyType) to render it read-only, then surfaced on the `Field` object. Data Classes makes no use of it whatsoever; it exists as a hook for third-party extensions. Several third-parties can each claim their own key, treating it as a namespace within the metadata.

- *kw_only*: When true, this field gets flagged as keyword-only. This comes into play while the parameters of the generated [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method are being worked out.

`__match_args__` likewise leaves out keyword-only fields.

>

Added in version 3.10.

- *doc*: an optional docstring for this field.

>

Added in version 3.14.

Where the default value of a field comes from a `field()` call, the class attribute for that field will be swapped out for the *default* value specified. Where *default* was not supplied, the class attribute gets deleted instead. The aim is that once the `@dataclass` decorator has run, every class attribute will hold the default values for the fields, exactly as though the default value itself had been written out. For instance, after:

```python
@dataclass
class C:
    x: int
    y: int = field(repr=False)
    z: int = field(repr=False, default=10)
    t: int = 20

```

The class attribute `C.z` is `10`, the class attribute `C.t` is `20`, while the class attributes `C.x` and `C.y` go unset.

[Subject index](INDEX.md) · [Previous](dataclasses-and-per-above.md) · [Continue](dataclasses-field-class.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md) · [Owning module, declaration or section: Module contents](module-contents-signature-and-initial-contract.md)
