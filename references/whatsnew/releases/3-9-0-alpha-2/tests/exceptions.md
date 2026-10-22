# Python 3.9.0 alpha 2 / tests / exceptions

[bpo-38692](https://bugs.python.org/issue?@action=redirect&bpo=38692): Bypass the test_posix.test_pidfd_open() test whenever `os.pidfd_open()` fails with a [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError). Such a situation can arise within a Linux sandbox that uses a syscall whitelist not yet permitting the `pidfd_open()` syscall.

[bpo-38669](https://bugs.python.org/issue?@action=redirect&bpo=38669): Raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) whenever target is passed as a string to [`unittest.mock.patch.object()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch.object).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
