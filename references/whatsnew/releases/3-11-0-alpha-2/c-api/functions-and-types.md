# Python 3.11.0 alpha 2 / c api / functions and types

[bpo-35081](https://bugs.python.org/issue?@action=redirect&bpo=35081): Relocate the `interpreteridobject.h` header out of `Include/` and into `Include/internal/`. The functions it exposes are private only. Victor Stinner contributed the patch.

[bpo-45434](https://bugs.python.org/issue?@action=redirect&bpo=45434): Delete the `pystrhex.h` header. The only things it holds are private functions. A C extension ought to include just the principal `<Python.h>` header. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
