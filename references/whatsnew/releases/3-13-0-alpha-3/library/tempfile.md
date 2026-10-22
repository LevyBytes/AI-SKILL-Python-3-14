# Python 3.13.0 alpha 3 / library / tempfile

[gh-79325](https://github.com/python/cpython/issues/79325): Resolve an endless recursion error during [`tempfile.TemporaryDirectory()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.TemporaryDirectory) cleanup on Windows.

[gh-91133](https://github.com/python/cpython/issues/91133): Fix a defect in [`tempfile.TemporaryDirectory`](https://docs.python.org/3.14/library/tempfile.html#tempfile.TemporaryDirectory) cleanup so it no longer follows symlinks while working around file system permission errors.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
