# Python 3.6.4 release candidate 1 / build / compiler and parser

[bpo-32059](https://bugs.python.org/issue?@action=redirect&bpo=32059): During cross-compilation, `detect_modules()` within `setup.py` now examines the sysroot paths as well.

[bpo-31926](https://bugs.python.org/issue?@action=redirect&bpo=31926): Corrected Argument Clinic, which on occasion triggered compilation errors when a single .c file held more than one function and/or method sharing the same name.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
