# Python 3.14.1 final / library / dataclasses

[gh-137530](https://github.com/python/cpython/issues/137530): [`dataclasses`](https://docs.python.org/3.14/library/dataclasses.html#module-dataclasses) Corrects the annotations on generated `__init__` methods: the in-line annotations that previously lived in the generated source code are swapped out for `__annotate__` functions attached to those methods.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
