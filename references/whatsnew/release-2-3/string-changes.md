# What’s New in Python 2.3 / String Changes

### String Changes

- For strings, the [`in`](https://docs.python.org/3.14/reference/expressions.html#in) operator now behaves differently. Formerly, in evaluating `X in Y` with *X* and *Y* both strings, *X* had to be a lone character. No longer; *X* can be a string of whatever length, and `X in Y` gives [`True`](https://docs.python.org/3.14/library/constants.html#True) whenever *X* is a substring of *Y*. Should *X* be the empty string, the answer is always `True`.

```python
>>> 'ab' in 'abcd'
True
>>> 'ad' in 'abcd'
False
>>> '' in 'abcd'
True

```

Keep in mind this won't reveal where the substring begins; for that, reach for the [`find()`](https://docs.python.org/3.14/library/stdtypes.html#str.find) string method.

- The [`strip()`](https://docs.python.org/3.14/library/stdtypes.html#str.strip), [`lstrip()`](https://docs.python.org/3.14/library/stdtypes.html#str.lstrip), and [`rstrip()`](https://docs.python.org/3.14/library/stdtypes.html#str.rstrip) string methods now accept an optional argument naming which characters to strip. As before, the default removes every whitespace character:

```python
>>> '   abc '.strip()
'abc'
>>> '><><abc<><><>'.strip('<>')
'abc'
>>> '><><abc<><><>\n'.strip('<>')
'abc<><><>\n'
>>> u'\u4000\u4001abc\u4000'.strip(u'\u4000')
u'\u4001abc'
>>>

```

(Suggested by Simon Brunning and implemented by Walter Dörwald.)

-

The string methods [`startswith()`](https://docs.python.org/3.14/library/stdtypes.html#str.startswith) and [`endswith()`](https://docs.python.org/3.14/library/stdtypes.html#str.endswith) will now take negative values for their *start* and *end* parameters.

- There is also a fresh string method called [`zfill()`](https://docs.python.org/3.14/library/stdtypes.html#str.zfill), which began life as a function inside the [`string`](https://docs.python.org/3.14/library/string.html#module-string) module. What `zfill()` does is left-pad a numeric string with zeros until the requested width is reached. Keep in mind that the `%` operator remains more capable and adaptable than `zfill()`.

```python
>>> '45'.zfill(4)
'0045'
>>> '12345'.zfill(4)
'12345'
>>> 'goofy'.zfill(6)
'0goofy'

```

(Contributed by Walter Dörwald.)

- There is a brand-new type object named `basestring`. Since both 8-bit strings and Unicode strings derive from it, calling `isinstance(obj, basestring)` yields [`True`](https://docs.python.org/3.14/library/constants.html#True) for either flavor of string. Because the type is entirely abstract, you cannot construct `basestring` instances.

- Strings that have been interned are no longer immortal; they will be garbage-collected normally once the lone remaining reference comes from the internal dictionary that holds interned strings. (Implemented by Oren Tirosh.)

[Subject index](INDEX.md) · [Previous source section](pending-deprecation-warnings.md) · [Release/subject declaration](standard-set-type.md) · [Next source section](optimizations.md)
