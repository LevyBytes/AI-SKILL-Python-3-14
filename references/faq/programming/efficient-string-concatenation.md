# What is the most efficient way to concatenate many strings together?

### What is the most efficient way to concatenate many strings together?

Since [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) and [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects can't be changed, joining many strings together is inefficient because every concatenation produces a fresh object. In the general case, the overall runtime cost grows quadratically with the combined string length.

To gather many [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects, the advised idiom is to drop them into a list and invoke [`str.join()`](https://docs.python.org/3.14/library/stdtypes.html#str.join) at the very end:

```python
chunks = []
for s in my_strings:
    chunks.append(s)
result = ''.join(chunks)

```

(One more fairly efficient idiom is to employ [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO).)

To gather many [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects, the advised idiom is to grow a [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) object through in-place concatenation (the `+=` operator):

```python
result = bytearray()
for b in my_bytes_objects:
    result += b

```

[Subject index](INDEX.md)
