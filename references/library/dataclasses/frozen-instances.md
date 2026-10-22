# dataclasses — Frozen instances

### Frozen instances

Genuinely immutable Python objects cannot be built. You can nonetheless mimic immutability by handing `frozen=True` to the `@dataclass` decorator. When you do, dataclasses attaches [`__setattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setattr__) plus [`__delattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delattr__) methods onto the class, and those methods throw a `FrozenInstanceError` whenever they run.

A small speed cost comes with `frozen=True`: rather than initializing fields by plain assignment, [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) is forced to rely on `object.__setattr__()`.

[Subject index](INDEX.md) · [Previous](init-only-variables.md) · [Continue](inheritance.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md)
