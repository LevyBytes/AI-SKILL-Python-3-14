# unittest.mock.Mock: `assert_has_calls()`, `assert_not_called()`

assert_has_calls(*calls*, *any_order=False*)

assert that the named calls were made against the mock. Those calls are searched for within the `mock_calls` list.

Where *any_order* is false, the calls have to come in sequence. Extra calls may occur before or after the ones named.

Where *any_order* is true, the calls may come in any sequence, yet each one has to show up within `mock_calls`.

```python
>>> mock = Mock(return_value=None)
>>> mock(1)
>>> mock(2)
>>> mock(3)
>>> mock(4)
>>> calls = [call(2), call(3)]
>>> mock.assert_has_calls(calls)
>>> calls = [call(4), call(2), call(3)]
>>> mock.assert_has_calls(calls, any_order=True)

```

 assert_not_called()

Assert the mock was never called.

```python
>>> m = Mock()
>>> m.hello.assert_not_called()
>>> obj = m.hello()
>>> m.hello.assert_not_called()
Traceback (most recent call last):
  ...
AssertionError: Expected 'hello' to not have been called. Called 1 times.
Calls: [call()].

```

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](mock-call-count-and-argument-assertions.md) · [Continue](mock-reset-specification-and-attachment.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: unittest.mock.Mock](unittest-mock-mock-class.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
