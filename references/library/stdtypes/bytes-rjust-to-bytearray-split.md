# stdtypes: `bytes.rjust()`, `bytearray.rjust()`, `bytes.rsplit()`, `bytearray.rsplit()`, `bytes.rstrip()`, `bytearray.rstrip()`, `bytes.split()`, `bytearray.split()`

bytes.rjust(*width*, *fillbyte=b' '*, */*)

 bytearray.rjust(*width*, *fillbyte=b' '*, */*)

Hand back a copy of the object right justified inside a sequence whose length is *width*. The specified *fillbyte* supplies the padding (an ASCII space by default). With `bytes` objects, you get the original sequence back whenever *width* does not exceed `len(s)`.

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

 bytes.rsplit(*sep=None*, *maxsplit=-1*)

 bytearray.rsplit(*sep=None*, *maxsplit=-1*)

Break the binary sequence into subsequences of the same type, treating *sep* as the delimiter string. When *maxsplit* is supplied, no more than *maxsplit* splits happen, taking the *rightmost* ones. When *sep* is left out or set to `None`, any run made up entirely of ASCII whitespace counts as a separator. Apart from working from the right, `rsplit()` acts just like `split()`, which is documented in full further down.

 bytes.rstrip(*bytes=None*, */*)

 bytearray.rstrip(*bytes=None*, */*)

Hand back a copy of the sequence in which the indicated trailing bytes are dropped. The *bytes* argument is a binary sequence naming the collection of byte values to strip. When left out or set to `None`, the *bytes* argument falls back to dropping ASCII whitespace. Note that the *bytes* argument is not treated as a suffix; instead, every combination of its values gets stripped:

```python
>>> b'   spacious   '.rstrip()
b'   spacious'
>>> b'mississippi'.rstrip(b'ipz')
b'mississ'

```

The binary sequence of byte values to drop can be any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). Consult `removesuffix()` for a method that strips a single suffix string instead of an entire set of characters. As an illustration:

```python
>>> b'Monty Python'.rstrip(b' Python')
b'M'
>>> b'Monty Python'.removesuffix(b' Python')
b'Monty'

```

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

 bytes.split(*sep=None*, *maxsplit=-1*)

 bytearray.split(*sep=None*, *maxsplit=-1*)

Break the binary sequence into subsequences of the same type, treating *sep* as the delimiter string. When *maxsplit* is supplied and is non-negative, no more than *maxsplit* splits happen (so the list ends up with at most `maxsplit+1` elements). When *maxsplit* is left out or set to `-1`, the count of splits is unbounded (every possible split is made).

When *sep* is supplied, runs of adjacent delimiters are not collapsed together and are treated as bounding empty subsequences (so, for instance, `b'1,,2'.split(b',')` yields `[b'1', b'', b'2']`). A multibyte sequence may serve as the *sep* argument acting as one delimiter. Splitting an empty sequence with a given separator yields `[b'']` or `[bytearray(b'')]`, depending on which type of object is being split. The *sep* argument may be any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

As an illustration:

```python
>>> b'1,2,3'.split(b',')
[b'1', b'2', b'3']
>>> b'1,2,3'.split(b',', maxsplit=1)
[b'1', b'2,3']
>>> b'1,2,,3,'.split(b',')
[b'1', b'2', b'', b'3', b'']
>>> b'1<>2<>3<4'.split(b'<>')
[b'1', b'2', b'3<4']

```

When *sep* is left out or set to `None`, a different splitting strategy takes over: runs of adjacent ASCII whitespace are counted as one separator, and the outcome holds no empty strings at its beginning or end even if the sequence carries leading or trailing whitespace. As a result, splitting an empty sequence, or one made up entirely of ASCII whitespace, without naming a separator yields `[]`.

As an illustration:

```python
>>> b'1 2 3'.split()
[b'1', b'2', b'3']
>>> b'1 2 3'.split(maxsplit=1)
[b'1', b'2 3']
>>> b'   1   2   3   '.split()
[b'1', b'2', b'3']

```

[Subject index](INDEX.md) · [Previous](bytes-rpartition-to-bytearray-lstrip.md) · [Continue](bytes-strip-to-bytearray-isalpha.md) · [Owning module, declaration or section: Bytes and Bytearray Operations](bytes-count-to-bytearray-removeprefix.md)
