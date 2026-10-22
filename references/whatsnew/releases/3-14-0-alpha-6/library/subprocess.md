# Python 3.14.0 alpha 6 / library / subprocess

[gh-118761](https://github.com/python/cpython/issues/118761): Backs out a change from the prior release that tried to make certain stdlib imports inside the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module lazy, since doing so threw errors during `__del__` finalizers that invoke methods like `terminate`, `kill`, or `send_signal`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
