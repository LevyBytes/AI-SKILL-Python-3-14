# Python 3.10.0 beta 1 / tests / threading

[bpo-43843](https://bugs.python.org/issue?@action=redirect&bpo=43843): `test.libregrtest` will now flag a test as ENV_CHANGED (meaning it altered the execution environment) whenever a thread raises an exception that goes uncaught. It installs a hook on [`threading.excepthook()`](https://docs.python.org/3.14/library/threading.html#threading.excepthook). Pass the `--fail-env-changed` option to turn such a test into a failure. Victor Stinner provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
