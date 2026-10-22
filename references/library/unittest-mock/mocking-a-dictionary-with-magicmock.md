# unittest.mock — Mocking a dictionary with MagicMock

### Mocking a dictionary with MagicMock

There may be times you want to mock a dictionary, or some other container, logging every access to it while it continues to act like a dictionary.

[`MagicMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.MagicMock) makes this achievable: it can imitate a dictionary, and with [`side_effect`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.side_effect) we route dictionary access to a genuine backing dictionary that we control.

Whenever the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) and [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__) methods on our `MagicMock` fire (ordinary dictionary access), `side_effect` runs with the key (plus the value as well, in the `__setitem__` case). The return value is ours to dictate too.

Once the `MagicMock` has seen some use, attributes such as [`call_args_list`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.call_args_list) let us assert about the way the dictionary was exercised:

```python
>>> my_dict = {'a': 1, 'b': 2, 'c': 3}
>>> def getitem(name):
...      return my_dict[name]
...
>>> def setitem(name, val):
...     my_dict[name] = val
...
>>> mock = MagicMock()
>>> mock.__getitem__.side_effect = getitem
>>> mock.__setitem__.side_effect = setitem

```

Note

Rather than reaching for `MagicMock`, you can instead use `Mock` and supply *only* the magic methods you actually want:

```python
>>> mock = Mock()
>>> mock.__getitem__ = Mock(side_effect=getitem)
>>> mock.__setitem__ = Mock(side_effect=setitem)

```

A *third* possibility is to keep `MagicMock` but feed in `dict` as the *spec* (or *spec_set*) argument, so the resulting `MagicMock` exposes only the dictionary magic methods:

```python
>>> mock = MagicMock(spec_set=dict)
>>> mock.__getitem__.side_effect = getitem
>>> mock.__setitem__.side_effect = setitem

```

Once these side effect functions are wired up, the `mock` acts like an ordinary dictionary yet logs the access. It will even throw a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) should you reach for a key that isn't present.

```python
>>> mock['a']
1
>>> mock['c']
3
>>> mock['d']
Traceback (most recent call last):
    ...
KeyError: 'd'
>>> mock['b'] = 'fish'
>>> mock['d'] = 'eggs'
>>> mock['b']
'fish'
>>> mock['d']
'eggs'

```

Once it has seen use, you can assert about the access through the usual mock methods and attributes:

```python
>>> mock.__getitem__.call_args_list
[call('a'), call('c'), call('d'), call('b'), call('d')]
>>> mock.__setitem__.call_args_list
[call('b', 'fish'), call('d', 'eggs')]
>>> my_dict
{'a': 1, 'b': 'fish', 'c': 3, 'd': 'eggs'}

```

[Subject index](INDEX.md) · [Previous](nesting-patches.md) · [Continue](mock-subclasses-and-their-attributes.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
