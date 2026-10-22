# Python 3.11.0 alpha 5 / library / exceptions

[bpo-41403](https://bugs.python.org/issue?@action=redirect&bpo=41403): Have `mock.patch()` throw a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) carrying a meaningful message when given an invalid arg. Formerly a baffling [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) was allowed to leak out.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
