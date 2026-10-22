# stdtypes: `str.capitalize()`, `str.casefold()`, `str.center()`, `str.count()`

### String Methods

Beyond the full set of common sequence operations, strings also carry the extra methods laid out below.

On top of that, strings back two flavors of string formatting: one is broadly flexible and tunable (see `str.format()`, [Format string syntax](https://docs.python.org/3.14/library/string.html#formatstrings) and [Custom string formatting](https://docs.python.org/3.14/library/string.html#string-formatting)), while the other mirrors C `printf` style formatting, which copes with fewer types and takes a bit more care to wield correctly, yet frequently runs faster on the cases it does support (printf-style String Formatting).

Within the standard library, the [Text Processing Services](https://docs.python.org/3.14/library/text.html#textservices) section walks through several additional modules supplying assorted text utilities (regular-expression support among them, by way of the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module).

 str.capitalize()

Hand back a copy in which the leading character is uppercased and everything after it is lowercased.

Changed in version 3.8: The leading character now goes to titlecase in place of uppercase. The upshot is that a character such as a digraph keeps only its opening letter capitalized rather than the whole thing.

 str.casefold()

Give back a casefolded copy of the string. Such casefolded strings come in handy for caseless matching.

Though akin to lowercasing, this operation goes further, the aim being to strip every case distinction out of a string. Take the German lowercase letter `'ß'`, which stands in for `"ss"`. Being lowercase already, `'ß'` is untouched by `lower()`; `casefold()`, by contrast, turns it into `"ss"`. To illustrate:

```pycon
>>> 'straße'.lower()
'straße'
>>> 'straße'.casefold()
'strasse'

```

The casefolding algorithm is [described in section 3.13 ‘Default Case Folding’ of the Unicode Standard](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-3/#G33992).

Added in version 3.3.

 str.center(*width*, *fillchar=' '*, */*)

Give back the value centered inside a string whose length is *width*. The chosen *fillchar* supplies the padding (an ASCII space by default). Where *width* does not exceed `len(s)`, you simply get the original string back. To illustrate:

```python
>>> 'Python'.center(10)
'  Python  '
>>> 'Python'.center(10, '-')
'--Python--'
>>> 'Python'.center(4)
'Python'

```

 str.count(*sub*[, *start*[, *end*]])

Give back how many non-overlapping times the substring *sub* turns up across the range [*start*, *end*]. The optional *start* and *end* arguments carry their slice-notation meaning.

Where *sub* is empty, the result is the count of empty strings sitting between characters, which equals the string's length plus one. To illustrate:

```python
>>> 'spam, spam, spam'.count('spam')
3
>>> 'spam, spam, spam'.count('spam', 5)
2
>>> 'spam, spam, spam'.count('spam', 5, 10)
1
>>> 'spam, spam, spam'.count('eggs')
0
>>> 'spam, spam, spam'.count('')
17

```

[Subject index](INDEX.md) · [Previous](str-class-to-str-class.md) · [Continue](str-encode-to-str-find.md)
