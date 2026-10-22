# stdtypes: Memoryview element sizes and buffer layout

itemsize

How many bytes each element of the memoryview takes up:

```python
>>> import array, struct
>>> m = memoryview(array.array('H', [32000, 32001, 32002]))
>>> m.itemsize
2
>>> m[0]
32000
>>> struct.calcsize('H') == m.itemsize
True

```

 ndim

An integer reporting the count of dimensions of a multi-dimensional array that the memory stands for.

 shape

A tuple of integers, `ndim` long, that gives the memory's shape viewed as an N-dimensional array.

Changed in version 3.3: With ndim = 0 the result is an empty tuple rather than `None`.

 strides

A tuple of integers, `ndim` long, that gives, for each dimension of the array, the byte count needed to step to each element.

Changed in version 3.3: Where ndim = 0, an empty tuple appears rather than `None`.

 suboffsets

Employed internally for PIL-style arrays. Its value serves only as information.

 c_contiguous

A bool reporting whether the memory is C-[contiguous](https://docs.python.org/3.14/glossary.html#term-contiguous).

Added in version 3.3.

 f_contiguous

A bool reporting whether the memory is Fortran [contiguous](https://docs.python.org/3.14/glossary.html#term-contiguous).

Added in version 3.3.

 contiguous

A bool reporting whether the memory is [contiguous](https://docs.python.org/3.14/glossary.html#term-contiguous).

Added in version 3.3.

To learn about the thread safety of `memoryview` objects under the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), consult [Thread safety for memoryview objects](https://docs.python.org/3.14/library/threadsafety.html#thread-safety-memoryview).

[Subject index](INDEX.md) · [Previous](memoryview-count-to-memoryview-index.md) · [Continue](set-class-to-frozenset-class.md) · [Owning module, declaration or section: memoryview](memoryview-class.md) · [Owning module, declaration or section: Memory Views](memory-views-and-memoryview-construction.md)
