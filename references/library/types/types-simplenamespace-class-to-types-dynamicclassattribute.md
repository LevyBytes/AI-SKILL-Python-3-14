# types - Additional Utility Classes and Functions

### Additional Utility Classes and Functions

 *class *types.SimpleNamespace

A plain [`object`](https://docs.python.org/3.14/library/functions.html#object) subclass granting attribute access to its namespace, plus a meaningful repr.

In contrast to [`object`](https://docs.python.org/3.14/library/functions.html#object), `SimpleNamespace` lets you add attributes and take them away.

A `SimpleNamespace` object can be initialized just as a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) is: with keyword arguments, with one positional argument, or with both at once. Initializing with keyword arguments deposits those straight into the underlying namespace. Initializing instead with a positional argument refreshes the underlying namespace using key-value pairs taken from that argument (either a mapping object or an [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) object that yields key-value pairs). Every such key has to be a string.

This type corresponds roughly to the code below:

```python
class SimpleNamespace:
    def __init__(self, mapping_or_iterable=(), /, **kwargs):
        self.__dict__.update(mapping_or_iterable)
        self.__dict__.update(kwargs)

    def __repr__(self):
        items = (f"{k}={v!r}" for k, v in self.__dict__.items())
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __eq__(self, other):
        if isinstance(self, SimpleNamespace) and isinstance(other, SimpleNamespace):
           return self.__dict__ == other.__dict__
        return NotImplemented

```

`SimpleNamespace` can come in handy as a stand-in for `class NS: pass`. For a structured record type, though, reach for [`namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) instead.

[`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace) supports `SimpleNamespace` objects.

Added in version 3.3.

Changed in version 3.9: In the repr, the attribute ordering shifted away from alphabetical toward insertion order (as with `dict`).

Changed in version 3.13: Added support for an optional positional argument.

 types.DynamicClassAttribute(*fget=None*, *fset=None*, *fdel=None*, *doc=None*)

Send attribute access on a class through to `__getattr__`.

This is a descriptor used to define attributes that behave one way when reached through an instance and another way through a class. Access from an instance stays ordinary, while access to an attribute through a class gets sent to that class’s `__getattr__` method; the redirection works by raising AttributeError.

It thereby lets you keep properties live on an instance while also having virtual attributes of the same name on the class (refer to [`enum.Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) for an example).

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](types-capsuletype-class.md) · [Continue](types-coroutine.md) · [Owning module, declaration or section: types](types-dynamic-type-creation-and-names-for-built-in-types.md)
