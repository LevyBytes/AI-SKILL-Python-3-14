# Static methods

### Static methods

The underlying function comes back unmodified from a static method. Invoking `c.f` or `C.f` amounts to a direct lookup of `object.__getattribute__(c, "f")` or `object.__getattribute__(C, "f")`. The upshot is that the function stays equally reachable whether from an object or a class.

Methods that never touch the `self` variable make solid candidates for being static methods.

Take, for example, a statistics package that bundles a container class for experimental data. That class offers regular methods that compute the average, mean, median, and other descriptive statistics tied to the data. Yet some handy functions are conceptually related while standing apart from the data. As one case, `erf(x)` is a useful conversion routine that shows up in statistical work without leaning on any particular dataset. You can invoke it from either an object or the class: `s.erf(1.5) --> 0.9332` or `Sample.erf(1.5) --> 0.9332`.

Because static methods give back the underlying function untouched, the sample calls are nothing to write home about:

```python
class E:
    @staticmethod
    def f(x):
        return x * 10

```

```pycon
>>> E.f(3)
30
>>> E().f(3)
30

```

Leaning on the non-data descriptor protocol, a pure Python rendition of [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod) would read like this:

```python
import functools

class StaticMethod:
    "Emulate PyStaticMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f
        functools.update_wrapper(self, f)

    def __get__(self, obj, objtype=None):
        return self.f

    def __call__(self, *args, **kwds):
        return self.f(*args, **kwds)

    @property
    def __annotations__(self):
        return self.f.__annotations__

```

Invoking [`functools.update_wrapper()`](https://docs.python.org/3.14/library/functools.html#functools.update_wrapper) attaches a `__wrapped__` attribute pointing at the underlying function. On top of that, it propagates the attributes that make the wrapper resemble the wrapped function, among them [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#function.__name__), [`__qualname__`](https://docs.python.org/3.14/reference/datamodel.html#function.__qualname__), and [`__doc__`](https://docs.python.org/3.14/reference/datamodel.html#function.__doc__).

[Subject index](INDEX.md) · [Previous source context](kinds-of-methods.md) · [Following source context](class-methods.md)
