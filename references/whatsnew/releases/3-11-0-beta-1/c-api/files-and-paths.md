# Python 3.11.0 beta 1 / c api / files and paths

[bpo-35134](https://bugs.python.org/issue?@action=redirect&bpo=35134): Dropped the `Include/code.h` header. The only header that C extensions ought to pull in is the principal `<Python.h>` file. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
