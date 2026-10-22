# How do I call a method defined in a base class from a derived class that extends it?

### How do I call a method defined in a base class from a derived class that extends it?

Reach for the built-in [`super()`](https://docs.python.org/3.14/library/functions.html#super) function:

```python
class Derived(Base):
    def meth(self):
        super().meth()  # calls Base.meth

```

Here, [`super()`](https://docs.python.org/3.14/library/functions.html#super) figures out on its own the instance it was invoked from (the `self` value), consults the [method resolution order](https://docs.python.org/3.14/glossary.html#term-method-resolution-order) (MRO) via `type(self).__mro__`, and yields whatever follows `Derived` in the MRO: `Base`.

[Subject index](INDEX.md)
