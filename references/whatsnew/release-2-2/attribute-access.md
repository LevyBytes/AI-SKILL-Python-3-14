# What’s New in Python 2.2 / Attribute Access

### Attribute Access

Quite a few advanced Python classes set up hooks for attribute access via [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__); most of the time this is for convenience, making code easier to read by quietly turning an attribute access like `obj.parent` into a method call like `obj.get_parent`. Python 2.2 brings a few new levers for managing attribute access.

First off, `__getattr__(attr_name)` is still honoured by new-style classes, and nothing about it changed. Just as before, it fires when something tries to reach `obj.foo` and no attribute called `foo` shows up in the instance’s dictionary.

New-style classes also gain a new method, `__getattribute__(attr_name)`. Where the two diverge is that [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) gets invoked *every* time any attribute at all is reached, whereas the older [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) only runs when `foo` can’t be located in the instance’s dictionary.

That said, the *properties* support in Python 2.2 will frequently be an easier route to intercepting attribute references. Coding a `__getattr__()` method is fiddly, because dodging recursion means you can’t perform ordinary attribute accesses inside it and instead must fiddle with the contents of [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__). [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) methods also wind up being called by Python while it probes for other methods such as [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) or `__coerce__()`, so they must be authored with that in mind. On top of that, running a function on every single attribute access carries a noticeable performance hit.

[`property`](https://docs.python.org/3.14/library/functions.html#property) is a brand-new built-in type that bundles up three functions to get, set, or delete an attribute, plus a docstring. Suppose, for instance, you want a `size` attribute that’s computed yet still assignable; you could write:

```python
class C(object):
    def get_size (self):
        result = ... computation ...
        return result
    def set_size (self, size):
        ... compute something based on the size
        and set internal state appropriately ...

    # Define a property.  The 'delete this attribute'
    # method is defined as None, so the attribute
    # can't be deleted.
    size = property(get_size, set_size,
                    None,
                    "Storage size of this instance")

```

That’s undeniably clearer and less effort to write than a `__getattr__()`/`__setattr__()` pair that watches for the `size` attribute and treats it specially while pulling every other attribute out of the instance’s [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__). Only accesses to `size` bear the cost of invoking a function, so references to the rest of the attributes proceed at their normal pace.

Lastly, you can restrict which attributes may be referenced on an object via the new [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__) class attribute. Python objects are typically highly dynamic; at any moment you can conjure a new attribute on an instance just by writing `obj.new_attr=1`. A new-style class is able to declare a class attribute called `__slots__` to confine the permitted attributes to a specific set of names. An example should make it plain:

```python
>>> class C(object):
...     __slots__ = ('template', 'name')
...
>>> obj = C()
>>> print obj.template
None
>>> obj.template = 'Test'
>>> print obj.template
Test
>>> obj.newattr = None
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
AttributeError: 'C' object has no attribute 'newattr'

```

Notice that trying to assign to an attribute absent from [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__) earns you an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

[Subject index](INDEX.md) · [Previous source section](multiple-inheritance-the-diamond-rule.md) · [Next source section](related-links.md) · [Release/subject declaration](introduction.md)
