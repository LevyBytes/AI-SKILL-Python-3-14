# typing - Functions and decorators - Signature and initial contract

@typing.dataclass_transform(***, *eq_default=True*, *order_default=False*, *kw_only_default=False*, *frozen_default=False*, *field_specifiers=()*, ***kwargs*)

Decorator to mark an object as providing [`dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass)-like behavior.

You can apply `dataclass_transform` to a class, a metaclass, or a function that acts as a decorator. Seeing `@dataclass_transform()` informs a static type checker that the object it decorates carries out runtime "magic" reshaping a class much like [`@dataclasses.dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass) does.

Example usage with a decorator function:

```python
@dataclass_transform()
def create_model[T](cls: type[T]) -> type[T]:
    ...
    return cls

@create_model
class CustomerModel:
    id: int
    name: str

```

On a base class:

```python
@dataclass_transform()
class ModelBase: ...

class CustomerModel(ModelBase):
    id: int
    name: str

```

On a metaclass:

```python
@dataclass_transform()
class ModelMeta(type): ...

class ModelBase(metaclass=ModelMeta): ...

class CustomerModel(ModelBase):
    id: int
    name: str

```

Type checkers will handle each `CustomerModel` shown above much as they handle classes built with [`@dataclasses.dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass). To illustrate, a type checker will presume these classes carry `__init__` methods taking `id` and `name`.

The decorated class, metaclass, or function is allowed to take the following bool arguments, which type checkers will treat as having the same impact they have on the [`@dataclasses.dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass) decorator: `init`, `eq`, `order`, `unsafe_hash`, `frozen`, `match_args`, `kw_only`, and `slots`. Each argument's value (`True` or `False`) has to be resolvable statically.

Supplying arguments to the `dataclass_transform` decorator lets you tailor the default behaviors of the decorated class, metaclass, or function:

Parameters:

- **eq_default** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – States the value, `True` or `False`, taken for `eq` when a caller leaves it out. Defaults to `True`.

- **order_default** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – States the value, `True` or `False`, taken for `order` when a caller leaves it out. Defaults to `False`.

- **kw_only_default** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – States the value, `True` or `False`, taken for `kw_only` when a caller leaves it out. Defaults to `False`.

- **frozen_default** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) –

States the value, `True` or `False`, taken for `frozen` when a caller leaves it out. Defaults to `False`.

Added in version 3.12.

- **field_specifiers** ([*tuple*](https://docs.python.org/3.14/library/stdtypes.html#tuple)*[*[*Callable*](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Callable)*[**...**, **Any**]**, **...**]*) – Names a fixed roster of allowed classes or functions that act as field descriptors, in the spirit of [`dataclasses.field()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.field). Defaults to `()`.

- ****kwargs** (*Any*) – Any further keyword arguments are tolerated so that future extensions remain possible.

[Subject index](INDEX.md) · [Previous](typing-reveal-type.md) · [Continue](dataclass-field-specifier-options.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Functions and decorators](typing-cast-to-typing-assert-never.md)
