# unittest.mock.Mock: `assert_called()`, `assert_called_once()`, `assert_called_with()`, `assert_called_once_with()`, `assert_any_call()`

assert_called()

Assert that the mock was called at least once.

```python
>>> mock = Mock()
>>> mock.method()
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called()

```

Added in version 3.6.

 assert_called_once()

Assert that the mock was called exactly once.

```python
>>> mock = Mock()
>>> mock.method()
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called_once()
>>> mock.method()
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called_once()
Traceback (most recent call last):
...
AssertionError: Expected 'method' to have been called once. Called 2 times.
Calls: [call(), call()].

```

Added in version 3.6.

 assert_called_with(**args*, ***kwargs*)

This method offers a handy way to assert that the most recent call happened in a specific manner:

```python
>>> mock = Mock()
>>> mock.method(1, 2, 3, test='wow')
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called_with(1, 2, 3, test='wow')

```

 assert_called_once_with(**args*, ***kwargs*)

Assert that just a single call to the mock occurred, and that this one call carried the supplied arguments.

```python
>>> mock = Mock(return_value=None)
>>> mock('foo', bar='baz')
>>> mock.assert_called_once_with('foo', bar='baz')
>>> mock('other', bar='values')
>>> mock.assert_called_once_with('other', bar='values')
Traceback (most recent call last):
  ...
AssertionError: Expected 'mock' to be called once. Called 2 times.
Calls: [call('foo', bar='baz'), call('other', bar='values')].

```

 assert_any_call(**args*, ***kwargs*)

assert the mock has been called with the specified arguments.

This assert succeeds when the mock has *ever* been called, in contrast to `assert_called_with()` and `assert_called_once_with()`, which succeed only when the call is the latest one, and for `assert_called_once_with()` it additionally has to be the sole call.

```python
>>> mock = Mock(return_value=None)
>>> mock(1, 2, arg='thing')
>>> mock('some', 'thing', 'else')
>>> mock.assert_any_call(1, 2, arg='thing')

```

[Subject index](INDEX.md) · [Previous](unittest-mock-mock-class.md) · [Continue](mock-call-sequence-and-absence-assertions.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: unittest.mock.Mock](unittest-mock-mock-class.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
