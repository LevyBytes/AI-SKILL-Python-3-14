# unittest.mock: Mock return-value configuration

return_value

Assign this to set up the value that calling the mock returns:

```python
>>> mock = Mock()
>>> mock.return_value = 'fish'
>>> mock()
'fish'

```

By default the return value is a mock object, and you may set it up in the ordinary way:

```python
>>> mock = Mock()
>>> mock.return_value.attribute = sentinel.Attribute
>>> mock.return_value()
<Mock name='mock()()' id='...'>
>>> mock.return_value.assert_called_with()

```

`return_value` may likewise be assigned within the constructor:

```python
>>> mock = Mock(return_value=3)
>>> mock.return_value
3
>>> mock()
3

```

[Subject index](INDEX.md) · [Previous](mock-configuration-and-child-creation.md) · [Continue](mock-side-effects.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: unittest.mock.Mock](unittest-mock-mock-class.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
