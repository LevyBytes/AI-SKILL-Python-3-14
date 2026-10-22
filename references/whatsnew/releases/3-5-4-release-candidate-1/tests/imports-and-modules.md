# Python 3.5.4 release candidate 1 / tests / imports and modules

[bpo-30197](https://bugs.python.org/issue?@action=redirect&bpo=30197): Improve the swap_attr() and swap_item() helpers within the test.support module. They now behave correctly when the replaced attribute or item is deleted inside the with statement. Whatever value the attribute or item previously held (or None when it was absent) now becomes the target of the "as" clause, when one is present.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
