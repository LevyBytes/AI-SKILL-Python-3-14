# What’s New in Python 2.4 / PEP 237: Unifying Long Integers and Integers

### PEP 237: Unifying Long Integers and Integers

Kicked off back in Python 2.2, this PEP’s drawn-out migration advances another notch with Python 2.4. Under 2.3, a handful of integer operations whose behavior would shift once int and long merged raised [`FutureWarning`](https://docs.python.org/3.14/library/exceptions.html#FutureWarning) warnings while returning results capped at 32 or 64 bits (your platform decides which). Come 2.4, those same expressions stop emitting a warning and instead hand back a different result, typically a long integer.

The expressions that caused trouble were chiefly left shifts plus large hexadecimal and octal literals. Take `2 << 32`, for example: under 2.3 it raises a warning and evaluates to 0 on 32-bit platforms. With Python 2.4, that same expression now yields the proper value, 8589934592.

See also

[**PEP 237**](https://peps.python.org/pep-0237/) - Unifying Long Integers and Integers

The PEP was originally drafted by Moshe Zadka and GvR. Kalle Svensson coded the 2.4 changes.

[Subject index](INDEX.md) · [Previous source section](pep-218-built-in-set-objects.md) · [Next source section](pep-289-generator-expressions.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
