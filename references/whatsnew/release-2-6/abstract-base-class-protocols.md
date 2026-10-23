# What’s New in Python 2.6 / PEP 3119: Abstract Base Classes - abc, collections

### PEP 3119: Abstract Base Classes

Certain object-oriented languages, Java among them, offer interfaces that declare a class to carry a particular set of methods or to honor a particular access protocol. For Python, Abstract Base Classes (ABCs) fill that same role. The machinery behind ABCs is made up of an [`abc`](https://docs.python.org/3.14/library/abc.html#module-abc) module that holds a metaclass named [`ABCMeta`](https://docs.python.org/3.14/library/abc.html#abc.ABCMeta), special-case treatment of that metaclass within the [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) and [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) builtins, plus a set of foundational ABCs that the Python developers expect to see broad use. Later Python releases are likely to introduce additional ABCs.

Suppose you hold some class in hand and want to determine whether it permits dictionary-style access. Yet the term “dictionary-style” is imprecise. Likely it means that fetching items via `obj[1]` functions. Does that also require setting items via `obj[2] = value` to function? Or that the object exposes `keys()`, `values()`, and `items()` methods? And the iterator-flavored ones like `iterkeys()`? `copy()` and `update()`? Looping over the object via `iter()`?

The [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module in Python 2.6 ships several distinct ABCs that capture these very distinctions. `Iterable` signals that a class supplies [`__iter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__iter__), while `Container` indicates the class supplies a [`__contains__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__contains__) method and consequently handles `x in y` expressions. The `MutableMapping` ABC specifies the core dictionary interface: fetching items, setting items, and `keys()`, `values()`, and `items()`.

To signal that your own classes honor a given ABC’s interface, you can subclass that ABC:

```python
import collections

class Storage(collections.MutableMapping):
    ...

```

As an alternative, you might define the class without subclassing the chosen ABC, then enroll the class by invoking the ABC’s [`register()`](https://docs.python.org/3.14/library/abc.html#abc.ABCMeta.register) method:

```python
import collections

class Storage:
    ...

collections.MutableMapping.register(Storage)

```

When the class is one you author, subclassing the ABC tends to read more clearly. The [`register()`](https://docs.python.org/3.14/library/abc.html#abc.ABCMeta.register) method comes in handy once you’ve authored a fresh ABC that fits an existing type or class, or when you wish to assert that some third-party class fulfills an ABC. Say you had defined a `PrintableType` ABC; it would then be valid to write:

```python
# Register Python's types
PrintableType.register(int)
PrintableType.register(float)
PrintableType.register(str)

```

A class ought to honor the semantics an ABC lays out, yet Python has no way to verify that; the responsibility falls on the class author to grasp the ABC’s expectations and code to them.

To test whether an object honors a given interface, you may now write:

```python
def func(d):
    if not isinstance(d, collections.MutableMapping):
        raise ValueError("Mapping object expected, not %r" % d)

```

Don’t take this to mean you should now scatter checks like the one above throughout your code. Duck-typing runs deep in Python, where the convention is to skip explicit type checks entirely and simply invoke methods on an object, relying on those methods to exist and letting an exception surface when they don’t. Apply ABC checks sparingly, only where they are truly indispensable.

To craft your own ABCs, set `abc.ABCMeta` as the metaclass within a class definition:

```python
from abc import ABCMeta, abstractmethod

class Drawable():
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self, x, y, scale=1.0):
        pass

    def draw_doubled(self, x, y):
        self.draw(x, y, scale=2.0)

class Square(Drawable):
    def draw(self, x, y, scale):
        ...

```

Within the `Drawable` ABC shown above, the `draw_doubled()` method draws the object at double scale and can be built out of the other methods defined on `Drawable`. As a result, classes that realize this ABC need not supply their own `draw_doubled()`, although they may. A `draw()` implementation, however, is required; the ABC has no useful generic version to offer.

Decorating methods like `draw()` with the [`@~abc.abstractmethod`](https://docs.python.org/3.14/library/abc.html#abc.abstractmethod) decorator marks them as mandatory to implement; Python then raises an exception for any class that omits the method. Keep in mind the exception fires only at the moment you actually attempt to instantiate a subclass that is missing the method:

[Subject index](INDEX.md) · [Previous source section](pep-3118-revised-buffer-protocol.md) · [Next source section](pep-3119-abstract-base-classes-readonly.md) · [Release/subject declaration](python-3-0.md)
