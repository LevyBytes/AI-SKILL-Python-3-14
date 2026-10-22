# Python 3.12.0 alpha 6 / library / zipfile

[gh-88233](https://github.com/python/cpython/issues/88233): Make `zipfile` keep ?extra? fields intact no matter how they are ordered relative to a zip64 ?extra.?

[gh-101566](https://github.com/python/cpython/issues/101566): Bring zipfile's Path into sync with [zipp 3.14](https://zipp.readthedocs.io/en/latest/history.html#v3-14-0), which includes a fix for extractall on the underlying zipfile once it has been wrapped inside `Path`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
