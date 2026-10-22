# re — search() vs. match()

### search() vs. match()

Python supplies several distinct regular-expression-based primitive operations:

- `re.match()` looks for a match strictly at the start of the string

- `re.search()` looks for a match at any position in the string (the behavior Perl applies by default)

- `re.fullmatch()` requires the whole string to constitute a match

To illustrate:

```python
>>> re.match("c", "abcdef")    # No match
>>> re.search("c", "abcdef")   # Match
<re.Match object; span=(2, 3), match='c'>
>>> re.fullmatch("p.*n", "python") # Match
<re.Match object; span=(0, 6), match='python'>
>>> re.fullmatch("r.*n", "python") # No match

```

A regular expression that opens with `'^'` can pair with `search()` to confine the match to the string's start:

```python
>>> re.match("c", "abcdef")    # No match
>>> re.search("^c", "abcdef")  # No match
>>> re.search("^a", "abcdef")  # Match
<re.Match object; span=(0, 1), match='a'>

```

Be aware, though, that under `MULTILINE` mode `match()` still anchors only to the string's start, while `search()` paired with a regular expression that opens with `'^'` anchors to the start of every line.

```python
>>> re.match("X", "A\nB\nX", re.MULTILINE)  # No match
>>> re.search("^X", "A\nB\nX", re.MULTILINE)  # Match
<re.Match object; span=(4, 5), match='X'>

```

[Subject index](INDEX.md) · [Previous](simulating-scanf.md) · [Continue](making-a-phonebook.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
