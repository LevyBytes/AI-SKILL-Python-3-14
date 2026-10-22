# Python 3.6.0 alpha 1 / core and builtins / repair partially broken sanity check within posixsubprocess internals concerning

[bpo-23564](https://bugs.python.org/issue?@action=redirect&bpo=23564): Repair a partially broken sanity check within the _posixsubprocess internals concerning the way fds_to_pass reached the child. The bug carried no real impact since subprocess.py was already steering clear of it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
