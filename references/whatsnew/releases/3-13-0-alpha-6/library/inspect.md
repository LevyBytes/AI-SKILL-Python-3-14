# Python 3.13.0 alpha 6 / library / inspect

[bpo-27578](https://bugs.python.org/issue?@action=redirect&bpo=27578): [`inspect.getsource()`](https://docs.python.org/3.14/library/inspect.html#inspect.getsource) (alongside its sibling functions) now copes with empty module files: rather than throwing `OSError`, it yields `'\n'` (or a sensible equivalent). Kernc wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
