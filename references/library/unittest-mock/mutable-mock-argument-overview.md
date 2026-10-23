# unittest.mock - Coping with mutable arguments - Section introduction and initial examples

### Coping with mutable arguments

A further scenario, uncommon yet capable of tripping you up, arises when mutable arguments are passed to your mock. Both `call_args` and `call_args_list` keep *references* to the arguments. Once the code being tested mutates those arguments, you lose the ability to assert what they held at the moment the mock was invoked.

The snippet below illustrates the trouble. Picture these functions living in "mymodule":

```python
def frob(val):
    pass

def grob(val):
    "First frob and then clear val"
    frob(val)
    val.clear()

```

Watch what unfolds when we attempt to confirm that `grob` invokes `frob` with the right argument:

```python
>>> with patch('mymodule.frob') as mock_frob:
...     val = {6}
...     mymodule.grob(val)
...
>>> val
set()
>>> mock_frob.assert_called_with({6})
Traceback (most recent call last):
    ...
AssertionError: Expected: (({6},), {})
Called with: ((set(),), {})

```

One option would be having mock duplicate the arguments handed to it. That, though, could break assertions that depend on object identity for equality.

What follows is a fix built on the [`side_effect`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.side_effect) feature. When you supply a `side_effect` function to a mock, `side_effect` receives the very same args the mock did. That hands us a chance to clone the arguments and stash them for assertions made later. Here I lean on *another* mock to keep the arguments, letting me reuse the mock methods to run the assertion. Once more a helper function wires this together for me.

```python
>>> from copy import deepcopy
>>> from unittest.mock import Mock, patch, DEFAULT
>>> def copy_call_args(mock):
...     new_mock = Mock()
...     def side_effect(*args, **kwargs):
...         args = deepcopy(args)
...         kwargs = deepcopy(kwargs)
...         new_mock(*args, **kwargs)
...         return DEFAULT
...     mock.side_effect = side_effect
...     return new_mock
...
>>> with patch('mymodule.frob') as mock_frob:
...     new_mock = copy_call_args(mock_frob)
...     val = {6}
...     mymodule.grob(val)
...
>>> new_mock.assert_called_with({6})
>>> new_mock.call_args
call({6})

```

You feed `copy_call_args` the mock that is destined to be called, and it gives back a fresh mock against which we assert. The `side_effect` function clones the args and then calls our `new_mock` with that clone.

Note

When a mock is destined to be invoked just once, there is a simpler route for inspecting arguments right where the call lands. Just place the checks straight inside a `side_effect` function.

```python
>>> def side_effect(arg):
...     assert arg == {6}
...
>>> mock = Mock(side_effect=side_effect)
>>> mock({6})
>>> mock(set())
Traceback (most recent call last):
    ...
AssertionError

```

A different route is to derive a subclass of [`Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock) or [`MagicMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.MagicMock) that duplicates the arguments (via [`copy.deepcopy()`](https://docs.python.org/3.14/library/copy.html#copy.deepcopy)). One possible implementation looks like this:

[Subject index](INDEX.md) · [Previous](checking-multiple-calls-with-mock.md) · [Continue](mutable-mock-argument-deepcopy-example.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
