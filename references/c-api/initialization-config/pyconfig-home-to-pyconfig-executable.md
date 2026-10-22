# Python Path Configuration

### Python Path Configuration

`PyConfig` holds several fields devoted to the path configuration:

- Path configuration inputs:

  - `PyConfig.home`

  - `PyConfig.platlibdir`

  - `PyConfig.pathconfig_warnings`

  - `PyConfig.program_name`

  - `PyConfig.pythonpath_env`

  - the current working directory: used for resolving absolute paths

  - the `PATH` environment variable: used to resolve the program's full path (out of `PyConfig.program_name`)

  - `__PYVENV_LAUNCHER__` environment variable

  - (Windows only) Application paths recorded in the registry beneath “SoftwarePythonPythonCoreX.YPythonPath” within both HKEY_CURRENT_USER and HKEY_LOCAL_MACHINE (here X.Y stands for the Python version).

- Path configuration output fields:

  - `PyConfig.base_exec_prefix`

  - `PyConfig.base_executable`

  - `PyConfig.base_prefix`

  - `PyConfig.exec_prefix`

  - `PyConfig.executable`

  - `PyConfig.module_search_paths_set`, `PyConfig.module_search_paths`

  -

[Subject index](INDEX.md) · [Previous source contract](python-configuration.md) · [Following source contract](pyconfig-prefix-to-pybuilddir-txt.md)
