# PYTHON_FROZEN_MODULES

PYTHON_FROZEN_MODULES

Assigning this variable a value of `on` or `off` controls how the import system treats frozen modules. When `on`, those modules are loaded; when `off`, the import machinery skips past them. Standard (non-debug) builds default to `on`, while debug builds default to `off`. Be aware that the `importlib_bootstrap` and `importlib_bootstrap_external` frozen modules remain in use regardless — even when this flag carries the `off` value.

The equivalent `-X frozen_modules` command-line option is also available.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous source section](python-cpu-count.md) · [Following source section](python-colors.md)
