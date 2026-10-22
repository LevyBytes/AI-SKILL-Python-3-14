# Python 3.13.0 alpha 1 / tests / files and paths

[gh-109748](https://github.com/python/cpython/issues/109748): Repaired `test_zippath_from_non_installed_posix()` belonging to test_venv by not copying `__pycache__/` sub-directories, given that concurrently running Python tests can alter them. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
