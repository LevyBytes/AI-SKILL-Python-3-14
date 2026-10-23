# unittest.mock - mock_open

### mock_open

 unittest.mock.mock_open(*mock=None*, *read_data=''*)

This helper builds a mock that stands in for [`open()`](https://docs.python.org/3.14/library/functions.html#open). It handles both a direct `open()` call and use as a context manager.

The *mock* argument names the mock object you wish to set up. Leave it `None` (the default) and a `MagicMock` is built for you, its API trimmed to the methods and attributes found on ordinary file handles.

*read_data* supplies the string handed back by the file handle's [`read()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.read), [`readline()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readline), and [`readlines()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readlines) methods. Each of those methods draws from *read_data* until nothing remains. The mocking of these methods stays rather basic: on every call to the *mock*, *read_data* is reset to the beginning. Should you need finer control over the data fed into the code under test, you will have to tailor this mock yourself. And where even that falls short, one of the in-memory filesystem packages on [PyPI](https://pypi.org) can supply a lifelike filesystem for tests.

Changed in version 3.4: [`readline()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readline) and [`readlines()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readlines) support was added. The mock of [`read()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.read) was changed to consume *read_data* instead of handing it back on every call.

Changed in version 3.5: *read_data* now resets with each call to the *mock*.

Changed in version 3.8: [`__iter__()`](https://docs.python.org/3.14/library/stdtypes.html#container.__iter__) was added to the implementation so that iterating (for instance in for loops) properly consumes *read_data*.

Treating [`open()`](https://docs.python.org/3.14/library/functions.html#open) as a context manager is an excellent and increasingly popular way to guarantee your file handles get closed cleanly:

```python
with open('/some/path', 'w') as f:
    f.write('something')

```

The snag is that, even after you mock out the [`open()`](https://docs.python.org/3.14/library/functions.html#open) call, the *returned object* is the thing actually used as the context manager (the one whose [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) and [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) get invoked).

Because mocking context managers via a `MagicMock` comes up so often and is so finicky, a dedicated helper function earns its keep.

```python
>>> m = mock_open()
>>> with patch('__main__.open', m):
...     with open('foo', 'w') as h:
...         h.write('some stuff')
...
>>> m.mock_calls
[call('foo', 'w'),
 call().__enter__(),
 call().write('some stuff'),
 call().__exit__(None, None, None)]
>>> m.assert_called_once_with('foo', 'w')
>>> handle = m()
>>> handle.write.assert_called_once_with('some stuff')

```

And to read files:

```python
>>> with patch('__main__.open', mock_open(read_data='bibble')) as m:
...     with open('foo') as h:
...         result = h.read()
...
>>> m.assert_called_once_with('foo')
>>> assert result == 'bibble'

```

[Subject index](INDEX.md) · [Previous](unittest-mock-filter-dir.md) · [Continue](autospeccing-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
