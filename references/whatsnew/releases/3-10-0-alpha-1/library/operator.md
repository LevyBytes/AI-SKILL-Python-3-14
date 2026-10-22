# Python 3.10.0 alpha 1 / library / operator

[bpo-40792](https://bugs.python.org/issue?@action=redirect&bpo=40792): What [`operator.index()`](https://docs.python.org/3.14/library/operator.html#operator.index) returns now always carries the exact type [`int`](https://docs.python.org/3.14/library/functions.html#int). Earlier, that result might have been an instance of an `int` subclass.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
