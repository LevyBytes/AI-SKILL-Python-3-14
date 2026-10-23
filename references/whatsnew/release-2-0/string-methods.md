# What’s New in Python 2.0 / String Methods - string

### String Methods

Up to this point, string-manipulation capability lived in the [`string`](https://docs.python.org/3.14/library/string.html#module-string) module, which generally served as a front-end for the `strop` module written in C. Bringing in Unicode created trouble for the `strop` module, since every function would have to be rewritten so it could take either 8-bit or Unicode strings. For a function such as `string.replace()`, which accepts 3 string arguments, that comes to eight possible permutations, and correspondingly tangled code.

Instead, Python 2.0 shifts the burden onto the string type, surfacing string manipulation capability through methods available on both 8-bit strings and Unicode strings.

```python
>>> 'andrew'.capitalize()
'Andrew'
>>> 'hostname'.replace('os', 'linux')
'hlinuxtname'
>>> 'moshe'.find('sh')
2

```

One thing that stayed the same, a memorable April Fools’ joke aside, is that Python strings remain immutable. Hence the string methods hand back new strings rather than changing the string they act upon.

The old [`string`](https://docs.python.org/3.14/library/string.html#module-string) module sticks around for backwards compatibility, but it largely operates as a front-end to the new string methods.

Two methods with no counterpart in pre-2.0 versions, though they’d existed in JPython for a good while, are `startswith()` and `endswith()`. `s.startswith(t)` amounts to `s[:len(t)] == t`, while `s.endswith(t)` amounts to `s[-len(t):] == t`.

Another method that warrants a special note is `join()`. Calling `join()` on a string passes it just one argument — a sequence of strings — and the effect mirrors the `string.join()` function out of the old [`string`](https://docs.python.org/3.14/library/string.html#module-string) module, only with its arguments in reverse order. Stated differently, `s.join(seq)` matches the old `string.join(seq, s)`.

[Subject index](INDEX.md) · [Previous source section](augmented-assignment.md) · [Next source section](garbage-collection-of-cycles.md) · [Release/subject declaration](introduction.md)
