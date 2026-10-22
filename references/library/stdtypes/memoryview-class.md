# stdtypes: `memoryview`

*class *memoryview(*object*)

>

Build a `memoryview` referring to *object*. The given *object* has to implement the buffer protocol. Among the built-in types that implement it are `bytes` and `bytearray`.

Every `memoryview` carries the concept of an *element*, the smallest atomic unit of memory that the source *object* deals in. With many basic types like `bytes` and `bytearray`, that element is just one byte, though other types — for instance [`array.array`](https://docs.python.org/3.14/library/array.html#array.array) — can use larger elements.

`memoryview`s are [generic](https://docs.python.org/3.14/library/typing.html#generics) over the type of their underlying data.

`len(view)` matches the length of `tolist`, the nested-list form of the view. When `view.ndim = 1`, that count is the same as the number of elements held by the view.

Changed in version 3.12: If `view.ndim == 0`, `len(view)` now raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) instead of returning 1.

You can read how many bytes a single element occupies from the `itemsize` attribute.

A `memoryview` permits slicing and indexing as a way to surface its data. Slicing along one dimension produces a subview:

```python
>>> v = memoryview(b'abcefg')
>>> v[1]
98
>>> v[-1]
103
>>> v[1:4]
<memory at 0x7f3ddc9f4350>
>>> bytes(v[1:4])
b'bce'

```

When `format` matches one of the native format specifiers from the [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module, you may also index with an integer or a tuple of integers, and the result is a single *element* of the appropriate type. A one-dimensional memoryview accepts indexing by an integer or by a one-integer tuple. A multi-dimensional one accepts tuples holding precisely *ndim* integers, where *ndim* counts the dimensions. A zero-dimensional one accepts the empty tuple as its index.

The following demonstrates a format that is not byte-based:

```python
>>> import array
>>> a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
>>> m = memoryview(a)
>>> m[0]
-11111111
>>> m[-1]
44444444
>>> m[::2].tolist()
[-11111111, -33333333]

```

When the source object can be written to, the memoryview permits assignment to a one-dimensional slice. Changing the size is forbidden:

```python
>>> data = bytearray(b'abcefg')
>>> v = memoryview(data)
>>> v.readonly
False
>>> v[0] = ord(b'z')
>>> data
bytearray(b'zbcefg')
>>> v[1:4] = b'123'
>>> data
bytearray(b'z123fg')
>>> v[2:3] = b'spam'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: memoryview assignment: lvalue and rvalue have different structures
>>> v[2:6] = b'spam'
>>> data
bytearray(b'z1spam')

```

A one-dimensional memoryview over a [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) (read-only) type whose format is ‘B’, ‘b’ or ‘c’ is itself hashable. Its hash satisfies `hash(m) == hash(m.tobytes())`:

```python
>>> v = memoryview(b'abcefg')
>>> hash(v) == hash(b'abcefg')
True
>>> hash(v[2:4]) == hash(b'ce')
True
>>> hash(v[::-2]) == hash(b'abcefg'[::-2])
True

```

Changed in version 3.3: Slicing of one-dimensional memoryviews became possible. Those with formats ‘B’, ‘b’ or ‘c’ also turned [hashable](https://docs.python.org/3.14/glossary.html#term-hashable).

Changed in version 3.4: memoryview is now registered automatically with [`collections.abc.Sequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Sequence)

Changed in version 3.5: Indexing a memoryview by a tuple of integers became possible.

Changed in version 3.14: memoryview is now a [generic type](https://docs.python.org/3.14/glossary.html#term-generic-type).

`memoryview` has several methods:

[Subject index](INDEX.md) · [Previous](memory-views-and-memoryview-construction.md) · [Continue](memoryview-eq-to-memoryview-hex.md) · [Owning module, declaration or section: Memory Views](memory-views-and-memoryview-construction.md)
