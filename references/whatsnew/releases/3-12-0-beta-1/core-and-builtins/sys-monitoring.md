# Python 3.12.0 beta 1 / core and builtins / sys monitoring

[gh-103082](https://github.com/python/cpython/issues/103082): Adjust how `sys.monitoring.events.LINE` events behave under `sys.monitoring`: rather than the static approximation used previously, line events now fire as each new line is reached dynamically. The result closely tracks the behavior of "line" events in `sys.settrace`, which should make moving tools from 3.11 to 3.12 smoother.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
