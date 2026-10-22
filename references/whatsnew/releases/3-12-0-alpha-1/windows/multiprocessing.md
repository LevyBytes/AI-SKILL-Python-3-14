# Python 3.12.0 alpha 1 / windows / multiprocessing

[gh-98360](https://github.com/python/cpython/issues/98360): Corrects how [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) launches child processes on Windows out of a virtual environment, so that any of those children that in turn lean on `multiprocessing` to start more processes will correctly see themselves as being inside a virtual environment.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
