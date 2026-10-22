# Properties

### Properties

A call to [`property()`](https://docs.python.org/3.14/library/functions.html#property) is a compact way to construct a data descriptor whose access to an attribute fires off a function call. Here is the signature:

```python
property(fget=None, fset=None, fdel=None, doc=None) -> property

```

Documentation illustrates a common pattern that defines a managed attribute `x`:

```python
class C:
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, "I'm the 'x' property.")

```

For a look at how [`property()`](https://docs.python.org/3.14/library/functions.html#property) maps onto the descriptor protocol, the pure Python equivalent below reproduces most of the central functionality:

```python
class Property:
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __set_name__(self, owner, name):
        self.__name__ = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)

```

The [`property()`](https://docs.python.org/3.14/library/functions.html#property) builtin proves useful any time an interface has already exposed direct attribute access and a later change demands that a method step in.

Consider a spreadsheet class that exposes a cell's value via `Cell('b10').value`. Later refinements to the program demand recalculating the cell on each access; yet the programmer would rather not disturb the existing client code that reaches the attribute directly. The remedy is to route access to the value attribute through a property data descriptor:

```python
class Cell:
    ...

    @property
    def value(self):
        "Recalculate the cell before returning value"
        self.recalc()
        return self._value

```

For this example, the built-in [`property()`](https://docs.python.org/3.14/library/functions.html#property) and our `Property()` equivalent both do the job.

[Subject index](INDEX.md) · [Previous source context](pure-python-equivalents.md) · [Following source context](methodtype-and-function-descriptor-binding.md)
