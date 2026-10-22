# Python 3.13.0 alpha 4 / core and builtins / functions

[gh-55664](https://github.com/python/cpython/issues/55664): Emit a warning when a [`type`](https://docs.python.org/3.14/library/functions.html#type) is created from a namespace dictionary whose keys are not strings. Daniel Urban and Furkan Onder contributed the patch.

[gh-112087](https://github.com/python/cpython/issues/112087): An empty reverse iterator over a list will now collapse to [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed). Donghee Na contributed the patch

[gh-114828](https://github.com/python/cpython/issues/114828): Repair the compilation crashes seen in unusual code that calls [`super()`](https://docs.python.org/3.14/library/functions.html#super) within a comprehension inside a class body.

[gh-115011](https://github.com/python/cpython/issues/115011): For an object that provides an [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method, setters of unsigned-integer-typed members now accept the same span of valid values that an [`int`](https://docs.python.org/3.14/library/functions.html#int) does.

[gh-76763](https://github.com/python/cpython/issues/76763): For arguments outside the permitted range, the [`chr()`](https://docs.python.org/3.14/library/functions.html#chr) builtin now consistently raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). It used to raise [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) for extreme magnitudes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
