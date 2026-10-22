# Python 3.12.0 alpha 2 / library / sysconfig

[gh-92452](https://github.com/python/cpython/issues/92452): Resolved a race condition able to make [`sysconfig.get_config_var()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_config_var) wrongly hand back [`None`](https://docs.python.org/3.14/library/constants.html#None) within multi-threaded programs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
