# Python 3.14.0 release candidate 3 / library / exceptions

[gh-138804](https://github.com/python/cpython/issues/138804): Throw [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) rather than [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) whenever a wrongly typed argument reaches [`shlex.quote()`](https://docs.python.org/3.14/library/shlex.html#shlex.quote). That brings back how the function acted before 3.14.

[gh-138514](https://github.com/python/cpython/issues/138514): Throw [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever a string with more than one character reaches the *echo_char* parameter of [`getpass.getpass()`](https://docs.python.org/3.14/library/getpass.html#getpass.getpass). Benjamin Johnson contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
