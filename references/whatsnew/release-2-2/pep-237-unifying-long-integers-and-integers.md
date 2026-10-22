# What’s New in Python 2.2 / PEP 237: Unifying Long Integers and Integers

### PEP 237: Unifying Long Integers and Integers

Over the last few releases, the split between ordinary integers (32-bit quantities on the majority of machines) and long integers (which may grow to any size) had grown irritating. Consider, for instance, a platform handling files above `2**32` bytes: there the `tell()` method on file objects must hand back a long integer. Yet assorted corners of Python anticipated plain integers and threw an error when handed a long integer instead. As a case in point, under Python 1.5 a slice index had to be a regular integer, so `'abc'[1L:]` would throw a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception carrying the message ‘slice index must be int’.

Whenever it is needed, Python 2.2 promotes a value from a short integer to a long one. You no longer have to tack on an ‘L’ suffix to write a long integer literal, because the compiler now picks the right type itself. (Going forward, the ‘L’ suffix will be frowned upon across later 2.x releases, will set off a warning in Python 2.4, and is likely to disappear in Python 3.0.) Plenty of operations that formerly threw an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) now yield a long integer instead. As an example:

```python
>>> 1234567890123
1234567890123L
>>> 2 ** 64
18446744073709551616L

```

For the most part, you'll see integers and long integers handled the same way now. The [`type()`](https://docs.python.org/3.14/library/functions.html#type) built-in function still lets you tell them apart, though you'll seldom have cause to.

See also

[**PEP 237**](https://peps.python.org/pep-0237/) - Unifying Long Integers and Integers

Authored by Moshe Zadka and Guido van Rossum. The implementation was largely the work of Guido van Rossum.

[Subject index](INDEX.md) · [Previous source section](pep-255-simple-generators.md) · [Next source section](pep-238-changing-the-division-operator.md) · [Release/subject declaration](introduction.md)
