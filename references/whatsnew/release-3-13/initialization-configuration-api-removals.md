# Python 3.13 changes: Initialization configuration replacement APIs

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

  - [`Py_LegacyWindowsFSEncodingFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_LegacyWindowsFSEncodingFlag): switch to [`PyPreConfig.legacy_windows_fs_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding) or [`PyConfig_Get("legacy_windows_fs_encoding")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_LegacyWindowsStdioFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_LegacyWindowsStdioFlag): switch to [`PyConfig.legacy_windows_stdio`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.legacy_windows_stdio) or [`PyConfig_Get("legacy_windows_stdio")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - `Py_FileSystemDefaultEncoding`, `Py_HasFileSystemDefaultEncoding`: switch to [`PyConfig.filesystem_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_encoding) or [`PyConfig_Get("filesystem_encoding")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - `Py_FileSystemDefaultEncodeErrors`: switch to [`PyConfig.filesystem_errors`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_errors) or [`PyConfig_Get("filesystem_errors")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  -

[Subject index](INDEX.md) · [Previous source section](c-api-removals-scheduled-for-3-15.md) · [Next source section](utf8-global-configuration-removals.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-changes-deprecated-c-apis.md) · [Release/subject declaration](c-api-removals-scheduled-for-3-15.md)
