# match() versus search()

### match() versus search()

The [`match()`](https://docs.python.org/3.14/library/re.html#re.match) function tests solely whether the RE matches right at the string's start, whereas [`search()`](https://docs.python.org/3.14/library/re.html#re.search) moves forward across the string hunting for a match. Holding on to that distinction matters. Recall that `match()` reports a match only when it begins at 0; if the match wouldn't begin at zero, `match()` *won't* report it.

```python
>>> print(re.match('super', 'superstition').span())
(0, 5)
>>> print(re.match('super', 'insuperable'))
None

```

[`search()`](https://docs.python.org/3.14/library/re.html#re.search), by contrast, advances through the string and reports back the very first match it turns up.

```python
>>> print(re.search('super', 'superstition').span())
(0, 5)
>>> print(re.search('super', 'insuperable').span())
(2, 7)

```

Now and again you'll feel pulled toward sticking with [`re.match()`](https://docs.python.org/3.14/library/re.html#re.match) and merely tacking `.*` onto the head of your RE. Fight that urge and switch to [`re.search()`](https://docs.python.org/3.14/library/re.html#re.search). To hasten the search for a match, the regular expression compiler studies REs a little. One piece of that study works out what the opening character of a match has to be; a pattern leading with `Crow`, for example, has to match beginning at a `'C'`. That insight lets the engine race through the string after the starting character, attempting the whole match only once a `'C'` shows up.

Tacking on `.*` undoes that optimization, since it forces a scan clear to the string's end followed by backtracking to satisfy the remainder of the RE. Go with [`re.search()`](https://docs.python.org/3.14/library/re.html#re.search) instead.

[Subject index](INDEX.md) · [Previous source context](use-string-methods.md) · [Following source context](greedy-versus-non-greedy.md)
