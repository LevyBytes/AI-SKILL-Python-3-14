# unittest.mock - patch

### patch

Note

The crucial point is to patch within the correct namespace. Refer to the section where to patch.

Once `patch()` builds a mock on your behalf, configuring that mock is usually your immediate next step. Part of this setup is achievable straight from the patch call itself. Whatever arbitrary keywords you hand to the call become attributes assigned on the mock that gets produced:

```python
>>> patcher = patch('__main__.thing', first='one', second='two')
>>> mock_thing = patcher.start()
>>> mock_thing.first
'one'
>>> mock_thing.second
'two'

```

Beyond plain attributes on the produced mock, you can likewise configure attributes belonging to child mocks, such as their `return_value` and `side_effect`. Passing these straight in as keyword arguments isn't syntactically legal, yet you can still take a dictionary keyed by those names and unpack it into a `patch()` call with `**`:

```python
>>> config = {'method.return_value': 3, 'other.side_effect': KeyError}
>>> patcher = patch('__main__.thing', **config)
>>> mock_thing = patcher.start()
>>> mock_thing.method()
3
>>> mock_thing.other()
Traceback (most recent call last):
  ...
KeyError

```

By default, an attempt to patch some function within a module — or a method, or a class attribute — that has no existing definition raises [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError):

```python
>>> @patch('sys.non_existing_attribute', 42)
... def test():
...     assert sys.non_existing_attribute == 42
...
>>> test()
Traceback (most recent call last):
  ...
AttributeError: <module 'sys' (built-in)> does not have the attribute 'non_existing_attribute'

```

yet passing `create=True` into the `patch()` call makes the preceding example behave as intended:

```python
>>> @patch('sys.non_existing_attribute', 42, create=True)
... def test(mock_stdout):
...     assert sys.non_existing_attribute == 42
...
>>> test()

```

Changed in version 3.8: when its target happens to be an async function, `patch()` now hands back an `AsyncMock`.

[Subject index](INDEX.md) · [Previous](the-patchers.md) · [Continue](unittest-mock-patch.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Continue](patch-object.md) · [Owning module, declaration or section: unittest.mock.patch](unittest-mock-patch.md) · [Preceding source contract and version conditions](patch-code-example-thing-object.md)
