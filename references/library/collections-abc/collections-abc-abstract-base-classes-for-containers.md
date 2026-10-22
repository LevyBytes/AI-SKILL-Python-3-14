# collections.abc — `collections.abc` — Abstract Base Classes for Containers

## collections.abc — Abstract Base Classes for Containers??

### `collections.abc` — Abstract Base Classes for Containers

Added in version 3.3: In earlier releases these definitions lived inside the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module.

**Source code:** [Lib/_collections_abc.py](https://github.com/python/cpython/tree/3.14/Lib/_collections_abc.py)

---

[Abstract base classes](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) that let you check whether a class supplies a given interface are provided by this module — for instance, testing whether something is [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) or whether it is a [mapping](https://docs.python.org/3.14/glossary.html#term-mapping).

There are three ways an [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) or [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) check against an interface can succeed.

1.

A brand-new class may inherit straight from one of the abstract base classes. Such a class is obliged to provide the required abstract methods. The leftover mixin methods arrive through inheritance and can be overridden where wanted. Further methods may also be tacked on as needed:

```python
class C(Sequence):                      # Direct inheritance
    def __init__(self): ...             # Extra method not required by the ABC
    def __getitem__(self, index):  ...  # Required abstract method
    def __len__(self):  ...             # Required abstract method
    def count(self, value): ...         # Optionally override a mixin method

```

```pycon
>>> issubclass(C, Sequence)
True
>>> isinstance(C(), Sequence)
True

```

2.

Both existing classes and built-in classes may be enrolled as "virtual subclasses" of the ABCs. Each such class ought to define the complete API, covering every abstract method together with every mixin method. Doing so lets users count on [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) or [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) checks to confirm the full interface is present. This rule has an exception for methods that get inferred automatically from the rest of the API:

```python
class D:                                 # No inheritance
    def __init__(self): ...              # Extra method not required by the ABC
    def __getitem__(self, index):  ...   # Abstract method
    def __len__(self):  ...              # Abstract method
    def count(self, value): ...          # Mixin method
    def index(self, value): ...          # Mixin method

Sequence.register(D)                     # Register instead of inherit

```

```pycon
>>> issubclass(D, Sequence)
True
>>> isinstance(D(), Sequence)
True

```

Here, class `D` has no need to define `__contains__`, `__iter__`, and `__reversed__`, since the [in-operator](https://docs.python.org/3.14/reference/expressions.html#comparisons), the [iteration](https://docs.python.org/3.14/glossary.html#term-iterable) logic, and the [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed) function each automatically default to relying on `__getitem__` and `__len__`.

3.

A few straightforward interfaces are spotted directly through the presence of the necessary methods (provided those methods haven't been set to [`None`](https://docs.python.org/3.14/library/constants.html#None)):

```python
class E:
    def __iter__(self): ...
    def __next__(self): ...

```

```pycon
>>> issubclass(E, Iterable)
True
>>> isinstance(E(), Iterable)
True

```

This final technique fails for complex interfaces, since an interface amounts to more than merely the presence of method names. Interfaces lay out semantics and relationships among methods that no inspection of specific method names alone can reveal. To illustrate, observing that a class offers `__getitem__`, `__len__`, and `__iter__` does not suffice to tell a `Sequence` apart from a `Mapping`.

Added in version 3.9: These abstract classes now support `[]`. See [Generic Alias Type](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias) and [**PEP 585**](https://peps.python.org/pep-0585/).

[Subject index](INDEX.md) · [Continue](collections-abstract-base-classes.md)
