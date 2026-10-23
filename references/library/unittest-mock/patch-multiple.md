# unittest.mock - patch.multiple

### patch.multiple

 patch.multiple(*target*, *spec=None*, *create=False*, *spec_set=None*, *autospec=None*, *new_callable=None*, ***kwargs*)

Carry out several patches at once in one call. It accepts the object being patched (supplied either as an object or as a string that fetches the object via import) along with keyword arguments naming the patches:

```python
with patch.multiple(settings, FIRST_PATCH='one', SECOND_PATCH='two'):
    ...

```

Supply `DEFAULT` as the value when you want `patch.multiple()` to manufacture mocks for you. Here the created mocks reach a decorated function by keyword, and a dictionary comes back when `patch.multiple()` serves as a context manager.

`patch.multiple()` may serve as a decorator, a class decorator, or a context manager. The arguments *spec*, *spec_set*, *create*, *autospec* and *new_callable* mean the same thing they do for `patch()`. Those arguments get applied to *all* patches that `patch.multiple()` performs.

As a class decorator, `patch.multiple()` respects `patch.TEST_PREFIX` when selecting which methods to wrap.

When you'd like `patch.multiple()` to manufacture mocks for you, supply `DEFAULT` as the value. Used as a decorator, `patch.multiple()` delivers the created mocks to the decorated function by keyword.

```python
>>> thing = object()
>>> other = object()

>>> @patch.multiple('__main__', thing=DEFAULT, other=DEFAULT)
... def test_function(thing, other):
...     assert isinstance(thing, MagicMock)
...     assert isinstance(other, MagicMock)
...
>>> test_function()

```

You may nest `patch.multiple()` together with other `patch` decorators, but place keyword-supplied arguments *after* whatever standard arguments `patch()` creates:

```python
>>> @patch('sys.exit')
... @patch.multiple('__main__', thing=DEFAULT, other=DEFAULT)
... def test_function(mock_exit, other, thing):
...     assert 'other' in repr(other)
...     assert 'thing' in repr(thing)
...     assert 'exit' in repr(mock_exit)
...
>>> test_function()

```

Used as a context manager, `patch.multiple()` returns a dictionary in which the created mocks are keyed by name:

```python
>>> with patch.multiple('__main__', thing=DEFAULT, other=DEFAULT) as values:
...     assert 'other' in repr(values['other'])
...     assert 'thing' in repr(values['thing'])
...     assert values['thing'] is thing
...     assert values['other'] is other
...

```

[Subject index](INDEX.md) · [Previous](patch-dict-code-example-class-container.md) · [Continue](patch-stopall.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
