# Python 3.10.0 alpha 1 / tests / warnings

[bpo-41003](https://bugs.python.org/issue?@action=redirect&bpo=41003): Repair `test_copyreg` when `numpy` is present: `test.pickletester` now saves and restores the warnings filters around the `numpy` import, so it can ignore the filters that `numpy` installs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
