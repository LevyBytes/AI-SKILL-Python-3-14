# Python 3.14.1 final / core and builtins / debug

[gh-140358](https://github.com/python/cpython/issues/140358): Bring back elapsed time alongside the unreachable object count in GC debug output. A refactor of `gc.c` had dropped them by accident. Once more the debug log states the elapsed collection time together with how many unreachable objects there were. Pål Grønås Drange contributed this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
