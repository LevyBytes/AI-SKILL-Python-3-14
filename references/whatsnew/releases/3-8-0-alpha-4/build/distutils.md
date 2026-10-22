# Python 3.8.0 alpha 4 / build / distutils

[bpo-21536](https://bugs.python.org/issue?@action=redirect&bpo=21536): Outside of Android and Cygwin, C extensions on Unix are no longer linked against libpython.

A statically linked Python is now able to load a C extension that was built using a shared library Python.

For an embedded Python, `libpython` has to be loaded with `RTLD_GLOBAL` rather than `RTLD_LOCAL`. Under the old `RTLD_LOCAL` approach it was already impossible to load C extensions that were not linked to `libpython`, for instance the standard library's C extensions produced by the `*shared*` section of `Modules/Setup`.

distutils, python-config and python-config.py were all changed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
