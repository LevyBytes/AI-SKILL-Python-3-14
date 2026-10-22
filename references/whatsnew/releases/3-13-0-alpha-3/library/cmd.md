# Python 3.13.0 alpha 3 / library / cmd

[gh-52161](https://github.com/python/cpython/issues/52161): Before writing them out, [`cmd.Cmd.do_help()`](https://docs.python.org/3.14/library/cmd.html#cmd.Cmd.do_help) now tidies docstrings using [`inspect.cleandoc()`](https://docs.python.org/3.14/library/inspect.html#inspect.cleandoc). Filip ??apkiewicz wrote the patch.

[gh-102130](https://github.com/python/cpython/issues/102130): Bring tab completion to [`cmd`](https://docs.python.org/3.14/library/cmd.html#module-cmd) under `editline`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
