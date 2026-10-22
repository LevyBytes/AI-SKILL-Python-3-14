# stdtypes: `str.format()`, `str.format_map()`, `str.index()`, `str.isalnum()`

str.format(**args*, ***kwargs*)

Carry out a string formatting operation. Whatever string this method runs on may hold plain text together with replacement fields wrapped in braces `{}`. Inside each replacement field goes either a positional argument's numeric index or a keyword argument's name. The return value is a copy of the string in which every replacement field has been swapped for the string value of its matching argument. To illustrate:

```pycon
>>> "The sum of 1 + 2 is {0}".format(1+2)
'The sum of 1 + 2 is 3'
>>> "The sum of {a} + {b} is {answer}".format(answer=1+2, a=1, b=2)
'The sum of 1 + 2 is 3'
>>> "{1} expects the {0} Inquisition!".format("Spanish", "Nobody")
'Nobody expects the Spanish Inquisition!'

```

Turn to [Format string syntax](https://docs.python.org/3.14/library/string.html#formatstrings) for a rundown of the assorted formatting options you can name within format strings.

Note

Whenever a number ([`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`complex`](https://docs.python.org/3.14/library/functions.html#complex), [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) and subclasses) is formatted under the `n` type (for example `'{:n}'.format(1234)`), the routine briefly switches the `LC_CTYPE` locale over to the `LC_NUMERIC` locale so it can read the `decimal_point` and `thousands_sep` entries from `localeconv()` — but only when those entries run past 1 byte or hold non-ASCII content and the `LC_NUMERIC` locale fails to match the `LC_CTYPE` locale. Other threads feel the effect of that brief switch.

Changed in version 3.7: In certain situations, formatting a number under the `n` type makes the routine briefly flip the `LC_CTYPE` locale to the `LC_NUMERIC` locale.

 str.format_map(*mapping*, */*)

Behaves like `str.format(**mapping)`, the difference being that `mapping` is consulted directly rather than copied into a `dict`. That proves handy where, for instance, `mapping` happens to be a dict subclass:

```python
>>> class Default(dict):
...     def __missing__(self, key):
...         return key
...
>>> '{name} was born in {country}'.format_map(Default(name='Guido'))
'Guido was born in country'

```

Added in version 3.2.

 str.index(*sub*[, *start*[, *end*]])

Behaves like `find()`, except it raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever the substring goes unfound. To illustrate:

```pycon
>>> 'spam, spam, spam'.index('spam')
0
>>> 'spam, spam, spam'.index('eggs')
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    'spam, spam, spam'.index('eggs')
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
ValueError: substring not found

```

See also `rindex()`.

 str.isalnum()

Hand back `True` where every character in the string is alphanumeric and at least one character is present, and `False` otherwise. A character `c` qualifies as alphanumeric when any of these yields `True`: `c.isalpha()`, `c.isdecimal()`, `c.isdigit()`, or `c.isnumeric()`. To illustrate:

```pycon
>>> 'abc123'.isalnum()
True
>>> 'abc123!@#'.isalnum()
False
>>> ''.isalnum()
False
>>> ' '.isalnum()
False

```

[Subject index](INDEX.md) · [Previous](str-encode-to-str-find.md) · [Continue](str-isalpha-to-str-isidentifier.md) · [Owning module, declaration or section: String Methods](str-capitalize-to-str-count.md)
