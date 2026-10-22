# Python 3.8.0 alpha 1 / core and builtins / functions

[bpo-32236](https://bugs.python.org/issue?@action=redirect&bpo=32236): Emit a warning that line buffering has no support whenever [`open()`](https://docs.python.org/3.14/library/functions.html#open) is invoked using binary mode together with `buffering=1`.

[bpo-35560](https://bugs.python.org/issue?@action=redirect&bpo=35560): Repair an assertion error within [`format()`](https://docs.python.org/3.14/library/functions.html#format) on a debug build for floating-point formatting using the "n" format together with zero padding and a small width. The release build stays unaffected. Patch by Karthikeyan Singaravelan.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
