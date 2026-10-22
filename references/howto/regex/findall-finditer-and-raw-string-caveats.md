# findall, finditer and raw-string caveats

A pair of pattern methods give back every match for a pattern. [`findall()`](https://docs.python.org/3.14/library/re.html#re.Pattern.findall) yields a list of the matching strings:

```python
>>> p = re.compile(r'\d+')
>>> p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
['12', '11', '10']

```

This example needs the `r` prefix, which makes the literal a raw string literal, because escape sequences in a regular “cooked” string literal that Python — as distinct from regular expressions — does not recognize now trigger a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) and are slated to turn into a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). See The backslash plague.

[`findall()`](https://docs.python.org/3.14/library/re.html#re.Pattern.findall) must assemble the whole list before handing it back as the result. The [`finditer()`](https://docs.python.org/3.14/library/re.html#re.Pattern.finditer) method instead hands back a stream of [match object](https://docs.python.org/3.14/library/re.html#match-objects) instances in the form of an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator):

```python
>>> iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
>>> iterator
<callable_iterator object at 0x...>
>>> for match in iterator:
...     print(match.span())
...
(0, 2)
(22, 24)
(29, 31)

```

[Subject index](INDEX.md) · [Compile a pattern, match strings and inspect match objects](compile-a-pattern-match-strings-and-inspect-match-objects.md) · [Match/search positions and conditional match handling](match-search-positions-and-conditional-match-handling.md) · [Previous source context](match-search-positions-and-conditional-match-handling.md) · [Following source context](module-level-functions.md)
