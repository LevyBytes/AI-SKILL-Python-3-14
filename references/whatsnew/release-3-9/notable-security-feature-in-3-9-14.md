# What's New In Python 3.9 / Notable security feature in 3.9.14 - sys

### Notable security feature in 3.9.14

Going between [`int`](https://docs.python.org/3.14/library/functions.html#int) and [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) in any base apart from 2 (binary), 4, 8 (octal), 16 (hexadecimal), or 32 — base 10 (decimal) among them — from now on throws a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) once the digit count of the string form passes a ceiling, guarding against denial-of-service attacks rooted in the algorithmic complexity. It serves as a mitigation for [**CVE 2020-10735**](https://www.cve.org/CVERecord?id=CVE-2020-10735). You can tune or turn off this ceiling through an environment variable, a command line flag, or the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) APIs. Refer to the [integer string conversion length limitation](https://docs.python.org/3.14/library/stdtypes.html#int-max-str-digits) documentation. Out of the box the ceiling sits at 4300 digits of string form.

[Subject index](INDEX.md) · [Previous source section](urllib-parse.md) · [Next source section](tarfile.md) · [Release/subject declaration](summary-release-highlights.md)
