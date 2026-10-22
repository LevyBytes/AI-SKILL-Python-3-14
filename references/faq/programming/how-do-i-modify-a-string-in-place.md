# How do I modify a string in place?

### How do I modify a string in place?

That isn't possible, since strings are immutable. In the majority of cases, you should just build a fresh string out of the pieces you intend to combine. That said, when you require an object that can modify Unicode data in-place, consider an [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) object or the [`array`](https://docs.python.org/3.14/library/array.html#module-array) module:

```python
>>> import io
>>> s = "Hello, world"
>>> sio = io.StringIO(s)
>>> sio.getvalue()
'Hello, world'
>>> sio.seek(7)
7
>>> sio.write("there!")
6
>>> sio.getvalue()
'Hello, there!'

>>> import array
>>> a = array.array('w', s)
>>> print(a)
array('w', 'Hello, world')
>>> a[0] = 'y'
>>> print(a)
array('w', 'yello, world')
>>> a.tounicode()
'yello, world'

```

[Subject index](INDEX.md)
