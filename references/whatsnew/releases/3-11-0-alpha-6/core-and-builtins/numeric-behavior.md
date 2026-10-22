# Python 3.11.0 alpha 6 / core and builtins / numeric behavior

[bpo-46852](https://bugs.python.org/issue?@action=redirect&bpo=46852): Rename the private undocumented `float.__set_format__()` method back to `float.__setformat__()`, correcting a typo that crept in during Python 3.7. Only test_float makes use of the method. Victor Stinner wrote the patch.

[bpo-46852](https://bugs.python.org/issue?@action=redirect&bpo=46852): Drop the undocumented private `float.__set_format__()` method, which Python 3.7 had called `float.__setformat__()`. Its docstring read:

> "You probably don't want to use this function. It exists mainly to be used in Python's test suite."

Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
