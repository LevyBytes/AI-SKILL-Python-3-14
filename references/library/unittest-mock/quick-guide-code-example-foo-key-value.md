# unittest.mock — Quick Guide — Code example: >>> foo = {'key': 'value'}

```python
>>> foo = {'key': 'value'}
>>> original = foo.copy()
>>> with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
...     assert foo == {'newkey': 'newvalue'}
...
>>> assert foo == original

```

Python magic methods can be mocked through Mock as well. Reaching for the `MagicMock` class is the simplest route to magic methods. With it you can do such things as:

```python
>>> mock = MagicMock()
>>> mock.__str__.return_value = 'foobarbaz'
>>> str(mock)
'foobarbaz'
>>> mock.__str__.assert_called_with()

```

Mock lets you bind functions (or further Mock instances) onto magic methods, and they get invoked as expected. The `MagicMock` class is simply a Mock flavor that comes with every magic method already built in for you (well, every handy one at any rate).

Here is how magic methods look alongside the plain Mock class:

```python
>>> mock = Mock()
>>> mock.__str__ = Mock(return_value='wheeeeee')
>>> str(mock)
'wheeeeee'

```

So that the mock objects inside your tests carry the same api as whatever they stand in for, auto-speccing is available. You can reach auto-speccing by way of the *autospec* argument to patch, or via the `create_autospec()` function. Auto-speccing produces mock objects bearing the identical attributes and methods as the objects they substitute for, and every function and method (constructors included) shares the call signature of the genuine object.

This guarantees that, if misused, your mocks break the same way your production code would:

```python
>>> from unittest.mock import create_autospec
>>> def function(a, b, c):
...     pass
...
>>> mock_function = create_autospec(function, return_value='fishy')
>>> mock_function(1, 2, 3)
'fishy'
>>> mock_function.assert_called_once_with(1, 2, 3)
>>> mock_function('wrong arguments')
Traceback (most recent call last):
 ...
TypeError: missing a required argument: 'b'

```

You may also apply `create_autospec()` to classes, in which case it duplicates the signature of the `__init__` method, and to callable objects, where it duplicates the signature of the `__call__` method.

[Subject index](INDEX.md) · [Previous](quick-guide-section-introduction-and-initial-examples.md) · [Continue](unittest-mock-mock-class.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: Quick Guide](quick-guide-section-introduction-and-initial-examples.md)
