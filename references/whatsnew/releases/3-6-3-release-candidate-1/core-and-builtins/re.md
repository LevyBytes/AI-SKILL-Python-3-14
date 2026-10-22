# Python 3.6.3 release candidate 1 / core and builtins / re

[bpo-30876](https://bugs.python.org/issue?@action=redirect&bpo=30876): A relative import from a package that is not loaded now re-imports that package instead of erroring with SystemError. A relative import from a non-package now errors with ImportError rather than SystemError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
