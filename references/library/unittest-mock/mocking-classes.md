# unittest.mock - Mocking classes

### Mocking classes

A frequent scenario is mocking out classes that your code under test instantiates. Patching a class swaps it for a mock. New instances appear by *calling the class*. So you reach the "mock instance" by examining the return value of the mocked class.

The snippet below contains a function `some_function` that builds a `Foo` and invokes one of its methods. The [`patch()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch) call swaps the class `Foo` for a mock. Since the `Foo` instance comes from calling the mock, you set it up by adjusting the mock's [`return_value`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.return_value).

```python
>>> def some_function():
...     instance = module.Foo()
...     return instance.method()
...
>>> with patch('module.Foo') as mock:
...     instance = mock.return_value
...     instance.method.return_value = 'the result'
...     result = some_function()
...     assert result == 'the result'

```

[Subject index](INDEX.md) · [Previous](mock-for-method-calls-on-an-object.md) · [Continue](naming-your-mocks.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
