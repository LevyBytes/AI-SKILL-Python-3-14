# Python 3.13.0 alpha 1 / core and builtins / permit objects besides code objects serve executable within internal

[gh-100987](https://github.com/python/cpython/issues/100987): Permit objects besides code objects to serve as the "executable" within internal frames. Over the long run, this stands to let tools such as Cython and PySpy cooperate more efficiently. Nearer-term, it lets us carry out certain optimizations with less effort.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
