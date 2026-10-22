# pickle — Custom Reduction for Types, Functions, and Other Objects

### Custom Reduction for Types, Functions, and Other Objects

Added in version 3.8.

There are times when `dispatch_table` does not give you enough flexibility. In particular, you might want to base pickling on a criterion other than the object's type, or you might want to tailor how functions and classes are pickled.

In such cases, you can subclass the `Pickler` class and supply a `reducer_override()` method. That method may return any reduction tuple (see `__reduce__()`). Alternatively, it may return [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) to fall back on the standard behavior.

When both `dispatch_table` and `reducer_override()` are defined, the `reducer_override()` method takes priority.

Note

To keep performance up, `reducer_override()` might be skipped for these objects: `None`, `True`, `False`, plus exact instances of [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) and [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple).

The following is a straightforward example in which we permit pickling and reconstructing a given class:

```python
import io
import pickle

class MyClass:
    my_attribute = 1

class MyPickler(pickle.Pickler):
    def reducer_override(self, obj):
        """Custom reducer for MyClass."""
        if getattr(obj, "__name__", None) == "MyClass":
            return type, (obj.__name__, obj.__bases__,
                          {'my_attribute': obj.my_attribute})
        else:
            # For any other object, fallback to usual reduction
            return NotImplemented

f = io.BytesIO()
p = MyPickler(f)
p.dump(MyClass)

del MyClass

unpickled_class = pickle.loads(f.getvalue())

assert isinstance(unpickled_class, type)
assert unpickled_class.__name__ == "MyClass"
assert unpickled_class.my_attribute == 1

```

[Subject index](INDEX.md) · [Previous](handling-stateful-objects.md) · [Continue](out-of-band-buffers.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)
