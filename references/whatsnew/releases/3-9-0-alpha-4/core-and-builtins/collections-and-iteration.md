# Python 3.9.0 alpha 4 / core and builtins / collections and iteration

[bpo-39606](https://bugs.python.org/issue?@action=redirect&bpo=39606): Repair a regression introduced by the fix for [bpo-39386](https://bugs.python.org/issue?@action=redirect&bpo=39386); it had blocked any call to `aclose` on an async generator already closed or already exhausted.

[bpo-39453](https://bugs.python.org/issue?@action=redirect&bpo=39453): Addressed a potential crash in `list.__contains__()` arising when the list mutates while its items are being compared. Donghee Na authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
