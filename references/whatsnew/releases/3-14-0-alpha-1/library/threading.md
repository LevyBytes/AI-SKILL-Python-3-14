# Python 3.14.0 alpha 1 / library / threading

[gh-121474](https://github.com/python/cpython/issues/121474): Add back the absent sanity check covering the `parties` arg inside the [`threading.Barrier`](https://docs.python.org/3.14/library/threading.html#threading.Barrier) constructor. Patch by Clinton Christian (pygeek).

[gh-117983](https://github.com/python/cpython/issues/117983): Postpone the `threading` import within `importlib.util` until lazy loading actually kicks in.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
