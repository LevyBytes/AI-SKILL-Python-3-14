# C API pending removal in 3.15: Initialization configuration functions

- Functions for configuring Python's initialization, which were deprecated back in Python 3.11:

  - `PySys_SetArgvEx()`: Set [`PyConfig.argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.argv) instead.

  - `PySys_SetArgv()`: Set [`PyConfig.argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.argv) instead.

  - `Py_SetProgramName()`: Set [`PyConfig.program_name`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.program_name) instead.

  - `Py_SetPythonHome()`: Set [`PyConfig.home`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.home) instead.

  - [`PySys_ResetWarnOptions()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_ResetWarnOptions): clear [`sys.warnoptions`](https://docs.python.org/3.14/library/sys.html#sys.warnoptions) along with `warnings.filters` in its place.

Pair the [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) API with [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig) in its place.

[Subject index](INDEX.md) · [Previous source section](pyimport-importmodulenoblock-through-initialization-getters.md) · [Next source section](global-configuration-variables.md)
