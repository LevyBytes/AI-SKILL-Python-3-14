# Python 3.12.0 alpha 7 / library / dataclasses

[gh-102947](https://github.com/python/cpython/issues/102947): Sharpen the traceback produced when [`dataclasses.fields()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.fields) runs against something that is not a dataclass. Alex Waygood wrote the patch

[gh-102578](https://github.com/python/cpython/issues/102578): Mutating or removing attributes on non-dataclass subclasses of frozen dataclasses is now quicker. Because of how `__setattr__` and `__delattr__` are written for frozen dataclasses, the cost here used to be *O*(*n*); the cost is now *O*(1).

[gh-102103](https://github.com/python/cpython/issues/102103): A `module` argument was added to [`dataclasses.make_dataclass()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.make_dataclass), and the classes it builds can now be pickled.

[gh-98886](https://github.com/python/cpython/issues/98886): Resolve problems that arose when declaring dataclasses whose fields carry particular underscore names that [`dataclasses`](https://docs.python.org/3.14/library/dataclasses.html#module-dataclasses) does not plainly reserve.

[gh-98169](https://github.com/python/cpython/issues/98169): Stop [`dataclasses.astuple()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.astuple) from crashing when a [`collections.defaultdict`](https://docs.python.org/3.14/library/collections.html#collections.defaultdict) appears among the attributes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
