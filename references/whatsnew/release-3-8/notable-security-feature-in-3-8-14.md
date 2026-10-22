# What’s New In Python 3.8 / Notable security feature in 3.8.14 — sys

### Notable security feature in 3.8.14

Translating between [`int`](https://docs.python.org/3.14/library/functions.html#int) and [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) for bases apart from 2 (binary), 4, 8 (octal), 16 (hexadecimal), or 32 — base 10 (decimal) among them — will now throw a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) once the digit count of the string representation crosses a ceiling, guarding against possible denial-of-service attacks rooted in the algorithmic cost. It serves as a countermeasure for [**CVE 2020-10735**](https://www.cve.org/CVERecord?id=CVE-2020-10735). You may adjust or switch off this ceiling through an environment variable, a command-line flag, or the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) APIs. The [integer string conversion length limitation](https://docs.python.org/3.14/library/stdtypes.html#int-max-str-digits) documentation covers it. Out of the box the ceiling sits at 4300 digits in string form.

[Subject index](INDEX.md) · [Previous source section](changes-in-the-python-api.md) · [Next source section](tarfile.md) · [Release/subject declaration](assignment-expressions.md)
