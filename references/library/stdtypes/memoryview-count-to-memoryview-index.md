# stdtypes / bytes, bytearray, memoryview / Memory Views: `count()`, `index()`

count(*value*, */*)

Tally how often *value* appears.

Added in version 3.14.

 index(*value*, *start=0*, *stop=sys.maxsize*, */*)

>

Hand back the index where *value* first appears (at or past index *start* and ahead of index *stop*).

Raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) if *value* cannot be found.

Added in version 3.14.

There are also several readonly attributes available:

 obj

The memoryview's underlying object:

```python
>>> b  = bytearray(b'xyz')
>>> m = memoryview(b)
>>> m.obj is b
True

```

Added in version 3.3.

 nbytes

`nbytes == product(shape) * itemsize == len(m.tobytes())`. This figure is how many bytes of space the array would take up were it laid out contiguously. It does not have to equal `len(m)`:

```python
>>> import array
>>> a = array.array('i', [1,2,3,4,5])
>>> m = memoryview(a)
>>> len(m)
5
>>> m.nbytes
20
>>> y = m[::2]
>>> len(y)
3
>>> y.nbytes
12
>>> len(y.tobytes())
12

```

Multi-dimensional arrays:

```python
>>> import struct
>>> buf = struct.pack("d"*12, *[1.5*x for x in range(12)])
>>> x = memoryview(buf)
>>> y = x.cast('d', shape=[3,4])
>>> y.tolist()
[[0.0, 1.5, 3.0, 4.5], [6.0, 7.5, 9.0, 10.5], [12.0, 13.5, 15.0, 16.5]]
>>> len(y)
3
>>> y.nbytes
96

```

Added in version 3.3.

 readonly

A bool reporting whether the memory is read only.

 format

A string giving the format (written in [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module style) of each element within the view. You can build a memoryview from exporters carrying arbitrary format strings, yet certain methods (`tolist()`, for example) only work with native single-element formats.

Changed in version 3.3: the `'B'` format is now interpreted per struct module syntax. Consequently `memoryview(b'abc')[0] == b'abc'[0] == 97`.

[Subject index](INDEX.md) · [Previous](memory-views-code-example-buf-struct-pack-l-6-list-range-6.md) · [Continue](memory-views.md) · [Owning module, declaration or section: memoryview](memoryview-class.md) · [Owning module, declaration or section: Memory Views](memory-views-and-memoryview-construction.md)
