# difflib — SequenceMatcher examples

### SequenceMatcher examples

The following example contrasts two strings while treating blanks as "junk":

```python
>>> s = SequenceMatcher(lambda x: x == " ",
...                     "private Thread currentThread;",
...                     "private volatile Thread currentThread;")

```

`ratio()` returns a float in [0, 1] gauging how similar the sequences are. As a rough guideline, a `ratio()` value above 0.6 indicates the sequences are close matches:

```python
>>> print(round(s.ratio(), 3))
0.866

```

When all you care about is where the sequences match, `get_matching_blocks()` comes in handy:

```python
>>> for block in s.get_matching_blocks():
...     print("a[%d] and b[%d] match for %d elements" % block)
a[0] and b[0] match for 8 elements
a[8] and b[17] match for 21 elements
a[29] and b[38] match for 0 elements

```

Observe that the final tuple returned by `get_matching_blocks()` is always a dummy, `(len(a), len(b), 0)`, and this is the sole case where the last tuple element (the number of elements matched) is `0`.

When you want to learn how to turn the first sequence into the second, reach for `get_opcodes()`:

```python
>>> for opcode in s.get_opcodes():
...     print("%6s a[%d:%d] b[%d:%d]" % opcode)
 equal a[0:8] b[0:8]
insert a[8:8] b[8:17]
 equal a[8:29] b[17:38]

```

See also

- The `get_close_matches()` function in this module, which shows how a little code built atop `SequenceMatcher` can accomplish something useful.

- [Simple version control recipe](https://code.activestate.com/recipes/576729-simple-version-control/) for a small application built with `SequenceMatcher`.

[Subject index](INDEX.md) · [Previous](sequence-matcher-opcodes-and-similarity.md) · [Continue](difflib-differ-class.md) · [Owning module, declaration or section: difflib](difflib-sequencematcher-class.md)
