# unittest.mock — patch — Code example: >>> thing = object()

```python
>>> thing = object()
>>> with patch('__main__.thing', new_callable=NonCallableMock) as mock_thing:
...     assert thing is mock_thing
...     thing()
...
Traceback (most recent call last):
  ...
TypeError: 'NonCallableMock' object is not callable

```

Yet another scenario could be swapping an object for an [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) instance:

```python
>>> from io import StringIO
>>> def foo():
...     print('Something')
...
>>> @patch('sys.stdout', new_callable=StringIO)
... def test(mock_stdout):
...     foo()
...     assert mock_stdout.getvalue() == 'Something\n'
...
>>> test()

```

[Subject index](INDEX.md) · [Previous](unittest-mock-patch.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: patch](patch.md) · [Owning module, declaration or section: unittest.mock.patch](unittest-mock-patch.md) · [Required continuation of the source contract](patch.md)
