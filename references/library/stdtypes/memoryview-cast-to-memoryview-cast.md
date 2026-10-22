# Memory Views — Signature and initial contract

cast(*format*, */*)

 cast(*format*, *shape*, */*)

Recast a memoryview into a different format or shape. By default *shape* is `[byte_length//new_itemsize]`, so the resulting view comes out one-dimensional. What you get back is a fresh memoryview, though the buffer is left uncopied. The casts that are permitted are 1D -> C-[contiguous](https://docs.python.org/3.14/glossary.html#term-contiguous) and C-contiguous -> 1D.

The target format may only be a single-element native format expressed in [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) syntax. At least one of the two formats has to be a byte format (‘B’, ‘b’ or ‘c’). The result's byte length has to match the byte length of the original. Bear in mind that every byte length can vary with the operating system.

Cast 1D/long to 1D/unsigned bytes:

```python
>>> import array
>>> a = array.array('l', [1,2,3])
>>> x = memoryview(a)
>>> x.format
'l'
>>> x.itemsize
8
>>> len(x)
3
>>> x.nbytes
24
>>> y = x.cast('B')
>>> y.format
'B'
>>> y.itemsize
1
>>> len(y)
24
>>> y.nbytes
24

```

Cast 1D/unsigned bytes to 1D/char:

```python
>>> b = bytearray(b'zyz')
>>> x = memoryview(b)
>>> x[0] = b'a'
Traceback (most recent call last):
  ...
TypeError: memoryview: invalid type for format 'B'
>>> y = x.cast('c')
>>> y[0] = b'a'
>>> b
bytearray(b'ayz')

```

Cast 1D/bytes to 3D/ints to 1D/signed char:

```python
>>> import struct
>>> buf = struct.pack("i"*12, *list(range(12)))
>>> x = memoryview(buf)
>>> y = x.cast('i', shape=[2,2,3])
>>> y.tolist()
[[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
>>> y.format
'i'
>>> y.itemsize
4
>>> len(y)
2
>>> y.nbytes
48
>>> z = y.cast('b')
>>> z.format
'b'
>>> z.itemsize
1
>>> len(z)
48
>>> z.nbytes
48

```

Cast 1D/unsigned long to 2D/unsigned long:

[Subject index](INDEX.md) · [Previous](memoryview-tolist-to-memoryview-release.md) · [Continue](memory-views-code-example-buf-struct-pack-l-6-list-range-6.md) · [Owning module, declaration or section: memoryview](memoryview-class.md) · [Owning module, declaration or section: Memory Views](memory-views-and-memoryview-construction.md)
