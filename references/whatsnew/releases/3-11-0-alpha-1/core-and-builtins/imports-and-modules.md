# Python 3.11.0 alpha 1 / core and builtins / imports and modules

[bpo-45020](https://bugs.python.org/issue?@action=redirect&bpo=45020): Introduce a fresh command line flag, “-X frozen_modules=[on|off]”, for opting out of (or into) the optional frozen modules. The default is “on” (or “off” when it runs out of the source tree).

[bpo-44486](https://bugs.python.org/issue?@action=redirect&bpo=44486): Modules will now always carry a dictionary, even those created via `types.ModuleType.__new__()`

[bpo-44717](https://bugs.python.org/issue?@action=redirect&bpo=44717): Better AttributeError messaging during circular imports of submodules.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
