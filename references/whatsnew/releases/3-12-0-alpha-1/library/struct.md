# Python 3.12.0 alpha 1 / library / struct

[gh-96735](https://github.com/python/cpython/issues/96735): Undefined behaviour within [`struct.unpack()`](https://docs.python.org/3.14/library/struct.html#struct.unpack) is corrected.

[gh-78724](https://github.com/python/cpython/issues/78724): A crash in [`struct.Struct`](https://docs.python.org/3.14/library/struct.html#struct.Struct) arising when it was not fully initialized is fixed by performing initialization within [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__). Kumar Aditya wrote the patch.

[gh-94254](https://github.com/python/cpython/issues/94254): The types belonging to the [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module are made immutable. Kumar Aditya wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
