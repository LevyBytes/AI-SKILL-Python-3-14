# stdtypes: `str.splitlines()`, `str.startswith()`

str.splitlines(*keepends=False*)

Yields a list holding the lines of the string, breaking at line boundaries. The resulting list leaves line breaks out unless *keepends* is supplied and true.

The breaks this method splits on are the following line boundaries. Notably, these boundaries form a superset of [universal newlines](https://docs.python.org/3.14/glossary.html#term-universal-newlines).

| Representation | Description |
| --- | --- |
| `\n` | Line Feed |
| `\r` | Carriage Return |
| `\r\n` | Carriage Return + Line Feed |
| `\v` or `\x0b` | Line Tabulation |
| `\f` or `\x0c` | Form Feed |
| `\x1c` | File Separator |
| `\x1d` | Group Separator |
| `\x1e` | Record Separator |
| `\x85` | Next Line (C1 Control Code) |
| `\u2028` | Line Separator |
| `\u2029` | Paragraph Separator |

Changed in version 3.2: `\v` and `\f` added to list of line boundaries.

Consider this:

```python
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines()
['ab c', '', 'de fg', 'kl']
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
['ab c\n', '\n', 'de fg\r', 'kl\r\n']

```

In contrast to `split()` when a delimiter string *sep* is supplied, this method gives back an empty list for the empty string, and a closing line break does not produce one extra line:

```python
>>> "".splitlines()
[]
>>> "One line\n".splitlines()
['One line']

```

By way of comparison, `split('\n')` produces:

```python
>>> ''.split('\n')
['']
>>> 'Two lines\n'.split('\n')
['Two lines', '']

```

 str.startswith(*prefix*[, *start*[, *end*]])

Yields `True` when the string begins with the *prefix*, and `False` otherwise. *prefix* may also be a tuple of prefixes to test for. Supplying the optional *start* tests the string starting from that position. Supplying the optional *end* halts the comparison of the string at that position.

Consider this:

```pycon
>>> 'Python'.startswith('Py')
True
>>> 'a tuple of prefixes'.startswith(('at', 'a'))
True
>>> 'Python is amazing'.startswith('is', 7)
True

```

See also `endswith()` and `removeprefix()`.

[Subject index](INDEX.md) · [Previous](str-rsplit-to-str-split.md) · [Continue](str-strip-to-str-swapcase.md) · [Owning module, declaration or section: String Methods](str-capitalize-to-str-count.md)
