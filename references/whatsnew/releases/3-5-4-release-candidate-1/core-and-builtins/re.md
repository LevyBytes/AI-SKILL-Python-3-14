# Python 3.5.4 release candidate 1 / core and builtins / re

[bpo-30876](https://bugs.python.org/issue?@action=redirect&bpo=30876): A relative import out of an unloaded package now re-imports that package rather than failing with SystemError. A relative import out of a non-package now fails with ImportError in place of SystemError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
