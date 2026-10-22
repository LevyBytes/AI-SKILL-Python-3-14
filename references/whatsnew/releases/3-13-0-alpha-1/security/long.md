# Python 3.13.0 alpha 1 / security / long

[gh-102509](https://github.com/python/cpython/issues/102509): Whenever [`PyLongObject`](https://docs.python.org/3.14/c-api/long.html#c.PyLongObject) objects are created, `ob_digit` now gets initialized from the start. Illia Volochii authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
