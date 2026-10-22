# unittest.mock: Mock call history across methods and return values

mock_calls

`mock_calls` logs *every* call to the mock object, along with its methods, magic methods *and* return value mocks.

```python
>>> mock = MagicMock()
>>> result = mock(1, 2, 3)
>>> mock.first(a=3)
<MagicMock name='mock.first()' id='...'>
>>> mock.second()
<MagicMock name='mock.second()' id='...'>
>>> int(mock)
1
>>> result(1)
<MagicMock name='mock()()' id='...'>
>>> expected = [call(1, 2, 3), call.first(a=3), call.second(),
... call.__int__(), call()(1)]
>>> mock.mock_calls == expected
True

```

The members of `mock_calls` are `call` objects. They can be unpacked as tuples to reach the individual arguments. See calls as tuples.

Note

Because of how `mock_calls` is logged, wherever nested calls occur, the parameters of ancestor calls go unrecorded and therefore will always compare as equal:

```python
>>> mock = MagicMock()
>>> mock.top(a=3).bottom()
<MagicMock name='mock.top().bottom()' id='...'>
>>> mock.mock_calls
[call.top(a=3), call.top().bottom()]
>>> mock.mock_calls[-1] == call.top(a=-1).bottom()
True

```

 __class__

Ordinarily the `__class__` attribute of an object yields its type. For a mock object carrying a `spec`, `__class__` yields the spec class in its place. This lets mock objects clear [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) tests for whatever object they are standing in for / masquerading as:

```python
>>> mock = Mock(spec=3)
>>> isinstance(mock, int)
True

```

`__class__` accepts assignment, which lets a mock clear an [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) check without obliging you to use a spec:

```python
>>> mock = Mock()
>>> mock.__class__ = dict
>>> isinstance(mock, dict)
True

```

[Subject index](INDEX.md) · [Previous](mock-call-arguments.md) · [Continue](unittest-mock-noncallablemock-class.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: unittest.mock.Mock](unittest-mock-mock-class.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
