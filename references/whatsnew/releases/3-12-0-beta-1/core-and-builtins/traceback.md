# Python 3.12.0 beta 1 / core and builtins / traceback

[gh-102818](https://github.com/python/cpython/issues/102818): Refrain from pushing a frame onto the traceback within the `sys.setprofile` and `sys.settrace` trampoline functions. Doing so keeps frames from being duplicated should an exception arise inside the callback, and keeps frames from being dropped when a C callback runs without adding the frame itself.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
