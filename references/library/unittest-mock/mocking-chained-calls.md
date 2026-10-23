# unittest.mock - Mocking chained calls

### Mocking chained calls

Once you grasp the [`return_value`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.return_value) attribute, mocking chained calls turns out to be quite easy with mock. The first time a mock is called - or whenever you read its `return_value` before any call - a fresh [`Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock) springs into existence.

That means you can observe how the object handed back from a call to a mocked object got used by inspecting the `return_value` mock:

```python
>>> mock = Mock()
>>> mock().foo(a=2, b=3)
<Mock name='mock().foo()' id='...'>
>>> mock.return_value.foo.assert_called_with(a=2, b=3)

```

From there it's a short hop to configuring and then asserting on chained calls. Naturally, one other option is to write your code more testably to begin with…

So, imagine we have some code resembling this:

```python
>>> class Something:
...     def __init__(self):
...         self.backend = BackendProvider()
...     def method(self):
...         response = self.backend.get_endpoint('foobar').create_call('spam', 'eggs').start_call()
...         # more code

```

Granting that `BackendProvider` is already thoroughly tested, how should we test `method()`? In particular, we want to confirm that the `# more code` portion handles the response object the right way.

Since an instance attribute is where this call chain originates, the `backend` attribute on a `Something` instance is something we can monkey patch. Here we care solely about the return value from the last call to `start_call`, so there isn't much to configure. Suppose the object it returns is 'file-like'; we'll then make our response object adopt the builtin [`open()`](https://docs.python.org/3.14/library/functions.html#open) as its `spec`.

For this, we build a mock instance to be our mock backend along with a mock response object for it. To make the response the return value of that final `start_call`, we could write:

```python
mock_backend.get_endpoint.return_value.create_call.return_value.start_call.return_value = mock_response

```

A somewhat tidier route uses the [`configure_mock()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.configure_mock) method to set the return value for us directly:

```python
>>> something = Something()
>>> mock_response = Mock(spec=open)
>>> mock_backend = Mock()
>>> config = {'get_endpoint.return_value.create_call.return_value.start_call.return_value': mock_response}
>>> mock_backend.configure_mock(**config)

```

Armed with these we monkey patch the "mock backend" into place and can issue the real call:

```python
>>> something.backend = mock_backend
>>> something.method()

```

Through [`mock_calls`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.mock_calls) we can verify the chained call with one assert. A chained call packs several calls into a single line of code, so `mock_calls` will hold several entries. We can call on [`call.call_list()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.call.call_list) to build that list of calls for us:

```python
>>> chained = call.get_endpoint('foobar').create_call('spam', 'eggs').start_call()
>>> call_list = chained.call_list()
>>> assert mock_backend.mock_calls == call_list

```

[Subject index](INDEX.md) · [Previous](further-examples.md) · [Continue](partial-mocking.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
