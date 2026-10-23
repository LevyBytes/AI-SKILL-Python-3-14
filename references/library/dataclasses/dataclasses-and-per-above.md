# dataclasses - Module contents - Contract: *match_args*: When true (where the default is `True`), the `__match_args__` tuple gets assembled from the non keyword-only parameters of the generated `__init__()` method (this holds even where `__init__()` itself is not generated, per above).

*match_args*: When true (where the default is `True`), the [`__match_args__`](https://docs.python.org/3.14/reference/datamodel.html#object.__match_args__) tuple gets assembled from the non keyword-only parameters of the generated [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method (this holds even where `__init__()` itself is not generated, per above). When false, or where `__match_args__` is already defined in the class, no `__match_args__` is generated.

>

Added in version 3.10.

- *kw_only*: When true (where the default value is `False`), every field is then flagged as keyword-only. Flagging a field keyword-only has just one consequence: the [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) parameter that comes from a keyword-only field has to be supplied by keyword whenever `__init__()` runs. Consult the [parameter](https://docs.python.org/3.14/glossary.html#term-parameter) glossary entry for the specifics. See also the `KW_ONLY` section.

`__match_args__` does not include keyword-only fields.

>

Added in version 3.10.

- *slots*: When true (where the default is `False`), a [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__) attribute gets generated and a new class — rather than the original — is returned. Where `__slots__` is already defined in the class, then [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

>

Warning

Handing parameters to a base class [`__init_subclass__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init_subclass__) while using `slots=True` produces a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). As a workaround, either invoke `__init_subclass__` without parameters or rely on default values. The full details live at [gh-91126](https://github.com/python/cpython/issues/91126).

Added in version 3.10.

Changed in version 3.11: Where a field name already appears in the `__slots__` of a base class, the generated `__slots__` leaves it out to avoid [overriding them](https://docs.python.org/3.14/reference/datamodel.html#datamodel-note-slots). For that reason, do not reach for `__slots__` to obtain the field names of a dataclass. Reach for `fields()` instead. So that inherited slots can be worked out, a base class `__slots__` may be any iterable, though *not* an iterator.

- *weakref_slot*: When true (where the default is `False`), it adds a slot called "__weakref__", which is needed to render an instance [`weakref-able`](https://docs.python.org/3.14/library/weakref.html#weakref.ref). Specifying `weakref_slot=True` while leaving out `slots=True` is an error.

>

Added in version 3.11.

`field`s are allowed to declare a default value, written with ordinary Python syntax:

```python
@dataclass
class C:
    a: int       # 'a' has no default value
    b: int = 0   # assign a default value for 'b'

```

For this example, the added [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method will take in both `a` and `b`, and that method will read as:

```python
def __init__(self, a: int, b: int = 0):

```

A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) gets raised whenever a field lacking a default value comes after a field that has one. That applies regardless of whether it happens inside one class or arises through class inheritance.

[Subject index](INDEX.md) · [Previous](module-contents-signature-and-initial-contract.md) · [Continue](dataclasses-field.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md) · [Owning module, declaration or section: Module contents](module-contents-signature-and-initial-contract.md) · [Owning module, declaration or section: @dataclasses.dataclass](module-contents-signature-and-initial-contract.md)
