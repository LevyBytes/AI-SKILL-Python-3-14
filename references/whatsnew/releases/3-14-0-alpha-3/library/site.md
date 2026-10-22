# Python 3.14.0 alpha 3 / library / site

[gh-126985](https://github.com/python/cpython/issues/126985): While running inside a virtual environment that has the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module disabled (refer to [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S)), both [`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix) and [`sys.base_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_prefix) will now refer to that virtual environment rather than the base installation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
