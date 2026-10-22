# Python 3.14.0 alpha 1 / tests / functions and types

[gh-121200](https://github.com/python/cpython/issues/121200): Repair `test_expanduser_pwd2()` belonging to `test_posixpath`. Call `getpwnam()` to obtain `pw_dir`, because it may differ from the `pw_dir` returned by `getpwall()`. Patch by Victor Stinner.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
