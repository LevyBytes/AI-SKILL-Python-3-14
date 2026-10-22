# What's New In Python 3.2 / io — io

### io

A fresh method, [`getbuffer()`](https://docs.python.org/3.14/library/io.html#io.BytesIO.getbuffer), now lives on [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) and behaves much like [`memoryview()`](https://docs.python.org/3.14/library/stdtypes.html#memoryview). The view it returns is writable and shares the underlying data rather than duplicating it. Because the buffer permits random access plus slice syntax, it lends itself nicely to editing in place:

```python
>>> REC_LEN, LOC_START, LOC_LEN = 34, 7, 11

>>> def change_location(buffer, record_number, location):
...     start = record_number * REC_LEN + LOC_START
...     buffer[start: start+LOC_LEN] = location

>>> import io

>>> byte_stream = io.BytesIO(
...     b'G3805  storeroom  Main chassis    '
...     b'X7899  shipping   Reserve cog     '
...     b'L6988  receiving  Primary sprocket'
... )
>>> buffer = byte_stream.getbuffer()
>>> change_location(buffer, 1, b'warehouse  ')
>>> change_location(buffer, 0, b'showroom   ')
>>> print(byte_stream.getvalue())
b'G3805  showroom   Main chassis    '
b'X7899  warehouse  Reserve cog     '
b'L6988  receiving  Primary sprocket'

```

(Contributed by Antoine Pitrou in [bpo-5506](https://bugs.python.org/issue?@action=redirect&bpo=5506).)

[Subject index](INDEX.md) · [Previous source section](abc.md) · [Next source section](reprlib.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
