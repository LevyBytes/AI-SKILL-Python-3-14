# Match/search positions and conditional match handling

[`group()`](https://docs.python.org/3.14/library/re.html#re.Match.group) gives back the substring the RE matched. [`start()`](https://docs.python.org/3.14/library/re.html#re.Match.start) and [`end()`](https://docs.python.org/3.14/library/re.html#re.Match.end) give back the match’s starting and ending index. [`span()`](https://docs.python.org/3.14/library/re.html#re.Match.span) returns both start and end indexes in a single tuple. Because the [`match()`](https://docs.python.org/3.14/library/re.html#re.Pattern.match) method only verifies whether the RE matches at the start of a string, `start()` is forever zero. The [`search()`](https://docs.python.org/3.14/library/re.html#re.Pattern.search) method of patterns, by contrast, sweeps along the string, so in that situation the match might begin somewhere other than zero.

```python
>>> print(p.match('::: message'))
None
>>> m = p.search('::: message'); print(m)
<re.Match object; span=(4, 11), match='message'>
>>> m.group()
'message'
>>> m.span()
(4, 11)

```

Within real programs, the usual habit is to keep the [match object](https://docs.python.org/3.14/library/re.html#match-objects) in a variable and then test whether it came back `None`. That typically reads as:

```python
p = re.compile( ... )
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')

```

[Subject index](INDEX.md) · [Compile a pattern, match strings and inspect match objects](compile-a-pattern-match-strings-and-inspect-match-objects.md) · [findall, finditer and raw-string caveats](findall-finditer-and-raw-string-caveats.md) · [Previous source context](compile-a-pattern-match-strings-and-inspect-match-objects.md) · [Following source context](findall-finditer-and-raw-string-caveats.md)
