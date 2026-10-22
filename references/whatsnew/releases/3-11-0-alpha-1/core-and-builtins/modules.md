# Python 3.11.0 alpha 1 / core and builtins / modules

[bpo-44313](https://bugs.python.org/issue?@action=redirect&bpo=44313): Objects and modules brought in directly (via import and from import statements) no longer emit `LOAD_METHOD`/`CALL_METHOD` for objects accessed directly off their namespace. The regular `LOAD_ATTR`/`CALL_FUNCTION` is used instead.

[bpo-44959](https://bugs.python.org/issue?@action=redirect&bpo=44959): Provide a fallback to extension modules carrying the ‘.sl’ suffix under HP-UX

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
