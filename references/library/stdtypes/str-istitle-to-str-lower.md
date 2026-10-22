# stdtypes: `str.istitle()`, `str.isupper()`, `str.join()`, `str.ljust()`, `str.lower()`

str.istitle()

Yields `True` when the string is a titlecased string with at least one character present — meaning, for example, that uppercase characters may appear only after uncased characters and lowercase characters only after cased ones. Otherwise yields `False`.

Consider this:

```pycon
>>> 'Spam, Spam, Spam'.istitle()
True
>>> 'spam, spam, spam'.istitle()
False
>>> 'SPAM, SPAM, SPAM'.istitle()
False

```

See also `title()`.

 str.isupper()

Yields `True` when every cased character [4] within the string is uppercase and at least one cased character is present; otherwise yields `False`.

```python
>>> 'BANANA'.isupper()
True
>>> 'banana'.isupper()
False
>>> 'baNana'.isupper()
False
>>> ' '.isupper()
False

```

 str.join(*iterable*, */*)

Yields a string formed by concatenating the strings found in *iterable*. Should *iterable* hold any non-string values, including `bytes` objects, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised. The string on which the method is called serves as the separator placed between elements. Consider this:

```pycon
>>> ', '.join(['spam', 'spam', 'spam'])
'spam, spam, spam'
>>> '-'.join('Python')
'P-y-t-h-o-n'

```

See also `split()`.

 str.ljust(*width*, *fillchar=' '*, */*)

Yields the string left justified inside a string whose length is *width*. The padding applies the supplied *fillchar* (an ASCII space by default). Should *width* be less than or equal to `len(s)`, the original string comes back unchanged.

Consider this:

```pycon
>>> 'Python'.ljust(10)
'Python    '
>>> 'Python'.ljust(10, '.')
'Python....'
>>> 'Monty Python'.ljust(10, '.')
'Monty Python'

```

See also `rjust()`.

 str.lower()

Yields a copy of the string where each of the cased characters [4] has been turned to lowercase. Consider this:

```pycon
>>> 'Lower Method Example'.lower()
'lower method example'

```

The lowercasing routine in use is [described in section 3.13 ‘Default Case Folding’ of the Unicode Standard](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-3/#G33992).

[Subject index](INDEX.md) · [Previous](str-islower-to-str-isspace.md) · [Continue](str-lstrip-to-str-removesuffix.md) · [Owning module, declaration or section: String Methods](str-capitalize-to-str-count.md)
