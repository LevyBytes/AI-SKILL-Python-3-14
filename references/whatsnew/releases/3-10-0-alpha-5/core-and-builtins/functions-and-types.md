# Python 3.10.0 alpha 5 / core and builtins / functions and types

[bpo-42927](https://bugs.python.org/issue?@action=redirect&bpo=42927): For `LOAD_ATTR`, the inline cache now speeds up access to attributes declared via `__slots__` too. Reading such an attribute gets up to 30% faster as a result.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
