# Python 3.14.0 alpha 6 / library / annotationlib

[gh-128184](https://github.com/python/cpython/issues/128184): Improves how an [`annotationlib.ForwardRef`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef) object shows up inside [`inspect.Signature`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature) representations. It additionally clears a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) that surfaced while applying [`dataclasses.dataclass()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass) to classes carrying unresolvable forward references.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
