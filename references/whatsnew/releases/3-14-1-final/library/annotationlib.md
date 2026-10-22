# Python 3.14.1 final / library / annotationlib

[gh-138764](https://github.com/python/cpython/issues/138764): Keeps [`annotationlib.call_annotate_function()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.call_annotate_function) from invoking `__annotate__` functions that lack `VALUE_WITH_FAKE_GLOBALS` support inside a fake globals namespace whose globals are empty.

Have `FORWARDREF` and `STRING` annotations drop back to `VALUE` annotations whenever neither their own format nor `VALUE_WITH_FAKE_GLOBALS` is supported.

[gh-138425](https://github.com/python/cpython/issues/138425): Corrects partial evaluation of those [`annotationlib.ForwardRef`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef) objects that depend on names declared as globals.

[gh-138151](https://github.com/python/cpython/issues/138151): Within [`annotationlib`](https://docs.python.org/3.14/library/annotationlib.html#module-annotationlib), forward references pointing at nonlocal variables that are still undefined at the moment annotations are first evaluated are now resolved better.

[gh-137969](https://github.com/python/cpython/issues/137969): Resolves a case where [`annotationlib.ForwardRef.evaluate()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef.evaluate) handed back [`ForwardRef`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef) objects that failed to refresh when new globals appeared.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
