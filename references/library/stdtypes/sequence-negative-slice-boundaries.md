# Common Sequence Operations - Contract: When *i* or *j* is below `-len(s)`, use `0`.

When *i* or *j* is below `-len(s)`, use `0`.

  - When *i* or *j* exceeds `len(s)`, use `len(s)`.

  - When *i* is at least as large as *j*, the slice comes out empty.

5.

The slice of *s* from *i* to *j* with step *k* is the sequence of items whose index is `x = i + n*k` for `0 <= n < (j-i)/k`. Put another way, the indices run `i`, `i+k`, `i+2*k`, `i+3*k` and onward, halting upon reaching *j* (yet never taking in *j*). For positive *k*, *i* and *j* get clamped to `len(s)` whenever they exceed it. For negative *k*, *i* and *j* get clamped to `len(s) - 1` whenever they exceed it. Should *i* or *j* be left out or `None`, they turn into "end" values (which end hinges on the sign of *k*). Note that *k* may not be zero. Where *k* is `None`, it counts as `1`.

6.

Joining immutable sequences always yields a fresh object. As a result, assembling a sequence through repeated concatenation incurs a quadratic runtime cost relative to the overall sequence length. For a linear runtime cost instead, you have to move to one of the options below:

  - when joining `str` objects, you can accumulate a list and apply `str.join()` at the finish, or else write into an [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) instance and fetch its value once done

  - when joining `bytes` objects, you can likewise apply `bytes.join()` or [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO), or perform in-place concatenation using a `bytearray` object. `bytearray` objects are mutable and carry an efficient overallocation mechanism

  - when joining `tuple` objects, extend a `list` in their place

  - for any other types, consult that class's documentation

7.

A handful of sequence types (`range` for one) admit only item sequences obeying fixed patterns, so they offer no sequence concatenation or repetition.

8.

When *i* lies beyond the sequence range, an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) gets raised.

Sequence Methods

Sequence types furthermore support the methods below:

[Subject index](INDEX.md) · [Previous](sequence-operations-overview.md) · [Continue](sequence-count-to-sequence-index.md) · [Owning module, declaration or section: Common Sequence Operations](sequence-operations-overview.md)
