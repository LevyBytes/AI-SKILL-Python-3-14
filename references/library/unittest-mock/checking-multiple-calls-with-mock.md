# unittest.mock - Checking multiple calls with mock

### Checking multiple calls with mock

mock offers a tidy API for asserting against the way your mock objects get exercised.

```python
>>> mock = Mock()
>>> mock.foo_bar.return_value = None
>>> mock.foo_bar('baz', spam='eggs')
>>> mock.foo_bar.assert_called_with('baz', spam='eggs')

```

When a mock is invoked just a single time, the [`assert_called_once_with()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_called_once_with) method serves well, since it additionally checks that the [`call_count`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.call_count) equals one.

```python
>>> mock.foo_bar.assert_called_once_with('baz', spam='eggs')
>>> mock.foo_bar()
>>> mock.foo_bar.assert_called_once_with('baz', spam='eggs')
Traceback (most recent call last):
    ...
AssertionError: Expected 'foo_bar' to be called once. Called 2 times.
Calls: [call('baz', spam='eggs'), call()].

```

Each of `assert_called_with` and `assert_called_once_with` checks against the *most recent* call. Should your mock be invoked multiple times and you want to assert about *all* of those invocations, reach for [`call_args_list`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.call_args_list):

```python
>>> mock = Mock(return_value=None)
>>> mock(1, 2, 3)
>>> mock(4, 5, 6)
>>> mock()
>>> mock.call_args_list
[call(1, 2, 3), call(4, 5, 6), call()]

```

Assertions about these invocations are straightforward thanks to the [`call`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.call) helper. Assemble a list of the calls you expect and match it against `call_args_list`. The result reads strikingly close to the repr of `call_args_list`:

```python
>>> expected = [call(1, 2, 3), call(4, 5, 6), call()]
>>> mock.call_args_list == expected
True

```

[Subject index](INDEX.md) · [Previous](mocking-unbound-methods.md) · [Continue](mutable-mock-argument-overview.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
