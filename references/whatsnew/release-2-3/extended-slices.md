# Python 2.3 changes: Extended slice syntax and operations

### Extended Slices

Going all the way back to Python 1.4, the slicing syntax has allowed an optional third “step” or “stride” argument. As examples, every one of these is valid Python syntax: `L[1:10:2]`, `L[:-1:1]`, `L[::-1]`. The Numerical Python developers asked for this, since their code leans on the third argument heavily. Yet Python's built-in list, tuple, and string sequence types never honored the feature, throwing a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when you attempted it. A patch from Michael Hudson addressed this gap.

As an illustration, pulling out a list's elements at even indexes is now trivial:

```python
>>> L = range(10)
>>> L[::2]
[0, 2, 4, 6, 8]

```

Using negative values likewise yields a reversed copy of that same list:

```python
>>> L[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

```

The same applies to tuples, arrays, and strings:

```python
>>> s='abcd'
>>> s[::2]
'ac'
>>> s[::-1]
'dcba'

```

Given a mutable sequence — a list or an array, say — assigning to or removing an extended slice is permitted, though the behavior on extended slices isn't identical to assigning on plain ones. An assignment to a regular slice can alter the length of the sequence:

```python
>>> a = range(3)
>>> a
[0, 1, 2]
>>> a[1:3] = [4, 5, 6]
>>> a
[0, 4, 5, 6]

```

Extended slices lack that flexibility. When you assign to one, the list on the right-hand side of the statement has to hold exactly as many items as the slice being replaced:

```python
>>> a = range(4)
>>> a
[0, 1, 2, 3]
>>> a[::2]
[0, 2]
>>> a[::2] = [0, -1]
>>> a
[0, 1, -1, 3]
>>> a[::2] = [0,1,2]
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ValueError: attempt to assign sequence of size 3 to extended slice of size 2

```

Deletion is simpler:

```python
>>> a = range(4)
>>> a
[0, 1, 2, 3]
>>> a[::2]
[0, 2]
>>> del a[::2]
>>> a
[1, 3]

```

Slice objects may now also be passed to the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) methods of the built-in sequences:

```python
>>> range(10).__getitem__(slice(0, 5, 2))
[0, 2, 4]

```

[Subject index](INDEX.md) · [Previous source section](pep-307-pickle-enhancements.md) · [Next source section](extended-slices-fakeseq.md) · [Release/subject declaration](standard-set-type.md)
