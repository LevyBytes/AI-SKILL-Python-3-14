# Python 3.11.0 alpha 7 / core and builtins / functions and types

[bpo-47127](https://bugs.python.org/issue?@action=redirect&bpo=47127): Through specialization, calls into c functions carrying keyword arguments run 25% faster. Kumar Aditya supplied the patch.

[bpo-47070](https://bugs.python.org/issue?@action=redirect&bpo=47070): Cut the count of `memcpy` calls to speed up `array_inplace_repeat`. The `repeat` plus inplace `repeat` methods belonging to `array`, `bytes`, `bytearray` and `unicodeobject` were reworked so they share the common `_PyBytes_Repeat`.

[bpo-46329](https://bugs.python.org/issue?@action=redirect&bpo=46329): The low bit of `LOAD_GLOBAL` now signals whether a `NULL` should be pushed ahead of the global. This trims the call sequence somewhat.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
