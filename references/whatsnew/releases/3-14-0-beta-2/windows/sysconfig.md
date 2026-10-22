# Python 3.14.0 beta 2 / windows / sysconfig

[gh-133779](https://github.com/python/cpython/issues/133779): Undoes the change that produced differing `pyconfig.h` files according to compiler settings, since it kept breaking extension builds. Specifically, the `Py_GIL_DISABLED` preprocessor variable now has to be defined explicitly every time you compile for the experimental free-threaded runtime. You can call the [`sysconfig.get_config_var()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_config_var) function to learn whether the active runtime was built with that flag.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
