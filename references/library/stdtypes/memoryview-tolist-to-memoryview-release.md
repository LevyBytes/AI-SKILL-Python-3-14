# stdtypes / bytes, bytearray, memoryview / Memory Views: `tolist()`, `toreadonly()`, `release()`

tolist()

Hand back the buffer's data as a list of elements.

```python
>>> memoryview(b'abc').tolist()
[97, 98, 99]
>>> import array
>>> a = array.array('d', [1.1, 2.2, 3.3])
>>> m = memoryview(a)
>>> m.tolist()
[1.1, 2.2, 3.3]

```

Changed in version 3.3: `tolist()` now handles every single-character native format written in [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module syntax, along with multi-dimensional representations.

 toreadonly()

Hand back a read-only counterpart of the memoryview object. The original memoryview object stays as it was.

```python
>>> m = memoryview(bytearray(b'abc'))
>>> mm = m.toreadonly()
>>> mm.tolist()
[97, 98, 99]
>>> mm[0] = 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot modify read-only memory
>>> m[0] = 43
>>> mm.tolist()
[43, 98, 99]

```

Added in version 3.8.

 release()

Free the underlying buffer that the memoryview object exposes. Quite a few objects react in particular ways while a view stays open against them (a `bytearray`, for instance, will block resizing for the time being); for that reason, invoking release() is convenient for lifting these limits — and freeing any lingering resources — at the earliest opportunity.

Once you have called this method, every later operation on the view raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) — `release()` being the lone exception, since you may call it more than once:

```python
>>> m = memoryview(b'abc')
>>> m.release()
>>> m[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: operation forbidden on released memoryview object

```

You can achieve a comparable result through the context management protocol, by way of the `with` statement:

```python
>>> with memoryview(b'abc') as m:
...     m[0]
...
97
>>> m[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: operation forbidden on released memoryview object

```

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](memoryview-eq-to-memoryview-hex.md) · [Continue](memoryview-cast-to-memoryview-cast.md) · [Owning module, declaration or section: memoryview](memoryview-class.md) · [Owning module, declaration or section: Memory Views](memory-views-and-memoryview-construction.md)
