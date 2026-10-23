# unittest.mock - Nesting Patch Decorators

### Nesting Patch Decorators

To carry out several patches, you can just stack the decorators one above another.

This is the pattern for stacking multiple patch decorators:

```python
>>> @patch.object(SomeClass, 'class_method')
... @patch.object(SomeClass, 'static_method')
... def test(mock1, mock2):
...     assert SomeClass.static_method is mock1
...     assert SomeClass.class_method is mock2
...     SomeClass.static_method('foo')
...     SomeClass.class_method('bar')
...     return mock1, mock2
...
>>> mock1, mock2 = test()
>>> mock1.assert_called_once_with('foo')
>>> mock2.assert_called_once_with('bar')

```

Be aware that the decorators take effect from the bottom up — the usual order in which Python applies decorators. The sequence of created mocks delivered to your test function follows that same order.

[Subject index](INDEX.md) · [Previous](test-prefix.md) · [Continue](where-to-patch.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
