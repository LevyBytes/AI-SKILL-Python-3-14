# Python 3.5.4 release candidate 1 / library / unittest testcase assertraises explicitly breaks reference cycle objects not kept alive

[bpo-23890](https://bugs.python.org/issue?@action=redirect&bpo=23890): unittest.TestCase.assertRaises() now explicitly breaks a reference cycle so that objects are not kept alive past what is expected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
