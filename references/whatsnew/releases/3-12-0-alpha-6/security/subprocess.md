# Python 3.12.0 alpha 6 / security / subprocess

[gh-101283](https://github.com/python/cpython/issues/101283): When launching with `shell=True`, [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) now locates `cmd.exe` through a safer route. Eryk Sun supplied the patch, building on one from Oleg Iarygin.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
