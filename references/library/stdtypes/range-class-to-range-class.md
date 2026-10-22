# stdtypes: `range`

### Ranges

An immutable run of numbers is what the `range` type models, and you'll frequently see it driving a fixed iteration count inside [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loops.

 *class *range(*stop*, */*)

 *class *range(*start*, *stop*, *step=1*, */*)

Whatever you hand the range constructor has to be an integer, meaning either a built-in [`int`](https://docs.python.org/3.14/library/functions.html#int) or any object exposing the [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) special method. Leave out the *step* argument and it falls back to `1`. Leave out the *start* argument and it falls back to `0`. A *step* of zero triggers [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

When *step* is positive, the elements of a range `r` follow from the formula `r[i] = start + step*i`, subject to `i >= 0` and `r[i] < stop`.

When *step* is negative, that same formula `r[i] = start + step*i` still applies, though now the bounds become `i >= 0` and `r[i] > stop`.

Whenever `r[0]` fails to satisfy the value constraint, the range comes out empty. Negative indices are accepted by ranges, where they count back from the tail of the sequence laid out by the positive indices.

You may build ranges whose absolute magnitudes exceed [`sys.maxsize`](https://docs.python.org/3.14/library/sys.html#sys.maxsize), though certain operations (for instance [`len()`](https://docs.python.org/3.14/library/functions.html#len)) can then raise [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError).

Range examples:

```python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0))
[]
>>> list(range(1, 0))
[]

```

Ranges offer every common sequence operation save concatenation and repetition (the reason being that a range object can only stand for a sequence obeying a rigid pattern, and concatenation or repetition would typically break that pattern).

[Subject index](INDEX.md) · [Previous](tuples.md) · [Continue](ranges.md)
