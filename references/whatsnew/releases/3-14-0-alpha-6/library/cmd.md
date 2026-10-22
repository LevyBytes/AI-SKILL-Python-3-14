# Python 3.14.0 alpha 6 / library / cmd

[gh-118761](https://github.com/python/cpython/issues/118761): Shortens the import time of [`cmd`](https://docs.python.org/3.14/library/cmd.html#module-cmd) by lazily importing [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) and dropping [`string`](https://docs.python.org/3.14/library/string.html#module-string). Semyon Moroz wrote this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
