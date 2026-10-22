# Python 3.9.0 alpha 1 / core and builtins / corrected defect stemming how weakrefs cyclic garbage collector interact

[bpo-38006](https://bugs.python.org/issue?@action=redirect&bpo=38006): Corrected a defect stemming from how weakrefs and the cyclic garbage collector interact. Any weakrefs found in garbage must be cleared so their callbacks cannot fire and produce a crash.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
