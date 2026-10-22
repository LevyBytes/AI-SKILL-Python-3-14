# Python 3.5.1 release candidate 1 / core and builtins / repaired partly broken sanity check within posixsubprocess internals concerning

[bpo-23564](https://bugs.python.org/issue?@action=redirect&bpo=23564): Repaired a partly broken sanity check within the _posixsubprocess internals concerning the way fds_to_pass reached the child. Because subprocess.py already steered clear of it, the bug carried no real consequence.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
