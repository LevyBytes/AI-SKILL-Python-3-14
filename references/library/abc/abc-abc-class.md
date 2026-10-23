# abc: `abc.ABC`

## abc - Abstract Base Classes

### `abc` - Abstract Base Classes

**Source code:** [Lib/abc.py](https://github.com/python/cpython/tree/3.14/Lib/abc.py)

---

This module supplies the machinery for declaring [abstract base classes](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) (ABCs) in Python, along the lines set out in [**PEP 3119**](https://peps.python.org/pep-3119/); the PEP explains the motivation for adding this to Python. (Take a look as well at [**PEP 3141**](https://peps.python.org/pep-3141/) and the [`numbers`](https://docs.python.org/3.14/library/numbers.html#module-numbers) module for an ABC-based type hierarchy covering numbers.)

Within the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module live several concrete classes built on ABCs, and those too can naturally be subclassed further. On top of that, the [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc) submodule holds ABCs you can use to check whether a class or instance offers some specific interface — say, whether it is [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) or whether it is a [mapping](https://docs.python.org/3.14/glossary.html#term-mapping).

For declaring ABCs this module gives you the metaclass `ABCMeta`, plus a helper class `ABC` that lets you instead declare ABCs by way of inheritance:

 *class *abc.ABC

A helper class whose metaclass is `ABCMeta`. Thanks to it, you can build an abstract base class just by subclassing `ABC`, sidestepping the occasionally puzzling metaclass syntax, for example:

```python
from abc import ABC

class MyABC(ABC):
    pass

```

Bear in mind that `ABC` still has `ABCMeta` as its type, so subclassing `ABC` calls for the same care you would take with any metaclass, since multiple inheritance can spark metaclass conflicts. You may equally declare an abstract base class by handing over the metaclass keyword and reaching for `ABCMeta` directly, for example:

```python
from abc import ABCMeta

class MyABC(metaclass=ABCMeta):
    pass

```

Added in version 3.4.

[Subject index](INDEX.md) · [Continue](abc-abcmeta-class-to-abc-abcmeta-subclasshook.md)
