# Python 3.14.1 final / library / typing

[gh-140348](https://github.com/python/cpython/issues/140348): Addresses a Python 3.14.0 regression in which applying the `|` operator to a [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) object alongside something that is not a type would throw an error.

[gh-139905](https://github.com/python/cpython/issues/139905): For [`typing.Generic`](https://docs.python.org/3.14/library/typing.html#typing.Generic) subclasses, a suggestion is appended to the error message when `cls.__parameters__` goes missing because some parent class neglected to call [`super().__init_subclass__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init_subclass__) inside its `__init_subclass__`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
