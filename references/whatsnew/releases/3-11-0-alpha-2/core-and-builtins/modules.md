# Python 3.11.0 alpha 2 / core and builtins / modules

[bpo-21736](https://bugs.python.org/issue?@action=redirect&bpo=21736): Frozen stdlib modules now carry `__file__` pointing at the .py file they would otherwise load from, where feasible. With packages, `__path__` now holds the right entry rather than an empty list, letting unfrozen submodules be imported. These get set only when the stdlib directory is known at runtime initialization. Keep in mind that the file referenced by `__file__` may not actually exist. Nothing here affects non-stdlib frozen modules, nor — for the time being — frozen modules brought in through `PyImport_ImportFrozenModule()`. Furthermore, `co_filename` is presently left unchanged for the module.

[bpo-45020](https://bugs.python.org/issue?@action=redirect&bpo=45020): With frozen stdlib modules, store the original module name under `module.__spec__.loader_state.origname`. Should that value differ from `module.__spec__.name`, the module was registered as an alias inside Tools/scripts/freeze_modules.py. When it is `None`, the module originates from a source file living outside the stdlib.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
