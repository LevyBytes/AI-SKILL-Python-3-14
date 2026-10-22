# Python 3.13.0 alpha 4 / library / exceptions and tracebacks

[gh-97928](https://github.com/python/cpython/issues/97928): Roll back, in part, how `tkinter.Text.count()` behaves. The default keeps the behavior seen in earlier Python releases, with the exception that assigning `wantobjects` a value of 0 stops having any effect. A fresh parameter *return_ints* arrives: passing `return_ints=True` causes `Text.count()` to always hand back the lone count as an integer rather than a 1-tuple or `None`.

[gh-114628](https://github.com/python/cpython/issues/114628): Should csv.Error surface while a TypeError is being processed, suppress printing of the TypeError traceback.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
