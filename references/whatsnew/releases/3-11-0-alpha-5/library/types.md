# Python 3.11.0 alpha 5 / library / types

[bpo-46510](https://bugs.python.org/issue?@action=redirect&bpo=46510): Supply a missing test covering [`types.TracebackType`](https://docs.python.org/3.14/library/types.html#types.TracebackType) and [`types.FrameType`](https://docs.python.org/3.14/library/types.html#types.FrameType). Derive them straight from the caught exception rather than invoking [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
