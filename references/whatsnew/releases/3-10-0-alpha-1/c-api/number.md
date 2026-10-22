# Python 3.10.0 alpha 1 / c api / number

[bpo-40792](https://bugs.python.org/issue?@action=redirect&bpo=40792): What [`PyNumber_Index()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_Index) returns is from now on guaranteed to be of the exact type [`int`](https://docs.python.org/3.14/library/functions.html#int). Beforehand the result might have been an instance of an `int` subclass.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
