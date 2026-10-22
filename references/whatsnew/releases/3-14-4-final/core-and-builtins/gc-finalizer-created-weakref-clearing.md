# Python 3.14.4 final / core and builtins / during garbage collection weakrefs pointing unreachable objects produced while

[gh-91636](https://github.com/python/cpython/issues/91636): During garbage collection, weakrefs pointing at unreachable objects produced while finalizers run are now cleared. Leaving such weakrefs uncleared could expose unreachable objects.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
