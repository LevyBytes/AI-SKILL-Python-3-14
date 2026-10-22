# What’s New in Python 2.2 / Descriptors

### Descriptors

Earlier Python releases gave you no uniform means of finding out which attributes and methods an object actually offered. A few loose conventions existed — defining `__members__` and `__methods__` attributes holding lists of names, say — yet the author of an extension type or a class frequently never bothered to set them. You could resort to peering at an object’s [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__), but with class inheritance or some arbitrary `__getattr__()` hook in play this could still mislead you.

The single overarching notion behind the reworked class model is that an API for laying out an object’s attributes by way of *descriptors* has now been made formal. Descriptors pin down an attribute’s value, declaring whether it stands for a method or a field. Thanks to the descriptor API, static methods and class methods become feasible, alongside more unusual constructs.

Attribute descriptors are objects residing inside class objects, and they carry a handful of attributes themselves:

- [`__name__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__name__) is the attribute’s name.

- [`__doc__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__doc__) is the attribute’s docstring.

- `__get__(object)` is a method that retrieves the attribute value from *object*.

- `__set__(object, value)` sets the attribute on *object* to *value*.

- `__delete__(object, value)` deletes the *value* attribute of *object*.

To illustrate, when you write `obj.x`, what Python is really doing under the hood is:

```python
descriptor = obj.__class__.x
descriptor.__get__(obj)

```

In the case of methods, [`descriptor.__get__`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) hands back a short-lived callable object that bundles together the instance plus the method due to run on it. That’s precisely why static methods and class methods can now exist; their descriptors bundle just the method, or the method together with the class. To put these new sorts of methods briefly: static methods receive no instance, which makes them act like plain functions. Class methods get handed the object’s class, though not the object itself. You declare static and class methods this way:

```python
class C(object):
    def f(arg1, arg2):
        ...
    f = staticmethod(f)

    def g(cls, arg1, arg2):
        ...
    g = classmethod(g)

```

The [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod) function accepts the function `f()` and gives it back wrapped inside a descriptor so it can be parked on the class object. One might assume there’d be dedicated syntax for declaring such methods (`def static f`, `defstatic f()`, or the like), but no such syntax exists so far; that’s been set aside for later Python releases.

Other fresh features — slots and properties among them — are likewise built as new kinds of descriptors, and writing a descriptor class that pulls off something inventive isn’t hard. As an example, you could craft a descriptor class that let you express Eiffel-style preconditions and postconditions on a method. A class leaning on such a feature might be written like so:

```python
from eiffel import eiffelmethod

class C(object):
    def f(self, arg1, arg2):
        # The actual function
        ...
    def pre_f(self):
        # Check preconditions
        ...
    def post_f(self):
        # Check postconditions
        ...

    f = eiffelmethod(f, pre_f, post_f)

```

Observe that someone leaning on the new `eiffelmethod()` need grasp nothing about descriptors at all. That’s exactly why I hold that these additions don’t pile fundamental complexity onto the language. A handful of wizards will have to learn the internals so they can build `eiffelmethod()` or the ZODB or whatever else, but the rest will simply write code atop the resulting libraries and never mind the implementation specifics.

[Subject index](INDEX.md) · [Previous source section](old-and-new-classes.md) · [Next source section](multiple-inheritance-the-diamond-rule.md) · [Release/subject declaration](introduction.md)
