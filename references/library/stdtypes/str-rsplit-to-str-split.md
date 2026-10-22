# stdtypes: `str.rsplit()`, `str.rstrip()`, `str.split()`

str.rsplit(*sep=None*, *maxsplit=-1*)

Yields a list holding the words of the string, taking *sep* as the delimiter string. When *maxsplit* is supplied, no more than *maxsplit* splits occur, taken from the *rightmost* side. When *sep* is absent or `None`, any whitespace string serves as a separator. Aside from splitting starting at the right, `rsplit()` works just like `split()`, which is covered thoroughly below.

 str.rstrip(*chars=None*, */*)

Yields a copy of the string from which trailing characters have been dropped. The *chars* argument is a string naming the collection of characters to drop. When left out or set to `None`, the *chars* argument falls back to dropping whitespace. The *chars* argument is not treated as a suffix; instead, each combination of its members gets stripped. Consider this:

```pycon
>>> '   spacious   '.rstrip()
'   spacious'
>>> 'mississippi'.rstrip('ipz')
'mississ'

```

Refer to `removesuffix()` for a method that drops one single suffix string in place of any character drawn from a set. Consider this:

```python
>>> 'Monty Python'.rstrip(' Python')
'M'
>>> 'Monty Python'.removesuffix(' Python')
'Monty'

```

See also `strip()`.

 str.split(*sep=None*, *maxsplit=-1*)

Yields a list holding the words of the string, taking *sep* as the delimiter string. When *maxsplit* is supplied, no more than *maxsplit* splits occur (so the list holds at most `maxsplit+1` elements). When *maxsplit* is absent or `-1`, the number of splits is unbounded (every possible split is made).

When *sep* is provided, back-to-back delimiters are not merged and are taken to bound empty strings (for instance, `'1,,2'.split(',')` returns `['1', '', '2']`). The *sep* argument may be several characters forming a single delimiter (to split using several delimiters, reach for [`re.split()`](https://docs.python.org/3.14/library/re.html#re.split)). Splitting an empty string when a separator is given returns `['']`.

Consider this:

```pycon
>>> '1,2,3'.split(',')
['1', '2', '3']
>>> '1,2,3'.split(',', maxsplit=1)
['1', '2,3']
>>> '1,2,,3,'.split(',')
['1', '2', '', '3', '']
>>> '1<>2<>3<4'.split('<>')
['1', '2', '3<4']

```

When *sep* is absent or is `None`, a different splitting routine kicks in: stretches of back-to-back whitespace count as one separator, and the outcome carries no empty strings at either edge when the string has leading or trailing whitespace. As a result, splitting an empty string, or a string made entirely of whitespace, with a `None` separator returns `[]`.

Consider this:

```pycon
>>> '1 2 3'.split()
['1', '2', '3']
>>> '1 2 3'.split(maxsplit=1)
['1', '2 3']
>>> '   1   2   3   '.split()
['1', '2', '3']

```

When *sep* is absent or is `None` while *maxsplit* equals `0`, only leading stretches of back-to-back whitespace are taken into account.

Consider this:

```pycon
>>> "".split(None, 0)
[]
>>> "   ".split(None, 0)
[]
>>> "   foo   ".split(maxsplit=0)
['foo   ']

```

See also `join()` and `rsplit()`.

[Subject index](INDEX.md) · [Previous](str-replace-to-str-rpartition.md) · [Continue](str-splitlines-to-str-startswith.md) · [Owning module, declaration or section: String Methods](str-capitalize-to-str-count.md)
