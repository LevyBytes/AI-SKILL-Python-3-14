# Python 3.10.0 alpha 4 / library / sys

[bpo-42639](https://bugs.python.org/issue?@action=redirect&bpo=42639): `atexit._run_exitfuncs()` now reports callback exceptions through [`sys.unraisablehook`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook) instead of writing them straight to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) and then re-raising the final exception.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
