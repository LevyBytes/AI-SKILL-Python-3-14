# What’s New in Python 2.6 / PEP 3127: Integer Literal Support and Syntax

### PEP 3127: Integer Literal Support and Syntax

In Python 3.0 the notation for octal (base-8) integer literals changes: a leading zero gives way to a “0o” or “0O” prefix, and binary (base-2) integer literals become available, marked by a “0b” or “0B” prefix.

Although Python 2.6 keeps recognizing a leading 0 as the marker of an octal number, it additionally accepts “0o” and “0b”:

```python
>>> 0o21, 2*8 + 1
(17, 17)
>>> 0b101111
47

```

The [`oct()`](https://docs.python.org/3.14/library/functions.html#oct) builtin keeps emitting numbers with a leading-zero prefix, while a fresh [`bin()`](https://docs.python.org/3.14/library/functions.html#bin) builtin yields a number’s binary form:

```python
>>> oct(42)
'052'
>>> future_builtins.oct(42)
'0o52'
>>> bin(173)
'0b10101101'

```

When base-8 or base-2 is requested, or when the *base* argument is zero (telling the call to deduce the base from the string), the [`int()`](https://docs.python.org/3.14/library/functions.html#int) and `long()` builtins will now honor the “0o” and “0b” prefixes:

```python
>>> int ('0o52', 0)
42
>>> int('1101', 2)
13
>>> int('0b1101', 2)
13
>>> int('0b1101', 0)
13

```

See also

[**PEP 3127**](https://peps.python.org/pep-3127/) - Integer Literal Support and Syntax

PEP written by Patrick Maupin; backported to 2.6 by Eric Smith.

[Subject index](INDEX.md) · [Previous source section](pep-3119-abstract-base-classes-readonly.md) · [Next source section](pep-3129-class-decorators.md) · [Release/subject declaration](python-3-0.md)
