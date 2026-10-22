# Python 3.14.1 final / core and builtins / functions

[gh-140406](https://github.com/python/cpython/issues/140406): Resolve a memory leak that arises once an object’s [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) method yields something that is not an [`int`](https://docs.python.org/3.14/library/functions.html#int).

[gh-139748](https://github.com/python/cpython/issues/139748): Resolve reference leaks within the error branches of functions that accept path strings or bytes, among them [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) plus [`os.system()`](https://docs.python.org/3.14/library/os.html#os.system). Bénédikt Tran supplied the patch.

[gh-140517](https://github.com/python/cpython/issues/140517): Resolved a reference leak that appeared while iterating across the result of [`map()`](https://docs.python.org/3.14/library/functions.html#map) under `strict=True` whenever the supplied iterables differ in length. Mikhail Efimov supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
