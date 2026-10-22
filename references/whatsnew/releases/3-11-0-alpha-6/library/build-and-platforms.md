# Python 3.11.0 alpha 6 / library / build and platforms

[bpo-46323](https://bugs.python.org/issue?@action=redirect&bpo=46323): `ctypes.CFUNCTYPE()` together with `ctypes.WINFUNCTYPE()` now refuse to build the type once its `_argtypes_` member holds too many arguments. Formerly that error surfaced only at function-call time. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
