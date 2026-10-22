# Python 3.14.0 alpha 2 / library / importlib

[gh-126066](https://github.com/python/cpython/issues/126066): Make [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) avoid writing partial .pyc files whenever a ulimit or another operating system mechanism stops the write from completing in full.

[gh-125519](https://github.com/python/cpython/issues/125519): Make the traceback better whenever [`importlib.reload()`](https://docs.python.org/3.14/library/importlib.html#importlib.reload) gets called with something that is not a module. Alex Waygood wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
