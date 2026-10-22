# Python 3.6.2 release candidate 1 / library / unittest testcase assertraises explicitly severs reference cycle objects do not survive

[bpo-23890](https://bugs.python.org/issue?@action=redirect&bpo=23890): unittest.TestCase.assertRaises() now explicitly severs a reference cycle so objects do not survive past their expected lifetime.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
