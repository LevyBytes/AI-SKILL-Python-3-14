# Python 3.14.4 final / library / annotationlib

[gh-146556](https://github.com/python/cpython/issues/146556): Corrects [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) hanging forever when invoked with `eval_str=True` against a callable carrying a circular `__wrapped__` chain (for instance `f.__wrapped__ = f`). Cycle detection through an id-based visited set now halts the traversal and reverts to the globals discovered up to that point, echoing how [`inspect.unwrap()`](https://docs.python.org/3.14/library/inspect.html#inspect.unwrap) behaves.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
