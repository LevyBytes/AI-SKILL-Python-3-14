# Python 3.10.0 alpha 4 / tests / tests and documentation

[bpo-42794](https://bugs.python.org/issue?@action=redirect&bpo=42794): Switched test_nntplib to test against the official group name of news.aioe.org. Donghee Na authored the patch.

[bpo-42641](https://bugs.python.org/issue?@action=redirect&bpo=42641): Improved `test_select.test_select()`: it now finishes in 500 milliseconds instead of 10 seconds. Driving it with Python rather than a shell makes the test more portable.

[bpo-31904](https://bugs.python.org/issue?@action=redirect&bpo=31904): Skip a few tests inside _test_all_chown_common() under VxWorks.

[bpo-31904](https://bugs.python.org/issue?@action=redirect&bpo=31904): Turn off os.popen plus the tests it affects under VxWorks

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
