# stdtypes: `str.islower()`, `str.isnumeric()`, `str.isprintable()`, `str.isspace()`

```python
>>> from keyword import iskeyword

>>> 'hello'.isidentifier(), iskeyword('hello')
(True, False)
>>> 'def'.isidentifier(), iskeyword('def')
(True, True)

```

 str.islower()

Yields `True` when every cased character [4] within the string is lowercase and at least one cased character is present; otherwise yields `False`.

 str.isnumeric()

Yields `True` when each character of the string is a numeric character and at least one character is present; otherwise yields `False`. The set of numeric characters covers digit characters along with every character carrying the Unicode numeric value property — for instance, U+2155, VULGAR FRACTION ONE FIFTH. Strictly speaking, numeric characters are the ones whose property value is Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric. Consider this:

```pycon
>>> '0123456789'.isnumeric()
True
>>> '٠١٢٣٤٥٦٧٨٩'.isnumeric()  # Arabic-Indic digits zero to nine
True
>>> '⅕'.isnumeric()  # Vulgar fraction one fifth
True
>>> '²'.isdecimal(), '²'.isdigit(),  '²'.isnumeric()
(False, True, True)

```

See also `isdecimal()` and `isdigit()`.

 str.isprintable()

Yields `True` when each character of the string is printable, and `False` when one or more non-printable characters appear.

In this context “printable” signifies that the character is fit for [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) to place in its output; a “non-printable” character is one that `repr()` on built-in types will render via hex escape. This says nothing about how strings sent to [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) or [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) are treated.

A character qualifies as printable when, inside the Unicode character database (refer to [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata)), its general category sits in one of the groups Letter, Mark, Number, Punctuation, or Symbol (L, M, N, P, or S); the ASCII space 0x20 also qualifies. By contrast, characters in group Separator or Other (Z or C) count as nonprintable, with the ASCII space again being the exception.

Consider this:

```pycon
>>> ''.isprintable(), ' '.isprintable()
(True, True)
>>> '\t'.isprintable(), '\n'.isprintable()
(False, False)

```

See also `isspace()`.

 str.isspace()

Yields `True` when the string holds only whitespace characters and at least one character is present; otherwise yields `False`.

Consider this:

```pycon
>>> ''.isspace()
False
>>> ' '.isspace()
True
>>> '\t\n'.isspace() # TAB and BREAK LINE
True
>>> '\u3000'.isspace() # IDEOGRAPHIC SPACE
True

```

A character counts as *whitespace* when, in the Unicode character database (refer to [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata)), its general category is `Zs` (“Separator, space”), or alternatively its bidirectional class is any of `WS`, `B`, or `S`.

See also `isprintable()`.

[Subject index](INDEX.md) · [Continue](str-istitle-to-str-lower.md) · [Owning module, declaration or section: String Methods](str-capitalize-to-str-count.md) · [Owning module, declaration or section: str.isidentifier](str-isalpha-to-str-isidentifier.md) · [Preceding source contract and version conditions](str-isalpha-to-str-isidentifier.md)
