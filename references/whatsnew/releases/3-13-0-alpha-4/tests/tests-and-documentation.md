# Python 3.13.0 alpha 4 / tests / tests and documentation

[gh-105089](https://github.com/python/cpython/issues/105089): Repair the `test.test_zipfile.test_core.TestWithDirectory.test_create_directory_with_write` test on AIX by applying a bitwise AND of 0xFFFF to mode, keeping it in step with `zinfo.external_attr`

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
