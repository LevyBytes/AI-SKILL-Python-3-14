# Python 3.12.0 alpha 4 / library / enum

[gh-100098](https://github.com/python/cpython/issues/100098): Stop `tuple` subclasses from being downcast to `tuple` when serving as enum values.

[gh-94943](https://github.com/python/cpython/issues/94943): Add [Dataclass support](https://docs.python.org/3.14/howto/enum.html#enum-dataclass-support) to the [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) [`__repr__()`](https://docs.python.org/3.14/library/enum.html#enum.Enum.__repr__). When a member subclasses a [`dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass), the value portion of the member [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) lists only field names and omits the dataclass? class name.

[gh-92122](https://github.com/python/cpython/issues/92122): Repair reStructuredText syntax errors found in docstrings within the [`enum`](https://docs.python.org/3.14/library/enum.html#module-enum) module.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
