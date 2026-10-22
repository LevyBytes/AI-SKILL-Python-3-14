# Python 3.9.0 alpha 1 / core and builtins / exceptions and tracebacks

[bpo-37619](https://bugs.python.org/issue?@action=redirect&bpo=37619): Whenever a wrapper descriptor is carried from one class over to a different class (for instance, assigning `__add__ = str.__add__` onto an `int` subclass), invoking the operator now correctly raises an exception.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
