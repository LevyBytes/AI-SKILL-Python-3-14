# Python 3.14.0 alpha 5 / library / sysconfig

[gh-92897](https://github.com/python/cpython/issues/92897): The `check_home` argument of [`sysconfig.is_python_build()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.is_python_build) is now scheduled for deprecation in Python 3.15.

[gh-129064](https://github.com/python/cpython/issues/129064): Mark `sysconfig.expand_makefile_vars()` as deprecated; prefer calling [`sysconfig.get_paths()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_paths) together with the `vars` argument instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
