# unittest.mock - Magic Mock - Contract: `__str__`: default str for the mock

`__str__`: default str for the mock

- `__sizeof__`: default sizeof for the mock

For example:

```python
>>> mock = MagicMock()
>>> int(mock)
1
>>> len(mock)
0
>>> list(mock)
[]
>>> object() in mock
False

```

The pair of equality methods, `__eq__()` and `__ne__()`, are a special case. They perform the default identity-based equality comparison through the `side_effect` attribute, until you alter their return value to yield something different:

```python
>>> MagicMock() == 3
False
>>> MagicMock() != 3
True
>>> mock = MagicMock()
>>> mock.__eq__.return_value = True
>>> mock == 3
True

```

What `__iter__()` returns may be any iterable object — it need not be an iterator:

```python
>>> mock = MagicMock()
>>> mock.__iter__.return_value = ['a', 'b', 'c']
>>> list(mock)
['a', 'b', 'c']
>>> list(mock)
['a', 'b', 'c']

```

When the return value *is* an iterator, iterating it a single time exhausts it, and any further iterations come back as an empty list:

```python
>>> mock.__iter__.return_value = iter(['a', 'b', 'c'])
>>> list(mock)
['a', 'b', 'c']
>>> list(mock)
[]

```

`MagicMock` arrives with every supported magic method configured, save for a few of the obscure and obsolete ones. You may still set those up yourself if you like.

The supported magic methods that `MagicMock` does not set up by default are:

- `__subclasses__`

- `__dir__`

- `__format__`

- `__get__`, `__set__` and `__delete__`

- `__reversed__` and `__missing__`

-

[Subject index](INDEX.md) · [Previous](unittest-mock-noncallablemagicmock-class.md) · [Continue](magic-mock-pickling-protocols.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: unittest.mock.NonCallableMagicMock](unittest-mock-noncallablemagicmock-class.md) · [Owning module, declaration or section: Magic Mock](unittest-mock-magicmock-class.md)
