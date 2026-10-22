# lexical analysis: F-string nesting, comments and format specifications

**CPython implementation detail:** CPython places no cap on how deeply f-strings may nest.

Newlines are permitted in replacement expressions for both single-quoted and triple-quoted f-strings, and such expressions may carry comments. Anything trailing a `#` within a replacement field counts as a comment (closing braces and quotes included). Because of this, a replacement field bearing a comment has to be closed on a separate line:

```text
>>> a = 2
>>> f"abc{a  # This comment  }"  continues until the end of the line
...       + 3}"
'abc5'

```

Following the expression, a replacement field may, as an option, hold:

- a *debug specifier* – an equal sign (`=`), with optional whitespace flanking it on one or both sides;

- a *conversion specifier* – `!s`, `!r` or `!a`; and/or

- a *format specifier* introduced by a colon (`:`).

For specifics on how these fields get evaluated, consult the [Standard Library section on f-strings](https://docs.python.org/3.14/library/stdtypes.html#stdtypes-fstrings).

As that section describes, *format specifiers* are handed to the [`format()`](https://docs.python.org/3.14/library/functions.html#format) function as its second argument so a replacement field's value gets formatted. As an example, they let you set a field width together with padding characters by way of the [Format Specification Mini-Language](https://docs.python.org/3.14/library/string.html#formatspec):

```python
>>> number = 14.3
>>> f'{number:20.7f}'
'          14.3000000'

```

A top-level format specifier is permitted to carry nested replacement fields of its own:

```python
>>> field_size = 20
>>> precision = 7
>>> f'{number:{field_size}.{precision}f}'
'          14.3000000'

```

Such nested fields are themselves free to carry their own conversion fields plus [format specifiers](https://docs.python.org/3.14/library/string.html#formatspec):

```python
>>> number = 3
>>> f'{number:{field_size}}'
'                   3'
>>> f'{number:{field_size:05}}'
'00000000000000000003'

```

That said, these nested fields are not permitted to carry replacement fields nested any more deeply.

Even when no expressions appear inside them, formatted string literals are not usable as [docstrings](https://docs.python.org/3.14/glossary.html#term-docstring):

```python
>>> def foo():
...     f"Not a docstring"
...
>>> print(foo.__doc__)
None

```

See also

- [**PEP 498**](https://peps.python.org/pep-0498/) – Literal String Interpolation

- [**PEP 701**](https://peps.python.org/pep-0701/) – Syntactic formalization of f-strings


- [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format), which uses a related format string mechanism.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Owning language section](f-strings-a-to-c.md) · [Contract or procedure setup](f-strings-a-to-c.md) · [Previous source section](f-strings-a-to-c.md) · [Following source section](t-strings.md)
