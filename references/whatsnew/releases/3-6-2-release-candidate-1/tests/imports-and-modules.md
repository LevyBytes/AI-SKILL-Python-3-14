# Python 3.6.2 release candidate 1 / tests / imports and modules

[bpo-30197](https://bugs.python.org/issue?@action=redirect&bpo=30197): Improved the functions swap_attr() and swap_item() within the test.support module. They now function when a replaced attribute or item is deleted inside the with statement. The previous value of the attribute or item (or None when it doesn't exist) is now assigned to the target of the "as" clause, should one be present.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
