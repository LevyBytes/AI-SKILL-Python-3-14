# Python 3.12.0 beta 1 / library / argparse

[gh-101640](https://github.com/python/cpython/issues/101640): [`argparse.ArgumentParser`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser) now traps errors that arise while writing messages, for instance whenever [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) is `None`. Oleg Iarygin authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
