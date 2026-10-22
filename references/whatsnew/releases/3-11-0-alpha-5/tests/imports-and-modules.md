# Python 3.11.0 alpha 5 / tests / imports and modules

[bpo-13886](https://bugs.python.org/issue?@action=redirect&bpo=13886): Bypass the test_builtin PTY tests on non-ASCII characters whenever the readline module is loaded. Because the readline module alters input() behavior, and test_builtin is not meant to exercise the readline module. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
