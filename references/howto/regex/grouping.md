# Grouping

### Grouping

Often you'll want to extract more than the bare fact of whether the RE matched. A common use of regular expressions is to take strings apart by composing a RE split across multiple subgroups, each matching a distinct piece of interest. As an example, an RFC-822 header line breaks down into a header name plus a value, with a `':'` between them, like so:

```none
From: author@example.com
User-Agent: Thunderbird 1.5.0.9 (X11/20061227)
MIME-Version: 1.0
To: editor@example.com

```

You can deal with this by composing a regular expression that matches a whole header line and contains one group for the header name plus a second group for the header's value.

Groups are denoted by the `'('`, `')'` metacharacters. `'('` and `')'` carry roughly the role they play in mathematical expressions; they bundle the expressions held inside them, and the contents of a group can be repeated with a quantifier such as `*`, `+`, `?`, or `{m,n}`. As an example, `(ab)*` matches zero or more repetitions of `ab`.

```python
>>> p = re.compile('(ab)*')
>>> print(p.match('ababababab').span())
(0, 10)

```

Groups denoted by `'('`, `')'` further record where the matched text begins and ends; you obtain that by handing an argument to [`group()`](https://docs.python.org/3.14/library/re.html#re.Match.group), [`start()`](https://docs.python.org/3.14/library/re.html#re.Match.start), [`end()`](https://docs.python.org/3.14/library/re.html#re.Match.end), and [`span()`](https://docs.python.org/3.14/library/re.html#re.Match.span). Numbering of groups begins at 0. Group 0, always available, stands for the entire RE, which is why every [match object](https://docs.python.org/3.14/library/re.html#match-objects) method takes group 0 as its default argument. Down the road we'll cover how to write groups that don't capture the stretch of text they match.

```python
>>> p = re.compile('(a)b')
>>> m = p.match('ab')
>>> m.group()
'ab'
>>> m.group(0)
'ab'

```

Subgroups get numbered left to right, beginning at 1 and rising. Groups may be nested; to work out a group's number, simply tally the opening parentheses as you scan left to right.

```python
>>> p = re.compile('(a(b)c)d')
>>> m = p.match('abcd')
>>> m.group(0)
'abcd'
>>> m.group(1)
'abc'
>>> m.group(2)
'b'

```

You can supply [`group()`](https://docs.python.org/3.14/library/re.html#re.Match.group) several group numbers in one call, and then it hands back a tuple holding the matching values for each of those groups.

```python
>>> m.group(2,1,2)
('b', 'abc', 'b')

```

The [`groups()`](https://docs.python.org/3.14/library/re.html#re.Match.groups) method hands back a tuple of the strings for every subgroup, running from 1 through as many as exist.

```python
>>> m.groups()
('abc', 'b')

```

Backreferences within a pattern let you require that whatever an earlier capturing group held must reappear at the present spot in the string. As an example, `\1` succeeds when the precise contents of group 1 turn up at the current position, and otherwise it fails. Bear in mind that Python's string literals likewise use a backslash and a number to embed arbitrary characters in a string, so always use a raw string whenever you place backreferences in a RE.

To illustrate, the RE below picks out repeated words within a string.

```python
>>> p = re.compile(r'\b(\w+)\s+\1\b')
>>> p.search('Paris in the the spring').group()
'the the'

```

Backreferences of this kind aren't usually handy for plain searching through a string — few text formats duplicate data this way — yet you'll shortly discover how *very* handy they become while carrying out string substitutions.

[Subject index](INDEX.md) · [Previous source context](more-metacharacters.md) · [Following source context](non-capturing-and-named-groups.md)
