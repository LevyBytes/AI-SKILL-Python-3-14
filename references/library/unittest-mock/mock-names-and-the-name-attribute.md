# unittest.mock - Mock names and the name attribute

### Mock names and the name attribute

Because “name” is one of the `Mock` constructor's arguments, you can't simply hand it in when you create the mock if you want a “name” attribute on it. Two paths exist. The first is to call `configure_mock()`:

```python
>>> mock = MagicMock()
>>> mock.configure_mock(name='my_name')
>>> mock.name
'my_name'

```

The easier path is to just assign the “name” attribute once the mock has been created:

```python
>>> mock = MagicMock()
>>> mock.name = "foo"

```

[Subject index](INDEX.md) · [Previous](deleting-attributes.md) · [Continue](attaching-mocks-as-attributes.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
