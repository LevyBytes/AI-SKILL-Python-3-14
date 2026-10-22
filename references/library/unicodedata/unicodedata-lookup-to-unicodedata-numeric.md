# unicodedata: `unicodedata.lookup()`, `unicodedata.name()`, `unicodedata.decimal()`, `unicodedata.digit()`, `unicodedata.numeric()`

# Unicodedata

### `unicodedata` — Unicode Database

---

Through this module you can reach the Unicode Character Database (UCD), which lays out the character properties for every Unicode character. Everything in that database is built from the [UCD version 16.0.0](https://www.unicode.org/Public/16.0.0/ucd).

The names and symbols this module relies on match those laid down by Unicode Standard Annex #44, [“Unicode Character Database”](https://www.unicode.org/reports/tr44/). The functions it provides are:

See also

The [Unicode HOWTO](https://docs.python.org/3.14/howto/unicode.html#unicode-howto) goes deeper into Unicode and how to put this module to use.

 unicodedata.lookup(*name*)

Find a character given its name. When a character carrying that name exists, hand it back; when none matches, [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised. As an illustration:

```python
>>> unicodedata.lookup('LEFT CURLY BRACKET')
'{'

```

Whatever characters this function yields match exactly what the `\N` escape sequence delivers inside string literals. As an illustration:

```python
>>> unicodedata.lookup('MIDDLE DOT') == '\N{MIDDLE DOT}'
True

```

Changed in version 3.3: Handling of name aliases [1] along with named sequences [2] was introduced.

 unicodedata.name(*chr*, *default=None*, */*)

Hands back, as a string, the name tied to the character *chr*. Where no name exists, *default* comes back instead; with no *default* supplied, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. As an illustration:

```python
>>> unicodedata.name('½')
'VULGAR FRACTION ONE HALF'
>>> unicodedata.name('\uFFFF', 'fallback')
'fallback'

```

 unicodedata.decimal(*chr*, *default=None*, */*)

Hands back, as an integer, the decimal value tied to the character *chr*. Lacking such a value, it yields *default*; and absent any *default*, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised. As an illustration:

```python
>>> unicodedata.decimal('\N{ARABIC-INDIC DIGIT NINE}')
9
>>> unicodedata.decimal('\N{SUPERSCRIPT NINE}', -1)
-1

```

 unicodedata.digit(*chr*, *default=None*, */*)

Hands back, as an integer, the digit value tied to the character *chr*. Should that value be missing, *default* is what you get; when no *default* was passed, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised:

```python
>>> unicodedata.digit('\N{SUPERSCRIPT NINE}')
9

```

 unicodedata.numeric(*chr*, *default=None*, */*)

Hands back, as a float, the numeric value tied to the character *chr*. If that value isn't present, *default* is returned in its place; failing a *default*, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised:

```python
>>> unicodedata.numeric('½')
0.5

```

[Subject index](INDEX.md) · [Continue](unicodedata-category-to-unicodedata-ucd-3-2-0.md)
