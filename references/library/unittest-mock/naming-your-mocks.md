# unittest.mock - Naming your mocks

### Naming your mocks

Assigning a name to your mocks can pay off. That name surfaces in the repr of the mock and proves handy whenever the mock turns up in test failure messages. The name also flows down to the mock's attributes or methods:

```python
>>> mock = MagicMock(name='foo')
>>> mock
<MagicMock name='foo' id='...'>
>>> mock.method
<MagicMock name='foo.method' id='...'>

```

[Subject index](INDEX.md) · [Previous](mocking-classes.md) · [Continue](tracking-all-calls.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
