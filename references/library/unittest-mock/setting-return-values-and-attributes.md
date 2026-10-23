# unittest.mock - Setting return values and attributes

### Setting return values and attributes

Configuring the return values on a mock object could hardly be easier:

```python
>>> mock = Mock()
>>> mock.return_value = 3
>>> mock()
3

```

Naturally the same works for methods belonging to the mock:

```python
>>> mock = Mock()
>>> mock.method.return_value = 3
>>> mock.method()
3

```

You may also supply the return value through the constructor:

```python
>>> mock = Mock(return_value=3)
>>> mock()
3

```

Need an attribute set on your mock? Simply set it:

```python
>>> mock = Mock()
>>> mock.x = 3
>>> mock.x
3

```

At times you'll want to mock a trickier arrangement, such as `mock.connection.cursor().execute("SELECT 1")`. To have this call yield a list, we must arrange the outcome of the nested call.

We can lean on [`call`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.call) to build up the collection of calls in a "chained call" this way, making later assertion easy:

```python
>>> mock = Mock()
>>> cursor = mock.connection.cursor.return_value
>>> cursor.execute.return_value = ['foo']
>>> mock.connection.cursor().execute("SELECT 1")
['foo']
>>> expected = call.connection.cursor().execute("SELECT 1").call_list()
>>> mock.mock_calls
[call.connection.cursor(), call.connection.cursor().execute('SELECT 1')]
>>> mock.mock_calls == expected
True

```

Invoking `.call_list()` is what converts our call object into a list of calls standing for the chained calls.

[Subject index](INDEX.md) · [Previous](tracking-all-calls.md) · [Continue](raising-exceptions-with-mocks.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
