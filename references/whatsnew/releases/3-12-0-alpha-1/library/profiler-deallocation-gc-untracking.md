# Python 3.12.0 alpha 1 / library / gc crash struck freeing lsprof profiler fixed untracking before any

[gh-95045](https://github.com/python/cpython/issues/95045): A GC crash that struck when freeing `_lsprof.Profiler` is fixed by untracking it before any callbacks fire. Kumar Aditya wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
