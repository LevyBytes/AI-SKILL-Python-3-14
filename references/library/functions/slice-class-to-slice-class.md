# Built-in Functions

*class *slice(*stop*, */*)

 *class *slice(*start*, *stop*, *step=None*, */*)

Hand back a [slice](https://docs.python.org/3.14/glossary.html#term-slice) object that stands for the collection of indices described by `range(start, stop, step)`. The *start* and *step* arguments fall back to `None`.

Slice objects come into being as well whenever [slicing syntax](https://docs.python.org/3.14/reference/expressions.html#slicings) appears. Take, for instance: `a[start:stop:step]` or `a[start:stop, i]`.

Look to [`itertools.islice()`](https://docs.python.org/3.14/library/itertools.html#itertools.islice) for a different version that hands back an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator).

[Subject index](INDEX.md) · [Previous](setattr.md) · [Continue](sorted.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
