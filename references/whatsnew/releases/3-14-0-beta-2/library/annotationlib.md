# Python 3.14.0 beta 2 / library / annotationlib

[gh-133684](https://github.com/python/cpython/issues/133684): Repair the bug where [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) produced the wrong result for some classes belonging to a class hierarchy that uses `from __future__ import annotations`.

[gh-133551](https://github.com/python/cpython/issues/133551): Add t-strings ([**PEP 750**](https://peps.python.org/pep-0750/)) support to [`annotationlib`](https://docs.python.org/3.14/library/annotationlib.html#module-annotationlib). Patch by Jelle Zijlstra.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
