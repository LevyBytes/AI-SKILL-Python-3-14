# fnmatch`fnmatch` - Unix filename pattern matching

### `fnmatch` - Unix filename pattern matching

**Source code:** [Lib/fnmatch.py](https://github.com/python/cpython/tree/3.14/Lib/fnmatch.py)

---

This module backs Unix shell-style wildcards, which are *not* equivalent to regular expressions (those get their own writeup in the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module). Shell-style wildcards draw on these special characters:

| Pattern | Meaning |
| --- | --- |
| `*` | stands in for anything at all |
| `?` | stands in for one character of any kind |
| `[seq]` | accepts any character drawn from *seq* |
| `[!seq]` | accepts any character absent from *seq* |

To match one literally, enclose the meta-characters in brackets; `'[?]'`, for instance, matches the character `'?'`.

Keep in mind that the filename separator (`'/'` under Unix) carries *no* special meaning for this module. Turn to the [`glob`](https://docs.python.org/3.14/library/glob.html#module-glob) module for pathname expansion (`glob` leans on `filter()` to match segments of a pathname). In the same way, a filename beginning with a period gets no special handling here and is matched by the `*` and `?` patterns.

Absent a note to the contrary, “filename string” and “pattern string” point at either [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects or `ISO-8859-1` encoded [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects. Be aware that the functions covered below forbid pairing a `bytes` pattern with a `str` filename, and the reverse as well.

One last point: [`functools.lru_cache()`](https://docs.python.org/3.14/library/functools.html#functools.lru_cache) set to a *maxsize* of 32768 caches the (typed) compiled regex patterns across these functions: `fnmatch()`, `fnmatchcase()`, `filter()`, `filterfalse()`.

 fnmatch.fnmatch(*name*, *pat*)

Checks whether the filename string *name* lines up with the pattern string *pat*, giving back `True` or `False`. Both arguments first run through case normalization via [`os.path.normcase()`](https://docs.python.org/3.14/library/os.path.html#os.path.normcase). For a case-sensitive comparison — whatever the operating system's usual behavior — reach for `fnmatchcase()`.

The example here prints every filename in the working directory whose extension is `.txt`:

```python
import fnmatch
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
        print(file)

```

 fnmatch.fnmatchcase(*name*, *pat*)

Checks whether the filename string *name* lines up with the pattern string *pat*, giving back `True` or `False`; this comparison is case-sensitive and skips [`os.path.normcase()`](https://docs.python.org/3.14/library/os.path.html#os.path.normcase).

 fnmatch.filter(*names*, *pat*)

Builds a list out of the entries in the [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) of filename strings *names* that line up with the pattern string *pat*. It comes to the same thing as `[n for n in names if fnmatch(n, pat)]`, only carried out more efficiently.

 fnmatch.filterfalse(*names*, *pat*)

Builds a list out of the entries in the [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) of filename strings *names* that fail to line up with the pattern string *pat*. It comes to the same thing as `[n for n in names if not fnmatch(n, pat)]`, only carried out more efficiently.

Added in version 3.14.

 fnmatch.translate(*pat*)

Takes the shell-style pattern *pat* and hands back its regular-expression form, ready for use with [`re.match()`](https://docs.python.org/3.14/library/re.html#re.match). The pattern is assumed to be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

Example:

```python
>>> import fnmatch, re
>>>
>>> regex = fnmatch.translate('*.txt')
>>> regex
'(?s:.*\\.txt)\\z'
>>> reobj = re.compile(regex)
>>> reobj.match('foobar.txt')
<re.Match object; span=(0, 10), match='foobar.txt'>

```

See also

Module [`glob`](https://docs.python.org/3.14/library/glob.html#module-glob)

Path expansion in the Unix shell style.

[Subject index](INDEX.md) · [Previous](unix-filename-pattern-matching.md) · [Continue](../fractions/fractions-fraction-class-to-fractions-fraction-class.md)
