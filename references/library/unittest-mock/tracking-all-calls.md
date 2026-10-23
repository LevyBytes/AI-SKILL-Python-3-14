# unittest.mock - Tracking all calls

### Tracking all calls

Frequently you want to follow more than just one call to a method. The [`mock_calls`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.mock_calls) attribute logs every call to the mock's child attributes - as well as calls to their children.

```python
>>> mock = MagicMock()
>>> mock.method()
<MagicMock name='mock.method()' id='...'>
>>> mock.attribute.method(10, x=53)
<MagicMock name='mock.attribute.method()' id='...'>
>>> mock.mock_calls
[call.method(), call.attribute.method(10, x=53)]

```

Should you assert something about `mock_calls` while unexpected methods were invoked, the assertion fails. That's valuable, because beyond confirming the calls you anticipated occurred, you simultaneously verify they happened in the correct sequence with nothing extra called:

The [`call`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.call) object lets you assemble lists to compare against `mock_calls`:

```python
>>> expected = [call.method(), call.attribute.method(10, x=53)]
>>> mock.mock_calls == expected
True

```

That said, arguments passed to calls that yield mocks aren't logged, so you can't trace nested calls in which the arguments used to build ancestors matter:

```python
>>> m = Mock()
>>> m.factory(important=True).deliver()
<Mock name='mock.factory().deliver()' id='...'>
>>> m.mock_calls[-1] == call.factory(important=False).deliver()
True

```

[Subject index](INDEX.md) · [Previous](naming-your-mocks.md) · [Continue](setting-return-values-and-attributes.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
