# unittest.mock — Quick Guide — Section introduction and initial examples

### Quick Guide

As soon as you touch their attributes and methods, `Mock` and `MagicMock` objects bring them into being and keep a record of how they were exercised. You may set them up to declare return values or restrict which attributes exist, and afterward assert against the way they were exercised:

```python
>>> from unittest.mock import MagicMock
>>> thing = ProductionClass()
>>> thing.method = MagicMock(return_value=3)
>>> thing.method(3, 4, 5, key='value')
3
>>> thing.method.assert_called_with(3, 4, 5, key='value')

```

To trigger side effects — for instance, throwing an exception once a mock is invoked — use `side_effect`:

```python
>>> from unittest.mock import Mock
>>> mock = Mock(side_effect=KeyError('foo'))
>>> mock()
Traceback (most recent call last):
 ...
KeyError: 'foo'

```

```python
>>> values = {'a': 1, 'b': 2, 'c': 3}
>>> def side_effect(arg):
...     return values[arg]
...
>>> mock.side_effect = side_effect
>>> mock('a'), mock('b'), mock('c')
(1, 2, 3)
>>> mock.side_effect = [5, 4, 3, 2, 1]
>>> mock(), mock(), mock()
(5, 4, 3)

```

Numerous additional knobs exist for setting Mock up and steering how it behaves. As one illustration, the *spec* argument tells the mock to draw its specification from some other object. Trying to reach attributes or methods on the mock that the spec lacks will fail with an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

Mocking classes or objects inside a module being tested is straightforward with the `patch()` decorator / context manager. Whatever object you name gets swapped out for a mock (or some other object) while the test runs and is put back once the test concludes:

```python
>>> from unittest.mock import patch
>>> @patch('module.ClassName2')
... @patch('module.ClassName1')
... def test(MockClass1, MockClass2):
...     module.ClassName1()
...     module.ClassName2()
...     assert MockClass1 is module.ClassName1
...     assert MockClass2 is module.ClassName2
...     assert MockClass1.called
...     assert MockClass2.called
...
>>> test()

```

Note

Stacking patch decorators delivers the mocks into the decorated function following the very order they were applied (the usual *Python* sequence for applying decorators). That works from the bottom upward, so above the mock standing in for `module.ClassName1` arrives first.

When using `patch()`, what counts is that you patch objects in whichever namespace they get looked up. Usually that poses no difficulty, yet for a brief overview consult where to patch.

Beyond serving as a decorator, `patch()` works as a context manager inside a with statement:

```python
>>> with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
...     thing = ProductionClass()
...     thing.method(1, 2, 3)
...
>>> mock_method.assert_called_once_with(1, 2, 3)

```

`patch.dict()` likewise exists for assigning entries in a dictionary only within a given scope and then returning the dictionary to how it began once the test finishes:

[Subject index](INDEX.md) · [Previous](unittest-mock-mock-object-library.md) · [Continue](quick-guide-code-example-foo-key-value.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
