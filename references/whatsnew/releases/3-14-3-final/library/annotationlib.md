# Python 3.14.3 final / library / annotationlib

[gh-143831](https://github.com/python/cpython/issues/143831): When created from annotation scopes that carry closures, [`annotationlib.ForwardRef`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef) objects are now hashable. Hashing such objects used to throw an exception. Bartosz Sławecki supplied the patch.

[gh-143517](https://github.com/python/cpython/issues/143517): When evaluating a stringified starred annotation that opens with one or more whitespace characters followed by a `*`, [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) no longer throws a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). Bartosz Sławecki supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
