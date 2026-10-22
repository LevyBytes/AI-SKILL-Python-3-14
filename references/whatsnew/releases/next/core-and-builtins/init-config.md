# Python next / core and builtins / init config

[gh-151218](https://github.com/python/cpython/issues/151218): [`PyConfig_Set()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Set) together with [`sys.set_int_max_str_digits()`](https://docs.python.org/3.14/library/sys.html#sys.set_int_max_str_digits) now swap out [`sys.flags`](https://docs.python.org/3.14/library/sys.html#sys.flags) (building a fresh object) rather than altering `sys.flags` in place. Victor Stinner authored the change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
