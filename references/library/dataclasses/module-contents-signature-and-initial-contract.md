# dataclasses — Module contents — Signature and initial contract

### Module contents

`@dataclasses.dataclass(***, *init=True*, *repr=True*, *eq=True*, *order=False*, *unsafe_hash=False*, *frozen=False*, *match_args=True*, *kw_only=False*, *slots=False*, *weakref_slot=False*)`

Acting as a [decorator](https://docs.python.org/3.14/glossary.html#term-decorator), this function attaches generated [special methods](https://docs.python.org/3.14/glossary.html#term-special-method) to classes in the manner laid out below.

To locate `field`s, the `@dataclass` decorator inspects the class. A `field` means a class variable carrying a [type annotation](https://docs.python.org/3.14/glossary.html#term-variable-annotation). Apart from two exceptions covered below, the type given in the variable annotation is never examined by anything within `@dataclass`.

Throughout every generated method, the fields keep the same order in which they were written in the class body.

A range of "dunder" methods, detailed below, will be attached to the class by the `@dataclass` decorator. When one of those methods is already present in the class, what happens then is governed by the relevant parameter, as the documentation below explains. What the decorator hands back is the very class it received; it never builds a fresh class.

When `@dataclass` is applied plainly as a bare decorator without arguments, it behaves as though the default values in this signature were supplied. Put differently, the following three ways of writing `@dataclass` amount to the same thing:

```python
@dataclass
class C:
    ...

@dataclass()
class C:
    ...

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False,
           match_args=True, kw_only=False, slots=False, weakref_slot=False)
class C:
    ...

```

Here are the parameters accepted by `@dataclass`:

- *init*: When true (which is the default), an [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method gets generated.

Should the class already provide its own `__init__()`, this parameter has no effect.

- *repr*: When true (which is the default), a [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) method gets generated. Its produced repr string carries the class name plus the name and repr of every field, following the order they were declared in the class. Any fields flagged as excluded from the repr are left out. As an illustration: `InventoryItem(name='widget', unit_price=3.0, quantity_on_hand=10)`.

Should the class already provide its own `__repr__()`, this parameter has no effect.

- *eq*: When true (which is the default), an [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) method gets generated.

The comparison this method performs works through each field in turn. The two instances being compared have to share the very same type.

Should the class already provide its own `__eq__()`, this parameter has no effect.

Changed in version 3.13: The `__eq__` method now produced compares the fields one at a time (for instance, `self.a == other.a and self.b == other.b`) instead of comparing tuples built from the fields, as earlier releases did.

The comparison runs faster because of this change, yet results can differ wherever attributes are equal by identity but not by value (`float('nan')` being one such case).

Under Python 3.12 and earlier, the comparison happened by assembling tuples out of the fields and comparing those (for example, `(self.a, self.b) == (other.a, other.b)`).

- *order*: When true (where the default is `False`), the methods [`__lt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__), [`__le__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__le__), [`__gt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__gt__), and [`__ge__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__ge__) get generated. They compare the class as though it were a tuple made from its fields, in order. The two instances being compared have to share the very same type. Where *order* is true while *eq* is false, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

Where the class already provides any of `__lt__()`, `__le__()`, `__gt__()`, or `__ge__()`, then [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

- *unsafe_hash*: When true, `dataclasses` is forced to build a [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) method even where doing so may be unsafe. Without it, a `__hash__()` method is generated based on how *eq* and *frozen* have been configured. Its default value is `False`.

The built-in [`hash()`](https://docs.python.org/3.14/library/functions.html#hash) relies on `__hash__()`, as does placing objects into hashed collections like dictionaries and sets. The presence of a `__hash__()` carries the implication that instances of the class are immutable. Mutability is a nuanced property hinging on the programmer's intent, on whether `__eq__()` exists and how it behaves, and on the *eq* and *frozen* flag values passed to the `@dataclass` decorator.

By default, `@dataclass` refrains from silently adding a [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) method except where that is safe. Nor will it add to or alter a `__hash__()` method that was explicitly defined already. Assigning the class attribute `__hash__ = None` carries a particular significance to Python, which the `__hash__()` documentation describes.

Where `__hash__()` has not been explicitly defined, or where it is set to `None`, then `@dataclass` *may* contribute an implicit `__hash__()` method. While discouraged, you are able to force `@dataclass` to build a `__hash__()` method via `unsafe_hash=True`. That could apply where your class is logically immutable yet remains capable of mutation. This is a niche scenario warranting careful thought.

What follows are the rules that govern implicit creation of a `__hash__()` method. Be aware that you cannot simultaneously keep an explicit `__hash__()` method in your dataclass and pass `unsafe_hash=True`; this produces a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Where *eq* and *frozen* are both true, `@dataclass` by default produces a `__hash__()` method on your behalf. Where *eq* is true but *frozen* is false, `__hash__()` becomes `None`, which flags it as unhashable (and it is, given that it is mutable). Where *eq* is false, `__hash__()` is left as is, meaning the superclass `__hash__()` method takes over (and if [`object`](https://docs.python.org/3.14/library/functions.html#object) is that superclass, the result is a fallback to id-based hashing).

- *frozen*: When true (where the default is `False`), any assignment to fields raises an exception. This mimics read-only frozen instances. Refer to the discussion further down.

Where [`__setattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setattr__) or [`__delattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delattr__) is defined in the class while *frozen* is true, then [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

-

[Subject index](INDEX.md) · [Continue](dataclasses-and-per-above.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md)
