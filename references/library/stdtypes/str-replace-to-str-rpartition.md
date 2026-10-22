# stdtypes: `str.replace()`, `str.rfind()`, `str.rindex()`, `str.rjust()`, `str.rpartition()`

str.replace(*old*, *new*, */*, *count=-1*)

Yields a copy of the string in which every occurrence of the substring *old* is swapped for *new*. When *count* is supplied, only the leading *count* occurrences get swapped. When *count* is absent or `-1`, every occurrence is swapped. Consider this:

```pycon
>>> 'spam, spam, spam'.replace('spam', 'eggs')
'eggs, eggs, eggs'
>>> 'spam, spam, spam'.replace('spam', 'eggs', 1)
'eggs, spam, spam'

```

Changed in version 3.13: passing *count* as a keyword argument is now supported.

 str.rfind(*sub*[, *start*[, *end*]])

Yields the greatest index within the string at which substring *sub* turns up, with *sub* lying inside `s[start:end]`. The optional arguments *start* and *end* are read the same way as in slice notation. Yields `-1` when the search fails. Consider this:

```pycon
>>> 'spam, spam, spam'.rfind('sp')
12
>>> 'spam, spam, spam'.rfind('sp', 0, 10)
6

```

See also `find()` and `rindex()`.

 str.rindex(*sub*[, *start*[, *end*]])

Behaves like `rfind()` except that a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when the substring *sub* cannot be located. Consider this:

```pycon
>>> 'spam, spam, spam'.rindex('spam')
12
>>> 'spam, spam, spam'.rindex('eggs')
Traceback (most recent call last):
  File "<stdin-0>", line 1, in <module>
    'spam, spam, spam'.rindex('eggs')
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
ValueError: substring not found

```

See also `index()` and `find()`.

 str.rjust(*width*, *fillchar=' '*, */*)

Yields the string right justified inside a string whose length is *width*. The padding applies the supplied *fillchar* (an ASCII space by default). Should *width* be less than or equal to `len(s)`, the original string comes back unchanged.

Consider this:

```pycon
>>> 'Python'.rjust(10)
'    Python'
>>> 'Python'.rjust(10, '.')
'....Python'
>>> 'Monty Python'.rjust(10, '.')
'Monty Python'

```

See also `ljust()` and `zfill()`.

 str.rpartition(*sep*, */*)

Divides the string at the final occurrence of *sep*, returning a 3-tuple made up of the portion ahead of the separator, the separator itself, and the portion after it. When the separator is absent, returns a 3-tuple holding two empty strings followed by the string itself.

Consider this:

```pycon
>>> 'Monty Python'.rpartition(' ')
('Monty', ' ', 'Python')
>>> "Monty Python's Flying Circus".rpartition(' ')
("Monty Python's Flying", ' ', 'Circus')
>>> 'Monty Python'.rpartition('-')
('', '', 'Monty Python')

```

See also `partition()`.

[Subject index](INDEX.md) · [Previous](str-lstrip-to-str-removesuffix.md) · [Continue](str-rsplit-to-str-split.md) · [Owning module, declaration or section: String Methods](str-capitalize-to-str-count.md)
