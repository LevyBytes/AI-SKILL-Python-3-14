# What’s New In Python 3.12 / C API Changes / Deprecated / Pending removal in Python 3.15 — sys, venv

#### Pending removal in Python 3.15

- The [`PyImport_ImportModuleNoBlock()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModuleNoBlock): Use [`PyImport_ImportModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModule) instead.

- [`PyWeakref_GetObject()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetObject) and [`PyWeakref_GET_OBJECT()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GET_OBJECT): Use [`PyWeakref_GetRef()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetRef) instead. To obtain `PyWeakref_GetRef()` under Python 3.12 plus any older release, lean on the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/).

- [`Py_UNICODE`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UNICODE) type and the `Py_UNICODE_WIDE` macro: Use `wchar_t` instead.

- `PyUnicode_AsDecodedObject()`: Use [`PyCodec_Decode()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_Decode) instead.

- `PyUnicode_AsDecodedUnicode()`: Use [`PyCodec_Decode()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_Decode) instead; keep in mind that certain codecs ("base64" being one) can hand back something other than [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) among them.

- `PyUnicode_AsEncodedObject()`: Use [`PyCodec_Encode()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_Encode) instead.

- `PyUnicode_AsEncodedUnicode()`: Use [`PyCodec_Encode()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_Encode) instead; keep in mind that certain codecs ("base64" being one) can hand back something other than [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) among them.

- Python initialization functions, deprecated in Python 3.13:

  - [`Py_GetPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPath): Use [`PyConfig_Get("module_search_paths")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path)) instead.

  - [`Py_GetPrefix()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPrefix): Use [`PyConfig_Get("base_prefix")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.base_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_prefix)) instead. Use `PyConfig_Get("prefix")` ([`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix)) if [virtual environments](https://docs.python.org/3.14/library/venv.html#venv-def) need to be handled.

  - [`Py_GetExecPrefix()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetExecPrefix): Use [`PyConfig_Get("base_exec_prefix")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.base_exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_exec_prefix)) instead. Use `PyConfig_Get("exec_prefix")` ([`sys.exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.exec_prefix)) if [virtual environments](https://docs.python.org/3.14/library/venv.html#venv-def) need to be handled.

  - [`Py_GetProgramFullPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramFullPath): Use [`PyConfig_Get("executable")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable)) instead.

  - [`Py_GetProgramName()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramName): Use [`PyConfig_Get("executable")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable)) instead.

  - [`Py_GetPythonHome()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPythonHome): Use [`PyConfig_Get("home")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) or the [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) environment variable instead.

To pull in [`PyConfig_Get()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) under Python 3.13 plus any older release, lean on the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/).

- Functions to configure Python's initialization, deprecated in Python 3.11:

  - `PySys_SetArgvEx()`: Set [`PyConfig.argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.argv) instead.

  -

`PySys_SetArgv()`: Set [`PyConfig.argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.argv) instead.

  - `Py_SetProgramName()`: Set [`PyConfig.program_name`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.program_name) instead.

  - `Py_SetPythonHome()`: Set [`PyConfig.home`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.home) instead.

  - [`PySys_ResetWarnOptions()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_ResetWarnOptions): clears [`sys.warnoptions`](https://docs.python.org/3.14/library/sys.html#sys.warnoptions) along with `warnings.filters` as the replacement.

Reach instead for the [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) API together with [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig).

- Global configuration variables:

  - [`Py_DebugFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_DebugFlag): switch to [`PyConfig.parser_debug`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.parser_debug) or [`PyConfig_Get("parser_debug")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_VerboseFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_VerboseFlag): switch to [`PyConfig.verbose`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.verbose) or [`PyConfig_Get("verbose")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_QuietFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_QuietFlag): switch to [`PyConfig.quiet`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.quiet) or [`PyConfig_Get("quiet")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_InteractiveFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InteractiveFlag): switch to [`PyConfig.interactive`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.interactive) or [`PyConfig_Get("interactive")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_InspectFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InspectFlag): switch to [`PyConfig.inspect`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.inspect) or [`PyConfig_Get("inspect")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_OptimizeFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_OptimizeFlag): switch to [`PyConfig.optimization_level`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.optimization_level) or [`PyConfig_Get("optimization_level")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_NoSiteFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_NoSiteFlag): switch to [`PyConfig.site_import`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.site_import) or [`PyConfig_Get("site_import")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_BytesWarningFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_BytesWarningFlag): switch to [`PyConfig.bytes_warning`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.bytes_warning) or [`PyConfig_Get("bytes_warning")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_FrozenFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_FrozenFlag): switch to [`PyConfig.pathconfig_warnings`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.pathconfig_warnings) or [`PyConfig_Get("pathconfig_warnings")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_IgnoreEnvironmentFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_IgnoreEnvironmentFlag): switch to [`PyConfig.use_environment`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.use_environment) or [`PyConfig_Get("use_environment")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_DontWriteBytecodeFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_DontWriteBytecodeFlag): switch to [`PyConfig.write_bytecode`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.write_bytecode) or [`PyConfig_Get("write_bytecode")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_NoUserSiteDirectory`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_NoUserSiteDirectory): switch to [`PyConfig.user_site_directory`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.user_site_directory) or [`PyConfig_Get("user_site_directory")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_UnbufferedStdioFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_UnbufferedStdioFlag): switch to [`PyConfig.buffered_stdio`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.buffered_stdio) or [`PyConfig_Get("buffered_stdio")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_HashRandomizationFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_HashRandomizationFlag): switch to [`PyConfig.use_hash_seed`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.use_hash_seed) paired with [`PyConfig.hash_seed`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.hash_seed), or [`PyConfig_Get("hash_seed")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_IsolatedFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_IsolatedFlag): switch to [`PyConfig.isolated`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.isolated) or [`PyConfig_Get("isolated")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

[Subject index](INDEX.md) · [Previous source section](c-api-changes-deprecated-pending-removal-in-python-3-14.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-changes-deprecated-deprecated.md) · [Next source section](legacy-global-configuration-removals.md)
