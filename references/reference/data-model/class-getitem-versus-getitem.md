# 3.3.5.2. *__class_getitem__* versus *__getitem__*

#### 3.3.5.2. *__class_getitem__* versus *__getitem__*

Normally, [subscription](https://docs.python.org/3.14/reference/expressions.html#subscriptions) of an object with square brackets invokes the `__getitem__()` instance method defined on that object's class. But when the thing being subscribed is itself a class, the class method `__class_getitem__()` might be invoked in its place. A properly defined `__class_getitem__()` should hand back a [GenericAlias](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias) object.

Faced with the [expression](https://docs.python.org/3.14/glossary.html#term-expression) `obj[x]`, the Python interpreter goes through roughly the following reasoning to choose between calling `__getitem__()` and `__class_getitem__()`:

```python
from inspect import isclass

def subscribe(obj, x):
    """Return the result of the expression 'obj[x]'"""

    class_of_obj = type(obj)

    # If the class of obj defines __getitem__,
    # call class_of_obj.__getitem__(obj, x)
    if hasattr(class_of_obj, '__getitem__'):
        return class_of_obj.__getitem__(obj, x)

    # Else, if obj is a class and defines __class_getitem__,
    # call obj.__class_getitem__(x)
    elif isclass(obj) and hasattr(obj, '__class_getitem__'):
        return obj.__class_getitem__(x)

    # Else, raise an exception
    else:
        raise TypeError(
            f"'{class_of_obj.__name__}' object is not subscriptable"
        )

```

Within Python, every class is itself an instance of some other class. A class's class is termed that class's [metaclass](https://docs.python.org/3.14/glossary.html#term-metaclass), and the [`type`](https://docs.python.org/3.14/library/functions.html#type) class is the metaclass of most classes. Since `type` defines no `__getitem__()`, expressions like `list[int]`, `dict[str, float]` and `tuple[str, bytes]` each cause `__class_getitem__()` to be called:

```python
>>> # list has class "type" as its metaclass, like most classes:
>>> type(list)
<class 'type'>
>>> type(dict) == type(list) == type(tuple) == type(str) == type(bytes)
True
>>> # "list[int]" calls "list.__class_getitem__(int)"
>>> list[int]
list[int]
>>> # list.__class_getitem__ returns a GenericAlias object:
>>> type(list[int])
<class 'types.GenericAlias'>

```

If, on the other hand, a class carries a custom metaclass that defines `__getitem__()`, subscribing that class can produce different behaviour. The [`enum`](https://docs.python.org/3.14/library/enum.html#module-enum) module furnishes one such example:

```python
>>> from enum import Enum
>>> class Menu(Enum):
...     """A breakfast menu"""
...     SPAM = 'spam'
...     BACON = 'bacon'
...
>>> # Enum classes have a custom metaclass:
>>> type(Menu)
<class 'enum.EnumMeta'>
>>> # EnumMeta defines __getitem__,
>>> # so __class_getitem__ is not called,
>>> # and the result is not a GenericAlias object:
>>> Menu['SPAM']
<Menu.SPAM: 'spam'>
>>> type(Menu['SPAM'])
<enum 'Menu'>

```

See also

[**PEP 560**](https://peps.python.org/pep-0560/) - Core Support for typing module and generic types

Introducing `__class_getitem__()`, and outlining when a [subscription](https://docs.python.org/3.14/reference/expressions.html#subscriptions) results in `__class_getitem__()` being called instead of `__getitem__()`

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-generic-types.md) · [Previous source section](the-purpose-of-class-getitem.md) · [Following source section](object-call.md)
