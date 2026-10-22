# re: `Match.expand()`, `Match.group()`

A match is [generic](https://docs.python.org/3.14/library/typing.html#generics) with respect to whichever string type produced it ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes)).

Changed in version 3.9: `re.Match` accepts `[]` to signal whether the match is Unicode (str) or bytes. Refer to [Generic Alias Type](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias).

 Match.expand(*template*)

Yield the string produced by applying backslash substitution to the *template* string, exactly the way the `sub()` method does. Escape sequences like `\n` turn into their matching characters, while numeric backreferences (`\1`, `\2`) and named ones (`\g<1>`, `\g<name>`) get swapped out for whatever the matching group captured. As for `\g<0>`, it stands in for the whole match.

Changed in version 3.5: Groups that go unmatched now come back as an empty string.

 Match.group([*group1*, *...*])

Hands back one or several subgroups from the match. A lone argument yields a single string, whereas several arguments yield a tuple holding one entry for each. With no arguments at all, *group1* falls back to zero, so the complete match is returned. When a *groupN* argument equals zero, you get the whole matched string; a positive integer instead gives the text captured by the matching parenthesized group. Passing a group number that is negative or exceeds how many groups the pattern declares triggers an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) exception. Where a group sits in a stretch of the pattern that never matched, its result is `None`; where a group lives in a stretch that matched more than once, the final match wins.

```python
>>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
>>> m.group(0)       # The entire match
'Isaac Newton'
>>> m.group(1)       # The first parenthesized subgroup.
'Isaac'
>>> m.group(2)       # The second parenthesized subgroup.
'Newton'
>>> m.group(1, 2)    # Multiple arguments give us a tuple.
('Isaac', 'Newton')

```

Should the regular expression employ the `(?P<name>...)` syntax, your *groupN* arguments can additionally be strings that name groups directly. Hand in a string that names no group in the pattern, and an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) exception is raised.

Here is a somewhat more involved example:

```python
>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
>>> m.group('first_name')
'Malcolm'
>>> m.group('last_name')
'Reynolds'

```

You may equally reach named groups through their numeric index:

```python
>>> m.group(1)
'Malcolm'
>>> m.group(2)
'Reynolds'

```

When a single group matches repeatedly, you can reach only its final match:

```python
>>> m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
>>> m.group(1)                        # Returns only the last match.
'c3'

```

[Subject index](INDEX.md) · [Continue](match-getitem-to-match-groupdict.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Owning module, declaration or section: re.Match](re-match-class.md) · [Owning module, declaration or section: Match Objects](re-match-class.md) · [Preceding source contract and version conditions](re-match-class.md)
