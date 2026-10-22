# Python 3.14.5 release candidate 1 / library / dataclasses

[gh-148947](https://github.com/python/cpython/issues/148947): Stop a crash in [`@dataclasses.dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass) using `slots=True` that arose whenever a function defined inside the class carried an empty `__class__` cell.

[gh-105936](https://github.com/python/cpython/issues/105936): Trying to change non-field attributes of a [`dataclasses`](https://docs.python.org/3.14/library/dataclasses.html#module-dataclasses) instance where both *frozen* and *slots* are `True` now triggers [`FrozenInstanceError`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.FrozenInstanceError) in place of [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Non-dataclass subclasses may now alter non-field attributes freely, and the original non-slotted class becomes eligible for garbage collection.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
