# difflib.SequenceMatcher: `get_opcodes()`, `get_grouped_opcodes()`, `ratio()`, `quick_ratio()`, `real_quick_ratio()`

get_opcodes()

Hand back a list of 5-tuples describing how to convert *a* into *b*. Each tuple takes the form `(tag, i1, i2, j1, j2)`. The first tuple has `i1 == j1 == 0`, and every later tuple has its *i1* equal to the *i2* of the tuple before it and, similarly, its *j1* equal to the earlier *j2*.

The *tag* values are strings carrying these meanings:

| Value | Meaning |
| --- | --- |
| `'replace'` | `a[i1:i2]` should be replaced by `b[j1:j2]`. |
| `'delete'` | `a[i1:i2]` should be deleted. Note that `j1 == j2` in this case. |
| `'insert'` | `b[j1:j2]` should be inserted at `a[i1:i1]`. Note that `i1 == i2` in this case. |
| `'equal'` | `a[i1:i2] == b[j1:j2]` (the sub-sequences are equal). |

For example:

```python
>>> a = "qabxcd"
>>> b = "abycdf"
>>> s = SequenceMatcher(None, a, b)
>>> for tag, i1, i2, j1, j2 in s.get_opcodes():
...     print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
...         tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
delete    a[0:1] --> b[0:0]      'q' --> ''
equal     a[1:3] --> b[0:2]     'ab' --> 'ab'
replace   a[3:4] --> b[2:3]      'x' --> 'y'
equal     a[4:6] --> b[3:5]     'cd' --> 'cd'
insert    a[6:6] --> b[5:6]       '' --> 'f'

```

 get_grouped_opcodes(*n=3*)

Hand back a [generator](https://docs.python.org/3.14/glossary.html#term-generator) of groups, each holding up to *n* lines of context.

Beginning from the groups that `get_opcodes()` returns, this method breaks out smaller clusters of change and drops the in-between ranges that hold no changes.

These groups come back in the same format `get_opcodes()` uses.

 ratio()

Hand back a measure of how similar the sequences are, as a float in the range [0, 1].

With T standing for the total count of elements in both sequences and M for the count of matches, this equals 2.0*M / T. Observe that it is `1.0` when the sequences are identical and `0.0` when they share nothing.

Computing it is costly if `get_matching_blocks()` or `get_opcodes()` has not run already, so in that situation you might first reach for `quick_ratio()` or `real_quick_ratio()` to obtain an upper bound.

Note

Caution: What a `ratio()` call returns can hinge on the ordering of the arguments. As an example:

```python
>>> SequenceMatcher(None, 'tide', 'diet').ratio()
0.25
>>> SequenceMatcher(None, 'diet', 'tide').ratio()
0.5

```

 quick_ratio()

Hand back an upper bound on `ratio()` fairly quickly.

 real_quick_ratio()

Hand back an upper bound on `ratio()` very quickly.

The three methods returning the ratio of matching to total characters may yield differing results owing to their different levels of approximation, though `quick_ratio()` and `real_quick_ratio()` are always at least as great as `ratio()`:

```python
>>> s = SequenceMatcher(None, "abcd", "bcde")
>>> s.ratio()
0.75
>>> s.quick_ratio()
0.75
>>> s.real_quick_ratio()
1.0

```

[Subject index](INDEX.md) · [Previous](sequence-matcher-inputs-and-matching-blocks.md) · [Continue](sequencematcher-examples.md) · [Owning module, declaration or section: difflib](difflib-sequencematcher-class.md) · [Owning module, declaration or section: difflib.SequenceMatcher](difflib-sequencematcher-class.md) · [Owning module, declaration or section: SequenceMatcher objects](difflib-sequencematcher-class.md)
