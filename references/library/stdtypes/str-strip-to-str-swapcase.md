# stdtypes: `str.strip()`, `str.swapcase()`

str.strip(*chars=None*, */*)

Yields a copy of the string from which the leading and trailing characters have been dropped. The *chars* argument is a string naming the collection of characters to drop. When left out or set to `None`, the *chars* argument falls back to dropping whitespace. The *chars* argument is treated as neither a prefix nor a suffix; instead, each combination of its members gets stripped.

Whitespace characters are the ones defined by `str.isspace()`.

Consider this:

```pycon
>>> '   spacious   '.strip()
'spacious'
>>> 'www.example.com'.strip('cmowz.')
'example'

```

The outermost leading and trailing *chars* argument values get stripped off the string. Stripping proceeds from the leading end until a string character is reached that does not belong to the set of characters named in *chars*. The trailing end undergoes the same treatment.

Consider this:

```pycon
>>> comment_string = '#....... Section 3.2.1 Issue #32 .......'
>>> comment_string.strip('.#! ')
'Section 3.2.1 Issue #32'

```

See also `rstrip()`.

 str.swapcase()

Yields a copy of the string with uppercase characters turned into lowercase and the reverse as well. Consider this:

```pycon
>>> 'Hello World'.swapcase()
'hELLO wORLD'

```

Bear in mind that `s.swapcase().swapcase() == s` does not necessarily hold true. Consider this:

```pycon
>>> 'straße'.swapcase().swapcase()
'strasse'

```

See also `str.lower()` and `str.upper()`.

[Subject index](INDEX.md) · [Previous](str-splitlines-to-str-startswith.md) · [Continue](str-title-to-str-zfill.md) · [Owning module, declaration or section: String Methods](str-capitalize-to-str-count.md)
