# What's New In Python 3.10 / Notable security feature in 3.10.7 - sys

### Notable security feature in 3.10.7

Translating an [`int`](https://docs.python.org/3.14/library/functions.html#int) to or from a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) in any base apart from 2 (binary), 4, 8 (octal), 16 (hexadecimal), or 32 — base 10 (decimal) being one such case — will now throw a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) once the digit count in the textual form exceeds a ceiling, the aim being to head off possible denial-of-service attacks rooted in the algorithm's complexity. The change serves as a safeguard against [**CVE 2020-10735**](https://www.cve.org/CVERecord?id=CVE-2020-10735). You can adjust or switch off this ceiling through an environment variable, a command line flag, or the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) APIs. Further detail lives in the [integer string conversion length limitation](https://docs.python.org/3.14/library/stdtypes.html#int-max-str-digits) documentation. Out of the box the ceiling sits at 4300 digits of textual form.

[Subject index](INDEX.md) · [Previous source section](removed-compiler-helper-apis.md) · [Next source section](notable-security-feature-in-3-10-8.md) · [Release/subject declaration](summary-release-highlights.md)
