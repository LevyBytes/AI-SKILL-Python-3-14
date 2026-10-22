# Python 3.11.0 beta 1 / core and builtins / ability chain classmethod descriptors bpo 19072 had added deprecated

[gh-89519](https://github.com/python/cpython/issues/89519): The ability to chain classmethod descriptors (which [bpo-19072](https://bugs.python.org/issue?@action=redirect&bpo=19072) had added) is now deprecated. Wrapping other descriptors with it, such as property(), is no longer permitted. This feature's underlying design had defects that spawned several problems further downstream.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
