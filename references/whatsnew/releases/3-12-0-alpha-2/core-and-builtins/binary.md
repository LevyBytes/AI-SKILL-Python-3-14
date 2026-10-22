# Python 3.12.0 alpha 2 / core and builtins / binary

[gh-99204](https://github.com/python/cpython/issues/99204): Correct how `sys._base_executable` is computed inside a POSIX virtual environment that copies the python binary, in cases where the base installation lacks the executable name the venv uses. The computation now falls back to alternative names ("python&lt;MAJOR&gt;", "python&lt;MAJOR&gt;.&lt;MINOR&gt;").

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
