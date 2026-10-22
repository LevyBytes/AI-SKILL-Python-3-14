# Identifying free-threaded Python

### Identifying free-threaded Python

You can confirm that the interpreter in use offers free threading because both [`python -VV`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-V) and [`sys.version`](https://docs.python.org/3.14/library/sys.html#sys.version) include the phrase “free-threading build”. To verify at runtime whether the GIL is genuinely off in the live process, call the recently added [`sys._is_gil_enabled()`](https://docs.python.org/3.14/library/sys.html#sys._is_gil_enabled) function.

Whether a given build offers free threading can be read from the `sysconfig.get_config_var("Py_GIL_DISABLED")` configuration variable. A value of `1` indicates that free threading is available in that build. For anything that hinges on build configuration, prefer this approach.

[Subject index](INDEX.md) · [Previous source context](installation.md) · [Following source context](the-global-interpreter-lock-in-free-threaded-python.md)
