# Compile a pattern, match strings and inspect match objects

### Performing matches

So you hold an object that stands for a compiled regular expression — now what? Pattern objects come with a handful of methods and attributes. Only the more notable ones get treated here; turn to the [`re`](https://docs.python.org/3.14/library/re.html#module-re) docs for the whole list.

| Method/Attribute | Purpose |
| --- | --- |
| `match()` | Check whether the RE lines up at the string’s start. |
| `search()` | Sweep across a string hunting for any spot this RE lines up. |
| `findall()` | Gather every substring the RE lines up with and hand them back as a list. |
| `finditer()` | Gather every substring the RE lines up with and hand them back as an iterator. |

[`match()`](https://docs.python.org/3.14/library/re.html#re.Pattern.match) and [`search()`](https://docs.python.org/3.14/library/re.html#re.Pattern.search) hand back `None` when nothing matches. On success, you instead get a [match object](https://docs.python.org/3.14/library/re.html#match-objects) instance, which holds details of the match: its start, its end, the substring it captured, and so on.

A good way to grasp all this is to play around interactively with the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module.

For its examples this HOWTO relies on the standard Python interpreter. To start, launch the Python interpreter, bring in the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module, and compile a RE:

```python
>>> import re
>>> p = re.compile('[a-z]+')
>>> p
re.compile('[a-z]+')

```

Next, you can test assorted strings against the RE `[a-z]+`. The empty string ought to match nothing, given that `+` denotes ‘one or more repetitions’. Here [`match()`](https://docs.python.org/3.14/library/re.html#re.Pattern.match) ought to give back `None`, which leaves the interpreter printing nothing. To make that plain, you can deliberately print what `match()` returns.

```python
>>> p.match("")
>>> print(p.match(""))
None

```

Next, give it a string it ought to match, like `tempo`. Here [`match()`](https://docs.python.org/3.14/library/re.html#re.Pattern.match) hands back a [match object](https://docs.python.org/3.14/library/re.html#match-objects), so you ought to keep the result in a variable to use afterward.

```python
>>> m = p.match('tempo')
>>> m
<re.Match object; span=(0, 5), match='tempo'>

```

You can now interrogate the [match object](https://docs.python.org/3.14/library/re.html#match-objects) about the string it matched. Instances of a match object likewise carry several methods and attributes; the ones that matter most are:

| Method/Attribute | Purpose |
| --- | --- |
| `group()` | Return the string matched by the RE |
| `start()` | Return the starting position of the match |
| `end()` | Return the ending position of the match |
| `span()` | Return a tuple containing the (start, end) positions of the match |

Putting these methods to use quickly reveals what they mean:

```python
>>> m.group()
'tempo'
>>> m.start(), m.end()
(0, 5)
>>> m.span()
(0, 5)

```

[Subject index](INDEX.md) · [Match/search positions and conditional match handling](match-search-positions-and-conditional-match-handling.md) · [findall, finditer and raw-string caveats](findall-finditer-and-raw-string-caveats.md) · [Previous source context](the-backslash-plague.md) · [Following source context](match-search-positions-and-conditional-match-handling.md)
