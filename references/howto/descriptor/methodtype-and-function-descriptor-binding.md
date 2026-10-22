# MethodType and Function descriptor binding

### Functions and methods

The object oriented capabilities in Python sit on top of a function based foundation. Non-data descriptors stitch the two together without a seam.

A function held in a class dictionary becomes a method once it is invoked. The only thing setting a method apart from an ordinary function is that the object instance gets placed ahead of the remaining arguments. The instance is conventionally named *self*, though *this* or any other variable name would serve.

You can construct methods by hand using [`types.MethodType`](https://docs.python.org/3.14/library/types.html#types.MethodType), which is approximately the same as:

```python
class MethodType:
    "Emulate PyMethod_Type in Objects/classobject.c"

    def __init__(self, func, obj):
        self.__func__ = func
        self.__self__ = obj

    def __call__(self, *args, **kwargs):
        func = self.__func__
        obj = self.__self__
        return func(obj, *args, **kwargs)

    def __getattribute__(self, name):
        "Emulate method_getset() in Objects/classobject.c"
        if name == '__doc__':
            return self.__func__.__doc__
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        "Emulate method_getattro() in Objects/classobject.c"
        return getattr(self.__func__, name)

    def __get__(self, obj, objtype=None):
        "Emulate method_descr_get() in Objects/classobject.c"
        return self

```

So that methods get built automatically, functions carry a [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) method that binds methods as attributes are accessed. In other words, functions act as non-data descriptors that hand back bound methods during a dotted lookup from an instance. The mechanics look like this:

```python
class Function:
    ...

    def __get__(self, obj, objtype=None):
        "Simulate func_descr_get() in Objects/funcobject.c"
        if obj is None:
            return self
        return MethodType(self, obj)

```

[Subject index](INDEX.md) · [Function descriptors, qualified names and bound-method introspection](function-descriptors-and-bound-method-inspection.md) · [Previous source context](properties.md) · [Following source context](function-descriptors-and-bound-method-inspection.md)
