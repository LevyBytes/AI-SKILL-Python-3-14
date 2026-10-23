# unittest.mock - Deleting Attributes

### Deleting Attributes

Mock objects bring attributes into being on demand. That lets them masquerade as objects of any type.

Sometimes you'll want a mock object to answer `False` for a [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr) check, or to raise an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) when an attribute is read. Supplying an object as a `spec` for a mock achieves this, but that's not always handy.

You "block" attributes by removing them. After deletion, reading the attribute raises an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

```python
>>> mock = MagicMock()
>>> hasattr(mock, 'm')
True
>>> del mock.m
>>> hasattr(mock, 'm')
False
>>> del mock.f
>>> mock.f
Traceback (most recent call last):
    ...
AttributeError: f

```

[Subject index](INDEX.md) · [Previous](calling-code-example-m-magicmock-side-effect-1-2-3.md) · [Continue](mock-names-and-the-name-attribute.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
