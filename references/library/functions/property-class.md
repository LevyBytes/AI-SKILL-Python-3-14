# Built-in Functions

*class *property(*fget=None*, *fset=None*, *fdel=None*, *doc=None*)

Return a property attribute.

The *fget* parameter is the function that reads an attribute's value, *fset* the one that assigns it, and *fdel* the one that removes it. As for *doc*, it supplies a docstring for the attribute.

One common pattern is wrapping a managed attribute `x`:

```python
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

```

Given that *c* is an instance of *C*, reading `c.x` triggers the getter, assigning `c.x = value` triggers the setter, and `del c.x` triggers the deleter.

When supplied, *doc* serves as the property attribute's docstring. If it isn't, the property inherits a copy of *fget*'s docstring whenever one is present. That behavior lets you define read-only properties with ease by applying `property()` as a [decorator](https://docs.python.org/3.14/glossary.html#term-decorator):

```python
class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

```

Here the `@property` decorator converts the `voltage()` method into a "getter" for an identically named read-only attribute, while assigning the docstring of *voltage* to "Get the current voltage."

 @getter

 @setter

 @deleter

Each property object carries `getter`, `setter`, and `deleter` methods that double as decorators; applying one produces a fresh copy of the property whose matching accessor is now the decorated function. An example makes this clearest:

```python
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

```

What you see here behaves identically to the very first example. Take care to name each added function exactly as the original property was named (`x` here.)

That returned property object additionally exposes the attributes `fget`, `fset`, and `fdel`, matching the constructor's arguments.

Changed in version 3.5: Docstrings belonging to property objects became writeable.

## Property name

__name__

This attribute stores the property's name. That name may be reassigned while the program runs.

Added in version 3.13.

[Builtin task index](INDEX.md).
