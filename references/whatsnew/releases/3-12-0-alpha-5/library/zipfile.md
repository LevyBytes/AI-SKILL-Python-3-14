# Python 3.12.0 alpha 5 / library / zipfile

[gh-101144](https://github.com/python/cpython/issues/101144): Allow [`zipfile.Path.open()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.Path.open) and [`zipfile.Path.read_text()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.Path.read_text) to take `encoding` positionally as well. Python 3.9 and earlier behaved this way. A regression in 3.10 turned passing it positionally into a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
