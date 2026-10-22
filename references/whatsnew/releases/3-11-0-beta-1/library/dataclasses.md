# Python 3.11.0 beta 1 / library / dataclasses

[gh-91215](https://github.com/python/cpython/issues/91215): For [`@~dataclasses.dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass), introduce *weakref_slot*. This new parameter has a default of `False`. When true together with `slots=True`, a slot called `"__weakref__"` is added so that instances can be weakref'd. Eric V. Smith contributed this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
