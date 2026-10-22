# module.__class__

module.__class__

For finer-grained tailoring of module behavior (setting attributes, properties, and so on), one can assign the `__class__` attribute of a module object a subclass of [`types.ModuleType`](https://docs.python.org/3.14/library/types.html#types.ModuleType). For instance:

```python
import sys
from types import ModuleType

class VerboseModule(ModuleType):
    def __repr__(self):
        return f'Verbose {self.__name__}'

    def __setattr__(self, attr, value):
        print(f'Setting {attr}...')
        super().__setattr__(attr, value)

sys.modules[__name__].__class__ = VerboseModule

```

Note

Defining a module `__getattr__` and assigning a module `__class__` only touch lookups carried out via the attribute access syntax – reaching the module globals directly (whether through code inside the module, or through a reference to the module’s globals dictionary) stays untouched.

Changed in version 3.5: The `__class__` module attribute is now writable.

Added in version 3.7: The `__getattr__` and `__dir__` module attributes.

See also

[**PEP 562**](https://peps.python.org/pep-0562/) - Module __getattr__ and __dir__

Describes the `__getattr__` and `__dir__` functions on modules.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-attribute-access.md) · [Owning language section](module-getattr-module-dir.md) · [Previous source section](module-getattr-module-dir.md) · [Following source section](implementing-descriptors.md)
