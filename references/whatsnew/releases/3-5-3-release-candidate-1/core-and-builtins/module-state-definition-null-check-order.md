# Python 3.5.3 release candidate 1 / core and builtins / repair another defect surfaced pvs studio null pointer check came after

[bpo-27587](https://bugs.python.org/issue?@action=redirect&bpo=27587): Repair another defect surfaced by PVS-Studio: a null-pointer check that came after using "def" inside _PyState_AddModule(). Christian Heimes supplied the initial patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
