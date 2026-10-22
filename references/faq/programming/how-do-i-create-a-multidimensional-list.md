# How do I create a multidimensional list?

### How do I create a multidimensional list?

Odds are you attempted to build a multidimensional array along these lines:

```python
>>> A = [[None] * 2] * 3

```

Printing it makes it appear correct:

```pycon
>>> A
[[None, None], [None, None], [None, None]]

```

Yet upon assigning a value, it turns up in several places:

```pycon
>>> A[0][0] = 5
>>> A
[[5, None], [5, None], [5, None]]

```

This happens because duplicating a list with `*` produces no copies; it merely produces references to the already-existing objects. The `*3` builds a list holding 3 references to one and the same list of length two. Modifications to a single row will appear across every row, which is almost surely not your intent.

The recommended way is to build a list of the wanted length first, then populate each element with a freshly built list:

```python
A = [None] * 3
for i in range(3):
    A[i] = [None] * 2

```

This produces a list holding 3 distinct lists of length two. A list comprehension works as well:

```python
w, h = 2, 3
A = [[None] * w for i in range(h)]

```

Alternatively, you can use an extension that supplies a matrix datatype; [NumPy](https://numpy.org/) is the most widely known.

[Subject index](INDEX.md)
