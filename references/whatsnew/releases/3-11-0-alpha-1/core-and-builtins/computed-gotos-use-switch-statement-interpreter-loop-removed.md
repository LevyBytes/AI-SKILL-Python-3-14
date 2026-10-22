# Python 3.11.0 alpha 1 / core and builtins / computed gotos use switch statement interpreter loop removed

[bpo-44878](https://bugs.python.org/issue?@action=redirect&bpo=44878): When computed gotos are in use, the switch statement for the interpreter loop was removed. This guarantees a single dispatch table inside the interpreter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
