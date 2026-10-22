# stdtypes: `str.encode()`, `str.endswith()`, `str.expandtabs()`, `str.find()`

str.encode(*encoding='utf-8'*, *errors='strict'*)

Give back the string encoded into `bytes`.

The default *encoding* is `'utf-8'`; the permitted values appear under [Standard Encodings](https://docs.python.org/3.14/library/codecs.html#standard-encodings).

How encoding errors get treated is governed by *errors*. Under `'strict'` (the default), a [`UnicodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError) exception fires. The remaining options are `'ignore'`, `'replace'`, `'xmlcharrefreplace'`, `'backslashreplace'`, plus any name you've registered through [`codecs.register_error()`](https://docs.python.org/3.14/library/codecs.html#codecs.register_error). Full details sit under [Error Handlers](https://docs.python.org/3.14/library/codecs.html#error-handlers).

To save time, the *errors* value isn't validated unless an encoding error genuinely happens, [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) is switched on, or a [debug build](https://docs.python.org/3.14/using/configure.html#debug-build) is in play. To illustrate:

```python
>>> encoded_str_to_bytes = 'Python'.encode()
>>> type(encoded_str_to_bytes)
<class 'bytes'>
>>> encoded_str_to_bytes
b'Python'

```

Changed in version 3.1: Added support for keyword arguments.

Changed in version 3.9: Validation of the *errors* argument's value now happens under [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) as well as in [debug mode](https://docs.python.org/3.14/using/configure.html#debug-build).

 str.endswith(*suffix*[, *start*[, *end*]])

Hand back `True` where the string finishes with the given *suffix*, and otherwise hand back `False`. You may also make *suffix* a tuple of suffixes to test against. Pass an optional *start* to begin checking from that point. Pass an optional *end* to halt the comparison there. Combining *start* and *end* matches `str[start:end].endswith(suffix)`. To illustrate:

```python
>>> 'Python'.endswith('on')
True
>>> 'a tuple of suffixes'.endswith(('at', 'in'))
False
>>> 'a tuple of suffixes'.endswith(('at', 'es'))
True
>>> 'Python is amazing'.endswith('is', 0, 9)
True

```

See also `startswith()` and `removesuffix()`.

 str.expandtabs(*tabsize=8*)

Hand back a copy in which every tab character has been swapped for one or more spaces, the count depending on the present column and the supplied tab size. Tab stops land every *tabsize* characters (8 by default, putting stops at columns 0, 8, 16 and onward). To carry out the expansion, the current column starts at zero and the string is walked character by character. Where a character is a tab (`\t`), spaces get added to the output until the current column reaches the following tab stop. (The tab itself is not carried over.) Where a character is a newline (`\n`) or return (`\r`), it is carried over and the current column drops back to zero. Any other character is carried over untouched, and the current column rises by one no matter how that character looks when printed. To illustrate:

```python
>>> '01\t012\t0123\t01234'.expandtabs()
'01      012     0123    01234'
>>> '01\t012\t0123\t01234'.expandtabs(4)
'01  012 0123    01234'
>>> print('01\t012\n0123\t01234'.expandtabs(4))
01  012
0123    01234

```

 str.find(*sub*[, *start*[, *end*]])

Hand back the smallest index within the string at which substring *sub* shows up inside the slice `s[start:end]`. The optional *start* and *end* arguments carry their slice-notation meaning. Where *sub* never appears, hand back `-1`. To illustrate:

```python
>>> 'spam, spam, spam'.find('sp')
0
>>> 'spam, spam, spam'.find('sp', 5)
6

```

See also `rfind()` and `index()`.

Note

Reserve the `find()` method for cases where the actual position of *sub* matters to you. Merely checking whether *sub* appears at all is better done with the [`in`](https://docs.python.org/3.14/reference/expressions.html#in) operator:

```python
>>> 'Py' in 'Python'
True

```

[Subject index](INDEX.md) · [Previous](str-capitalize-to-str-count.md) · [Continue](str-format-to-str-isalnum.md) · [Owning module, declaration or section: String Methods](str-capitalize-to-str-count.md)
