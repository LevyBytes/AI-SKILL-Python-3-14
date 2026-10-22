# Python 3.8.0 alpha 1 / core and builtins / restrict forking main interpreter only

[bpo-34651](https://bugs.python.org/issue?@action=redirect&bpo=34651): Restrict forking to the main interpreter only. This rules out the chance of disturbing the main interpreter, something essential to how the runtime operates.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
