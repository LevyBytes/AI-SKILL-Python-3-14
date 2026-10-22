# Python 3.14.0 beta 1 / library / typing

[gh-132882](https://github.com/python/cpython/issues/132882): Repair the copying of [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) objects that hold members which lack support for the `|` operator.

[gh-132493](https://github.com/python/cpython/issues/132493): [`typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol) will now call [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) while determining via [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) whether an instance satisfies the protocol. That makes `isinstance` checks work against classes whose annotations are deferred.

[gh-132493](https://github.com/python/cpython/issues/132493): Permit building [`typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol) classes whose annotations are impossible to resolve while the class itself is being created.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
