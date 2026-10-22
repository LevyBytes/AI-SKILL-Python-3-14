# -X frozen_modules

- `-X frozen_modules` controls whether the import machinery skips frozen modules. A value of `on` means they are imported, while `off` means they are skipped. The default comes out as `on` for an installed Python (the usual situation). When it is under development (running out of the source tree) the default is instead `off`. Bear in mind that the `importlib_bootstrap` and `importlib_bootstrap_external` frozen modules are used in every case, even when this flag is `off`. See also `PYTHON_FROZEN_MODULES`.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous source section](x-no-debug-ranges.md) · [Following source section](x-perf.md)
