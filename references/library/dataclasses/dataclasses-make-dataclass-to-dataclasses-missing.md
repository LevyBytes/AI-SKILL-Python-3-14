# dataclasses: `dataclasses.make_dataclass()`, `dataclasses.replace()`, `dataclasses.is_dataclass()`, `dataclasses.MISSING`

`dataclasses.make_dataclass(*cls_name*, *fields*, ***, *bases=()*, *namespace=None*, *init=True*, *repr=True*, *eq=True*, *order=False*, *unsafe_hash=False*, *frozen=False*, *match_args=True*, *kw_only=False*, *slots=False*, *weakref_slot=False*, *module=None*, *decorator=dataclass*)`

Builds a fresh dataclass named *cls_name*, with the fields laid out in *fields*, the base classes provided through *bases*, and set up with a namespace provided through *namespace*. *fields* is an iterable whose elements are each one of `name`, `(name, type)`, or `(name, type, Field)`. Should only `name` appear, [`typing.Any`](https://docs.python.org/3.14/library/typing.html#typing.Any) fills in for `type`. Every one of *init*, *repr*, *eq*, *order*, *unsafe_hash*, *frozen*, *match_args*, *kw_only*, *slots*, and *weakref_slot* keeps whatever meaning it already holds within `@dataclass`.

Where *module* is given, the dataclass `__module__` attribute is set to that value. Otherwise it is set to the module name of whoever called.

The *decorator* parameter is a callable employed to construct the dataclass. Its first positional argument ought to be the class object, with the remaining keyword arguments matching those of `@dataclass`. Absent any override, the chosen callable is the `@dataclass` function.

Strictly speaking this function is not required, because any Python means of creating a new class carrying [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotations__) can then have the `@dataclass` function applied to turn that class into a dataclass. The function is offered for convenience. For instance:

```python
C = make_dataclass('C',
                   [('x', int),
                     'y',
                    ('z', int, field(default=5))],
                   namespace={'add_one': lambda self: self.x + 1})

```

Amounts to the same thing as:

```python
@dataclass
class C:
    x: int
    y: 'typing.Any'
    z: int = 5

    def add_one(self):
        return self.x + 1

```

Added in version 3.14: Added the *decorator* parameter.

 dataclasses.replace(*obj*, */*, ***changes*)

Builds a fresh object of the same type as *obj*, swapping fields for the values found in *changes*. Where *obj* is not a Data Class, raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Where keys in *changes* are not field names belonging to the given dataclass, raises `TypeError`.

The freshly returned object comes about by invoking the dataclass [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method. This guarantees that `__post_init__()`, where present, runs too.

Any init-only variables lacking default values, if there are such, have to be given on the `replace()` call so that they can be forwarded to `__init__()` and `__post_init__()`.

It is an error for *changes* to include any fields declared with `init=False`. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised in that situation.

Take heed of how `init=False` fields behave throughout a `replace()` call. Rather than being copied from the source object, they get initialized inside `__post_init__()`, if they get initialized whatsoever. The expectation is that `init=False` fields will see rare and careful use. Where they are used, it may be prudent to provide alternate class constructors, or perhaps a custom `replace()` (or similarly named) method that takes care of instance copying.

The generic function [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace) also works with dataclass instances.

 dataclasses.is_dataclass(*obj*)

Returns `True` where its parameter is a dataclass (subclasses of a dataclass count, but [generic aliases](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias) do not) or an instance of one; otherwise returns `False`.

Where you need to learn whether a class is an instance of a dataclass (and not a dataclass on its own), tack on an additional check for `not isinstance(obj, type)`:

```python
def is_dataclass_instance(obj):
    return is_dataclass(obj) and not isinstance(obj, type)

```

 dataclasses.MISSING

A sentinel value that marks a missing default or default_factory.

[Subject index](INDEX.md) · [Previous](dataclasses-fields-to-dataclasses-astuple.md) · [Continue](dataclasses-kw-only-to-dataclasses-frozeninstanceerror.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md) · [Owning module, declaration or section: Module contents](module-contents-signature-and-initial-contract.md)
