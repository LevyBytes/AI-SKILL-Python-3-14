# Python 3.14.0 alpha 1 / library / site

[gh-125096](https://github.com/python/cpython/issues/125096): When the [`PYTHON_BASIC_REPL`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_BASIC_REPL) environment variable is present, the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module skips importing the `_pyrepl` module. On top of that, the `site` module now honors the [`-E`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-E) and [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I) command line options: under those, `PYTHON_BASIC_REPL` is ignored. Patch by Victor Stinner.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
