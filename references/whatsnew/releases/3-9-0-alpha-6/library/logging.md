# Python 3.9.0 alpha 6 / library / logging

[bpo-40275](https://bugs.python.org/issue?@action=redirect&bpo=40275): The [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) package is at this point pulled into [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) lazily, solely once the [`assertLogs()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertLogs) assertion gets exercised.

[bpo-40091](https://bugs.python.org/issue?@action=redirect&bpo=40091): Repair a fork-time hang within the logging module: the fresh private _at_fork_reinit() method is at this point used to re-set up locks at fork inside the child process.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
