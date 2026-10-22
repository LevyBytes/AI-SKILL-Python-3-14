# Python 3.13.0 alpha 4 / library / tarfile

[gh-67837](https://github.com/python/cpython/issues/67837): Sidestep data races while directories get created during parallel extraction within [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) plus [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile).

[gh-114959](https://github.com/python/cpython/issues/114959): [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) will no longer swallow errors while attempting to unpack a directory over an existing file.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
