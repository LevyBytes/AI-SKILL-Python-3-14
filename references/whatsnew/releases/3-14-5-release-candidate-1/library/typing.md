# Python 3.14.5 release candidate 1 / library / typing

[gh-146553](https://github.com/python/cpython/issues/146553): Break the infinite loop in [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) that struck when `__wrapped__` made a cycle. Shamil Abdulaev wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
