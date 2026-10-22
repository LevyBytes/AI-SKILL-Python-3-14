# Python 3.14.0 release candidate 2 / library / dataclasses

[gh-135228](https://github.com/python/cpython/issues/135228): Once [`dataclasses`](https://docs.python.org/3.14/library/dataclasses.html#module-dataclasses) swaps a class out for a slotted dataclass, the original class is again collectable by the garbage collector. A previous Python 3.14 change had kept that class alive permanently next to the substitute class that `dataclasses` builds.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
