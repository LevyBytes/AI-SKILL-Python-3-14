# stdtypes / bytes, bytearray, memoryview / Memory Views: `__eq__()`, `tobytes()`, `hex()`

__eq__(*exporter*)

A memoryview compares equal to a [**PEP 3118**](https://peps.python.org/pep-3118/) exporter when their shapes line up and every matching pair of values is equal once each operand's format code is read through [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) syntax.

Within the subset of [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) format strings that `tolist()` presently handles, `v` and `w` count as equal when `v.tolist() == w.tolist()`:

```python
>>> import array
>>> a = array.array('I', [1, 2, 3, 4, 5])
>>> b = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
>>> c = array.array('b', [5, 3, 1])
>>> x = memoryview(a)
>>> y = memoryview(b)
>>> x == a == y == b
True
>>> x.tolist() == a.tolist() == y.tolist() == b.tolist()
True
>>> z = y[::-2]
>>> z == c
True
>>> z.tolist() == c.tolist()
True

```

Should either of the format strings fall outside what the [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module handles, the objects always compare unequal — and that holds even when the format strings together with the buffer contents are identical:

```python
>>> from ctypes import BigEndianStructure, c_long
>>> class BEPoint(BigEndianStructure):
...     _fields_ = [("x", c_long), ("y", c_long)]
...
>>> point = BEPoint(100, 200)
>>> a = memoryview(point)
>>> b = memoryview(point)
>>> a == point
False
>>> a == b
False

```

Keep in mind that, much like with floating-point numbers, `v is w` carries *no* guarantee that `v == w` holds for memoryview objects.

Changed in version 3.3: Earlier releases looked at the raw memory alone, ignoring both the item format and the logical structure of the array.

 tobytes(*order='C'*)

Hand back the buffer's data as a bytestring. Doing so is the same as invoking the `bytes` constructor on the memoryview.

```python
>>> m = memoryview(b"abc")
>>> m.tobytes()
b'abc'
>>> bytes(m)
b'abc'

```

When arrays are non-contiguous, the result matches the flattened list form with every element turned into bytes. `tobytes()` accepts all format strings, even those outside [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module syntax.

Added in version 3.8: *order* may take {‘C’, ‘F’, ‘A’}. With *order* set to ‘C’ or ‘F’, the original array's data is recast into C or Fortran order respectively. Where the view is contiguous, ‘A’ yields a faithful copy of the physical memory; notably, Fortran order in memory carries through unchanged. Where the view is non-contiguous, the data first goes to C order. Passing *order=None* behaves like *order=’C’*.

 hex(***, *bytes_per_sep=1*)

 hex(*sep*, *bytes_per_sep=1*)

Hand back a string holding two hexadecimal digits per byte of the buffer.

```python
>>> m = memoryview(b"abc")
>>> m.hex()
'616263'

```

Added in version 3.5.

Changed in version 3.8: As with `bytes.hex()`, the `memoryview.hex()` method now accepts the optional *sep* and *bytes_per_sep* parameters for placing separators among the bytes of its hex output.

[Subject index](INDEX.md) · [Previous](memoryview-class.md) · [Continue](memoryview-tolist-to-memoryview-release.md) · [Owning module, declaration or section: memoryview](memoryview-class.md) · [Owning module, declaration or section: Memory Views](memory-views-and-memoryview-construction.md)
