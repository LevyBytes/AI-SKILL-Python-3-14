# 11.1. Output formatting

### 11.1. Output formatting

A `repr()` variant tuned for compact rendering of big or deeply nested containers ships in the [`reprlib`](https://docs.python.org/3.14/library/reprlib.html#module-reprlib) module, which adapts [`repr()`](https://docs.python.org/3.14/library/functions.html#repr):

```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"

```

For finer-grained control over rendering both standard and user-defined objects in a form the interpreter can read back, reach for the [`pprint`](https://docs.python.org/3.14/library/pprint.html#module-pprint) module. Whenever the rendered result spills past a single line, its “pretty printer” inserts newlines and indentation so the underlying structure stands out more plainly:

```python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
...
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]

```

To reflow blocks of prose so they fit within a particular display width, use the [`textwrap`](https://docs.python.org/3.14/library/textwrap.html#module-textwrap) module:

```python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
...
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.

```

A repository of culture-dependent data formats is reachable through the [`locale`](https://docs.python.org/3.14/library/locale.html#module-locale) module. By way of locale's format function, the grouping attribute gives you a straightforward route to rendering numbers with grouped separators:

```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()          # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format_string("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'

```

[Subject index](INDEX.md) · [Previous source section](brief-tour-of-the-standard-library-part-ii.md) · [Following source section](templating.md)
