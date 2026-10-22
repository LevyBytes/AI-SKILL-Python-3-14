# re: `Pattern.search()`, `Pattern.match()`, `Pattern.fullmatch()`, `Pattern.split()`, `Pattern.findall()`, `Pattern.finditer()`, `Pattern.sub()`, `Pattern.subn()`, `Pattern.flags`, `Pattern.groups`, `Pattern.groupindex`

Pattern.search(*string*[, *pos*[, *endpos*]])

Look through *string* for the earliest spot where this regular expression yields a match, returning a matching `Match`. Hand back `None` when no position in the string matches the pattern; observe that this differs from turning up a zero-length match somewhere inside the string.

The optional second parameter *pos* supplies an index into the string at which the search begins; its default is `0`. This is not entirely the same as slicing the string, because the `'^'` pattern character matches at the string's true start and at positions right after a newline, though not necessarily at the index where the search begins.

The optional parameter *endpos* sets a bound on how far the string gets searched; the effect is as though the string were *endpos* characters long, so only the characters running from *pos* up to `endpos - 1` are searched for a match. When *endpos* falls below *pos*, no match turns up; otherwise, given that *rx* is a compiled regular expression object, `rx.search(string, 0, 50)` is equivalent to `rx.search(string[:50], 0)`.

```python
>>> pattern = re.compile("d")
>>> pattern.search("dog")     # Match at index 0
<re.Match object; span=(0, 1), match='d'>
>>> pattern.search("dog", 1)  # No match; search doesn't include the "d"

```

 Pattern.match(*string*[, *pos*[, *endpos*]])

When some or all of the characters at the *beginning* of *string* match this regular expression, give back a matching `Match`. Return `None` if the string fails to match the pattern; observe that this differs from a zero-length match.

The optional *pos* and *endpos* parameters have the same meaning as for the `search()` method.

```python
>>> pattern = re.compile("o")
>>> pattern.match("dog")      # No match as "o" is not at the start of "dog".
>>> pattern.match("dog", 1)   # Match as "o" is the 2nd character of "dog".
<re.Match object; span=(1, 2), match='o'>

```

To find a match somewhere within *string*, reach for `search()` instead (see also search() vs. match()).

 Pattern.fullmatch(*string*[, *pos*[, *endpos*]])

When the entire *string* matches this regular expression, hand back a matching `Match`. Return `None` if the string fails to match the pattern; observe that this differs from a zero-length match.

The optional *pos* and *endpos* parameters have the same meaning as for the `search()` method.

```python
>>> pattern = re.compile("o[gh]")
>>> pattern.fullmatch("dog")      # No match as "o" is not at the start of "dog".
>>> pattern.fullmatch("ogre")     # No match as not the full string matches.
>>> pattern.fullmatch("doggie", 1, 3)   # Matches within given limits.
<re.Match object; span=(1, 3), match='og'>

```

Added in version 3.4.

 Pattern.split(*string*, *maxsplit=0*)

Identical to the `split()` function, using the compiled pattern.

 Pattern.findall(*string*[, *pos*[, *endpos*]])

Like the `findall()` function but driven by the compiled pattern, additionally taking optional *pos* and *endpos* parameters that constrain the search region just as they do for `search()`.

 Pattern.finditer(*string*[, *pos*[, *endpos*]])

Like the `finditer()` function but driven by the compiled pattern, additionally taking optional *pos* and *endpos* parameters that constrain the search region just as they do for `search()`.

 Pattern.sub(*repl*, *string*, *count=0*)

Identical to the `sub()` function, using the compiled pattern.

 Pattern.subn(*repl*, *string*, *count=0*)

Identical to the `subn()` function, using the compiled pattern.

 Pattern.flags

The regex matching flags. This blends the flags passed to `compile()`, any `(?...)` inline flags within the pattern, and implicit flags such as `UNICODE` when the pattern is a Unicode string.

 Pattern.groups

The number of capturing groups in the pattern.

 Pattern.groupindex

A dictionary that maps every symbolic group name set up via `(?P<id>)` to its group number. The dictionary stays empty when the pattern used no symbolic groups.

[Subject index](INDEX.md) · [Previous](re-pattern-class.md) · [Continue](pattern-pattern.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Owning module, declaration or section: re.Pattern](re-pattern-class.md) · [Owning module, declaration or section: Regular Expression Objects](re-pattern-class.md)
