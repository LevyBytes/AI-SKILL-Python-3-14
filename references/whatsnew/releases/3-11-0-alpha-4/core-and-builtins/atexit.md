# Python 3.11.0 alpha 4 / core and builtins / atexit

[bpo-46025](https://bugs.python.org/issue?@action=redirect&bpo=46025): Resolve a crash within the [`atexit`](https://docs.python.org/3.14/library/atexit.html#module-atexit) module tied to functions that deregister themselves prior to raising exceptions. Pablo Galindo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
