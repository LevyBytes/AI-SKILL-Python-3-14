# re: `Match.__getitem__()`, `Match.groups()`, `Match.groupdict()`

Match.__getitem__(*g*)

Behaves exactly like `m.group(g)`, giving you a more convenient way to pull a single group out of a match:

```python
>>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
>>> m[0]       # The entire match
'Isaac Newton'
>>> m[1]       # The first parenthesized subgroup.
'Isaac'
>>> m[2]       # The second parenthesized subgroup.
'Newton'

```

Named groups are supported as well:

```python
>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Isaac Newton")
>>> m['first_name']
'Isaac'
>>> m['last_name']
'Newton'

```

Added in version 3.6.

 Match.groups(*default=None*)

Give back a tuple holding every subgroup of the match, running from 1 through as many groups as the pattern contains. For groups that took no part in the match, the *default* argument supplies their value, and it itself defaults to `None`.

To illustrate:

```python
>>> m = re.match(r"(\d+)\.(\d+)", "24.1632")
>>> m.groups()
('24', '1632')

```

Once we mark the decimal point and the digits trailing it as optional, some groups may sit out the match entirely. Such groups fall back to `None` unless you supply the *default* argument:

```python
>>> m = re.match(r"(\d+)\.?(\d+)?", "24")
>>> m.groups()      # Second group defaults to None.
('24', None)
>>> m.groups('0')   # Now, the second group defaults to '0'.
('24', '0')

```

 Match.groupdict(*default=None*)

Give back a dictionary that gathers every *named* subgroup of the match, using each subgroup's name as its key. Groups absent from the match take the value of the *default* argument, which itself defaults to `None`. For instance:

```python
>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
>>> m.groupdict()
{'first_name': 'Malcolm', 'last_name': 'Reynolds'}

```

[Subject index](INDEX.md) · [Previous](match-expand-to-match-group.md) · [Continue](match-start-to-match-string.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Owning module, declaration or section: re.Match](re-match-class.md) · [Owning module, declaration or section: Match Objects](re-match-class.md)
