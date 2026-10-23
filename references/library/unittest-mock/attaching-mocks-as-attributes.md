# unittest.mock - Attaching Mocks as Attributes

### Attaching Mocks as Attributes

Attaching a mock as an attribute of another mock (or as its return value) makes it a “child” of that mock. Any calls to the child get logged in the parent's `method_calls` and `mock_calls` attributes. This comes in handy when you configure child mocks first and only then bind them onto the parent, or when binding mocks onto a parent that records each call reaching the children and lets you assert on how calls are ordered across mocks:

```python
>>> parent = MagicMock()
>>> child1 = MagicMock(return_value=None)
>>> child2 = MagicMock(return_value=None)
>>> parent.child1 = child1
>>> parent.child2 = child2
>>> child1(1)
>>> child2(2)
>>> parent.mock_calls
[call.child1(1), call.child2(2)]

```

There's an exception when the mock carries a name. That lets you stop the “parenting” in cases where, for whatever reason, you'd rather it didn't take place.

```python
>>> mock = MagicMock()
>>> not_a_child = MagicMock(name='not-a-child')
>>> mock.attribute = not_a_child
>>> mock.attribute()
<MagicMock name='not-a-child()' id='...'>
>>> mock.mock_calls
[]

```

The mocks that `patch()` builds for you are named automatically. To attach named mocks onto a parent, use the `attach_mock()` method:

```python
>>> thing1 = object()
>>> thing2 = object()
>>> parent = MagicMock()
>>> with patch('__main__.thing1', return_value=None) as child1:
...     with patch('__main__.thing2', return_value=None) as child2:
...         parent.attach_mock(child1, 'child1')
...         parent.attach_mock(child2, 'child2')
...         child1('one')
...         child2('two')
...
>>> parent.mock_calls
[call.child1('one'), call.child2('two')]

```

[Subject index](INDEX.md) · [Previous](mock-names-and-the-name-attribute.md) · [Continue](the-patchers.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
