# stdtypes: `str.title()`, `str.translate()`, `str.upper()`, `str.zfill()`

str.title()

Yields a titlecased rendition of the string in which words open with an uppercase character while the rest of the characters stay lowercase.

Consider this:

```python
>>> 'Hello world'.title()
'Hello World'

```

The routine relies on a simple, language-independent notion of a word as runs of consecutive letters. That notion holds up in many settings, yet it means apostrophes inside contractions and possessives act as word boundaries, which may not be what you intend:

```python
>>> "they're bill's friends from the UK".title()
"They'Re Bill'S Friends From The Uk"

```

The [`string.capwords()`](https://docs.python.org/3.14/library/string.html#string.capwords) function avoids this issue, since it breaks words apart on spaces alone.

As an alternative, a workaround that handles apostrophes can be built with regular expressions:

```python
>>> import re
>>> def titlecase(s):
...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
...                   lambda mo: mo.group(0).capitalize(),
...                   s)
...
>>> titlecase("they're bill's friends.")
"They're Bill's Friends."

```

See also `istitle()`.

 str.translate(*table*, */*)

Yields a copy of the string in which each character has been routed through the supplied translation table. The table has to be an object that supports indexing through [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__), generally a [mapping](https://docs.python.org/3.14/glossary.html#term-mapping) or [sequence](https://docs.python.org/3.14/glossary.html#term-sequence). On being indexed by a Unicode ordinal (an integer), the table object may do any of the following: return a Unicode ordinal or a string, mapping the character to one or more other characters; return `None`, removing the character from the returned string; or raise a [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError) exception, mapping the character to itself.

You can rely on `str.maketrans()` to build a translation map out of character-to-character mappings expressed in various formats.

Refer as well to the [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) module for a more adaptable means of custom character mappings.

 str.upper()

Yields a copy of the string where each of the cased characters [4] has been turned to uppercase. Note that `s.upper().isupper()` may turn out `False` when `s` holds uncased characters or when the Unicode category of the resulting character(s) is something other than “Lu” (Letter, uppercase) — for instance “Lt” (Letter, titlecase).

The uppercasing routine in use is [described in section 3.13 ‘Default Case Folding’ of the Unicode Standard](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-3/#G33992).

 str.zfill(*width*, */*)

Yields a copy of the string padded on the left with ASCII `'0'` digits so as to form a string whose length is *width*. A leading sign prefix (`'+'`/`'-'`) is dealt with by placing the padding *after* the sign character rather than ahead of it. Should *width* be less than or equal to `len(s)`, the original string comes back unchanged.

Consider this:

```pycon
>>> "42".zfill(5)
'00042'
>>> "-42".zfill(5)
'-0042'

```

See also `rjust()`.

[Subject index](INDEX.md) · [Previous](str-strip-to-str-swapcase.md) · [Continue](formatted-string-literals-f-strings.md) · [Owning module, declaration or section: String Methods](str-capitalize-to-str-count.md)
