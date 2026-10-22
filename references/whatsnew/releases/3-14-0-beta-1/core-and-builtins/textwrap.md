# Python 3.14.0 beta 1 / core and builtins / textwrap

[gh-103997](https://github.com/python/cpython/issues/103997): A string argument given to "-c" is now dedented automatically, as though [`textwrap.dedent()`](https://docs.python.org/3.14/library/textwrap.html#textwrap.dedent) had been applied. As a result, "python -c" calls may be indented inside shell scripts without triggering indentation errors. Jon Crall and Steven Sun wrote this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
