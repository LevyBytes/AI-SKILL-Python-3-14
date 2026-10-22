# Class methods

### Class methods

In contrast to static methods, class methods slip the class reference onto the front of the argument list ahead of the function call. The pattern stays identical regardless of whether the caller happens to be an object or a class:

```python
class F:
    @classmethod
    def f(cls, x):
        return cls.__name__, x

```

```pycon
>>> F.f(3)
('F', 3)
>>> F().f(3)
('F', 3)

```

Such behavior pays off whenever a method needs nothing more than a class reference and stays independent of data kept in any one instance. Building alternate class constructors is one application of class methods. As an illustration, the classmethod [`dict.fromkeys()`](https://docs.python.org/3.14/library/stdtypes.html#dict.fromkeys) produces a fresh dictionary out of a list of keys. Its pure Python counterpart is:

```python
class Dict(dict):
    @classmethod
    def fromkeys(cls, iterable, value=None):
        "Emulate dict_fromkeys() in Objects/dictobject.c"
        d = cls()
        for key in iterable:
            d[key] = value
        return d

```

You can now build a fresh dictionary of unique keys in this manner:

```pycon
>>> d = Dict.fromkeys('abracadabra')
>>> type(d) is Dict
True
>>> d
{'a': None, 'b': None, 'r': None, 'c': None, 'd': None}

```

Relying on the non-data descriptor protocol, a pure Python form of [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) would look as follows:

```python
import functools

class ClassMethod:
    "Emulate PyClassMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f
        functools.update_wrapper(self, f)

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)
        return MethodType(self.f, cls)

```

Inside `ClassMethod`, the [`functools.update_wrapper()`](https://docs.python.org/3.14/library/functools.html#functools.update_wrapper) call attaches a `__wrapped__` attribute that points at the underlying function. It likewise propagates the attributes that let the wrapper mimic the wrapped function: [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#function.__name__), [`__qualname__`](https://docs.python.org/3.14/reference/datamodel.html#function.__qualname__), [`__doc__`](https://docs.python.org/3.14/reference/datamodel.html#function.__doc__), and [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#function.__annotations__).

[Subject index](INDEX.md) · [Previous source context](static-methods.md) · [Following source context](slots-reject-misspellings-and-enable-immutable-attributes.md)
