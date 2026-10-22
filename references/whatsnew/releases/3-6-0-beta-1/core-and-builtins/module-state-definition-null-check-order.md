# Python 3.6.0 beta 1 / core and builtins / corrects another pvs studio finding null pointer check came after using

[bpo-27587](https://bugs.python.org/issue?@action=redirect&bpo=27587): Corrects another PVS-Studio finding: a null-pointer check that came after using ‘def’ in _PyState_AddModule(). Christian Heimes provided the initial patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
