# Python 3.10.0 beta 1 / tests / os

[bpo-43961](https://bugs.python.org/issue?@action=redirect&bpo=43961): On Windows, repaired test_logging.test_namer_rotator_inheritance() by switching to [`os.replace()`](https://docs.python.org/3.14/library/os.html#os.replace) in place of [`os.rename()`](https://docs.python.org/3.14/library/os.html#os.rename). Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
