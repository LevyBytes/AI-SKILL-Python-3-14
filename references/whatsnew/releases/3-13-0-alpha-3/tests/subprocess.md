# Python 3.13.0 alpha 3 / tests / subprocess

[gh-112334](https://github.com/python/cpython/issues/112334): A regression test now confirms that `vfork()` gets used where [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) expects it on vfork enabled POSIX systems (Linux).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
