# Memory Views — Code example: >>> buf = struct.pack("L"*6, *list(range(6)))

```python
>>> buf = struct.pack("L"*6, *list(range(6)))
>>> x = memoryview(buf)
>>> y = x.cast('L', shape=[2,3])
>>> len(y)
2
>>> y.nbytes
48
>>> y.tolist()
[[0, 1, 2], [3, 4, 5]]

```

Added in version 3.3.

Changed in version 3.5: Casting to a byte view no longer places any restriction on the source format.

[Subject index](INDEX.md) · [Previous](memoryview-cast-to-memoryview-cast.md) · [Continue](memoryview-count-to-memoryview-index.md) · [Owning module, declaration or section: memoryview](memoryview-class.md) · [Owning module, declaration or section: Memory Views](memory-views-and-memoryview-construction.md) · [Owning module, declaration or section: cast; cast](memoryview-cast-to-memoryview-cast.md)
