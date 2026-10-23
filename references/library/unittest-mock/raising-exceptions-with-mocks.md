# unittest.mock - Raising exceptions with mocks

### Raising exceptions with mocks

One handy attribute is [`side_effect`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.side_effect). Assign it an exception class or instance and the exception fires when the mock gets called.

```python
>>> mock = Mock(side_effect=Exception('Boom!'))
>>> mock()
Traceback (most recent call last):
  ...
Exception: Boom!

```

[Subject index](INDEX.md) · [Previous](setting-return-values-and-attributes.md) · [Continue](side-effect-functions-and-iterables.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
