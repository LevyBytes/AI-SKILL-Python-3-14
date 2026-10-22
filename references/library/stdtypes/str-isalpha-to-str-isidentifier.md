# stdtypes: `str.isalpha()`, `str.isascii()`, `str.isdecimal()`, `str.isdigit()`, `str.isidentifier()`

str.isalpha()

Hand back `True` where every character in the string is alphabetic and at least one character is present, and `False` otherwise. The alphabetic characters are the ones the Unicode character database flags as “Letter”, that is, those whose general category property is one of “Lm”, “Lt”, “Lu”, “Ll”, or “Lo”. Keep in mind this differs from the [Alphabetic property defined in the section 4.10 ‘Letters, Alphabetic, and Ideographic’ of the Unicode Standard](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-4/#G91002). To illustrate:

```pycon
>>> 'Letters and spaces'.isalpha()
False
>>> 'LettersOnly'.isalpha()
True
>>> 'µ'.isalpha()  # non-ASCII characters can be considered alphabetical too
True

```

See [Unicode Properties](https://docs.python.org/3.14/howto/unicode.html#unicode-properties).

 str.isascii()

Hand back `True` where the string is empty or each of its characters is ASCII, and `False` otherwise. The code points of ASCII characters fall in the range U+0000-U+007F. To illustrate:

```pycon
>>> 'ASCII characters'.isascii()
True
>>> 'µ'.isascii()
False

```

Added in version 3.7.

 str.isdecimal()

Hand back `True` where every character in the string is a decimal character and at least one character is present, and `False` otherwise. A decimal character is one you could use to spell out a base-10 number, U+0660 (ARABIC-INDIC DIGIT ZERO) being an example. In strict terms, any character sitting in the Unicode General Category “Nd” qualifies. To illustrate:

```pycon
>>> '0123456789'.isdecimal()
True
>>> '٠١٢٣٤٥٦٧٨٩'.isdecimal()  # Arabic-Indic digits zero to nine
True
>>> 'alphabetic'.isdecimal()
False

```

 str.isdigit()

Hand back `True` where every character in the string is a digit and at least one character is present, and `False` otherwise. The digits cover the decimal characters plus digits needing special handling, the compatibility superscript digits among them. They also take in digits unusable for spelling base-10 numbers, like the [Kharosthi numbers](https://en.wikipedia.org/wiki/Kharosthi#Numerals). In strict terms, a digit is any character whose property value is Numeric_Type=Digit or Numeric_Type=Decimal.

To illustrate:

```pycon
>>> '0123456789'.isdigit()
True
>>> '٠١٢٣٤٥٦٧٨٩'.isdigit()  # Arabic-Indic digits zero to nine
True
>>> '⅕'.isdigit()  # Vulgar fraction one fifth
False
>>> '²'.isdecimal(), '²'.isdigit(),  '²'.isnumeric()
(False, True, True)

```

See also `isdecimal()` and `isnumeric()`.

 str.isidentifier()

Hand back `True` where the string forms a valid identifier under the language definition, per the section [Names (identifiers and keywords)](https://docs.python.org/3.14/reference/lexical_analysis.html#identifiers).

You can lean on [`keyword.iskeyword()`](https://docs.python.org/3.14/library/keyword.html#keyword.iskeyword) to check whether a string `s` is a reserved identifier, like [`def`](https://docs.python.org/3.14/reference/compound_stmts.html#def) and [`class`](https://docs.python.org/3.14/reference/compound_stmts.html#class).

Example:

[Subject index](INDEX.md) · [Previous](str-format-to-str-isalnum.md) · [Owning module, declaration or section: String Methods](str-capitalize-to-str-count.md) · [Required continuation of the source contract](str-islower-to-str-isspace.md)
