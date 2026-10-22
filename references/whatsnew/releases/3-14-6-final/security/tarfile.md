# Python 3.14.6 final / security / tarfile

[gh-149486](https://github.com/python/cpython/issues/149486): [`tarfile.data_filter()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.data_filter) now checks link targets against the very same normalised value committed to disk, drops trailing separators off the member name as it resolves a symlink’s directory, and turns away link members that would overwrite the destination directory itself. That seals off a number of path-traversal bypasses of the `data` extraction filter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
