# Python 3.14.0 beta 1 / library / faulthandler

[gh-127604](https://github.com/python/cpython/issues/127604): On platforms where it works, the C stack trace can now be printed, either through [`faulthandler.dump_c_stack()`](https://docs.python.org/3.14/library/faulthandler.html#faulthandler.dump_c_stack) or via the *c_stack* argument to [`faulthandler.enable()`](https://docs.python.org/3.14/library/faulthandler.html#faulthandler.enable).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
