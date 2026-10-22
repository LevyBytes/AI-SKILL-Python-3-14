# unittest.mock.Mock: `configure_mock()`, `__dir__()`, `_get_child_mock()`

configure_mock(***kwargs*)

Set attributes on the mock through keyword arguments.

You can assign attributes together with return values and side effects on child mocks by using ordinary dot notation and unpacking a dictionary into the method call:

```python
>>> mock = Mock()
>>> attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
>>> mock.configure_mock(**attrs)
>>> mock.method()
3
>>> mock.other()
Traceback (most recent call last):
  ...
KeyError

```

The very same result is reachable in the constructor call to mocks:

```python
>>> attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
>>> mock = Mock(some_attribute='eggs', **attrs)
>>> mock.some_attribute
'eggs'
>>> mock.method()
3
>>> mock.other()
Traceback (most recent call last):
  ...
KeyError

```

The point of `configure_mock()` is to simplify carrying out configuration once the mock already exists.

 __dir__()

`Mock` objects pare down what `dir(some_mock)` returns to only the useful results. For mocks carrying a *spec* this covers every permitted attribute for the mock.

Consult `FILTER_DIR` for what this filtering accomplishes, and how to turn it off.

 _get_child_mock(***kw*)

Build the child mocks for attributes and return value. By default a child mock takes the same type as its parent. Subclasses of Mock might wish to override this to tailor the way child mocks get built.

For mocks that are non-callable, the callable flavor gets used (rather than any custom subclass).

 called

A boolean indicating whether or not the mock object has been called:

```python
>>> mock = Mock(return_value=None)
>>> mock.called
False
>>> mock()
>>> mock.called
True

```

 call_count

An integer reporting the number of times the mock object has been called:

```python
>>> mock = Mock(return_value=None)
>>> mock.call_count
0
>>> mock()
>>> mock()
>>> mock.call_count
2

```

[Subject index](INDEX.md) · [Previous](mock-reset-specification-and-attachment.md) · [Continue](mock-return-value.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: unittest.mock.Mock](unittest-mock-mock-class.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
