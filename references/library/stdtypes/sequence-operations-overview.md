# Common Sequence Operations - Section introduction and initial examples

### Common Sequence Operations

Most sequence types, whether mutable or immutable, support the operations laid out in the table below. The [`collections.abc.Sequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Sequence) ABC exists to ease correct implementation of these operations on your own sequence types.

This table presents the sequence operations in order of rising priority. Throughout the table, *s* and *t* denote sequences of one type, *n*, *i*, *j* and *k* denote integers, and *x* denotes any object that satisfies whatever type and value limits *s* imposes.

The `in` and `not in` operations carry the same priorities as the comparison operations do. The `+` (concatenation) and `*` (repetition) operations carry the same priority as their numeric counterparts. [3]

| Operation | Result | Notes |
| --- | --- | --- |
| `x in s` | `True` if an item of *s* is equal to *x*, else `False` | (1) |
| `x not in s` | `False` if an item of *s* is equal to *x*, else `True` | (1) |
| `s + t` | the concatenation of *s* and *t* | (6)(7) |
| `s * n` or `n * s` | equivalent to adding *s* to itself *n* times | (2)(7) |
| `s[i]` | *i*th item of *s*, origin 0 | (3)(8) |
| `s[i:j]` | slice of *s* from *i* to *j* | (3)(4) |
| `s[i:j:k]` | slice of *s* from *i* to *j* with step *k* | (3)(5) |
| `len(s)` | length of *s* |  |
| `min(s)` | smallest item of *s* |  |
| `max(s)` | largest item of *s* |  |

Comparisons are likewise supported by sequences of one and the same type. Tuples and lists in particular get compared lexicographically, element against corresponding element. So equality requires that every element compares equal and that both sequences share the same type and the same length. (The language reference's [Comparisons](https://docs.python.org/3.14/reference/expressions.html#comparisons) section spells out the complete details.)

Both forward and reversed iterators over mutable sequences reach values through an index. That index keeps advancing (or retreating) even should the underlying sequence get mutated. The iterator stops only upon hitting an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) or a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) (or once the index falls below zero).

Notes:

1.

Although the `in` and `not in` operations ordinarily serve plain membership testing, certain specialised sequences (`str`, `bytes` and `bytearray` among them) additionally employ them for subsequence testing:

```python
>>> "gg" in "eggs"
True

```

2.

Any *n* below `0` is handled as `0` (giving back an empty sequence whose type matches *s*). Be aware that the items inside sequence *s* are not duplicated; they get referenced again and again. This regularly trips up newcomers to Python; take this case:

```python
>>> lists = [[]] * 3
>>> lists
[[], [], []]
>>> lists[0].append(3)
>>> lists
[[3], [3], [3]]

```

What occurred is that `[[]]` is a single-element list holding one empty list, so each of the three entries in `[[]] * 3` references that one empty list. Changing any entry of `lists` changes that one list. Here is how to build a list made of distinct lists instead:

```python
>>> lists = [[] for i in range(3)]
>>> lists[0].append(3)
>>> lists[1].append(5)
>>> lists[2].append(7)
>>> lists
[[3], [5], [7]]

```

The FAQ entry [How do I create a multidimensional list?](https://docs.python.org/3.14/faq/programming.html#faq-multidimensional-list) offers more on this.

3.

Should *i* or *j* be negative, the index counts back from the end of sequence *s*: `len(s) + i` or `len(s) + j` takes its place. Note, however, that `-0` remains `0`.

4.

The slice of *s* from *i* to *j* is the sequence of items whose index *k* satisfies `i <= k < j`.

  - When *i* is left out or `None`, use `0`.

  - When *j* is left out or `None`, use `len(s)`.

  -

[Subject index](INDEX.md) · [Previous](sequence-types-list-tuple-range.md) · [Continue](sequence-negative-slice-boundaries.md)
