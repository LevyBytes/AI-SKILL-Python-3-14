# dataclasses - Default factory functions

### Default factory functions

Whenever a `field()` declares a *default_factory*, that callable runs with no arguments at the point a default for the field becomes necessary. To produce a fresh list instance, for instance, write:

```python
mylist: list = field(default_factory=list)

```

Should a field be kept out of [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) (via `init=False`) while still declaring a *default_factory*, the synthesized `__init__()` function invariably invokes that factory. The reason is that nothing else remains by which the field could receive a starting value.

[Subject index](INDEX.md) · [Previous](re-ordering-of-keyword-only-parameters-in-init.md) · [Continue](mutable-default-values.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md)
