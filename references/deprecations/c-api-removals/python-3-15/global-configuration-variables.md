# C API pending removal in 3.15: Global configuration variables

- Global configuration variables:

  - [`Py_DebugFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_DebugFlag): reach for [`PyConfig.parser_debug`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.parser_debug) or [`PyConfig_Get("parser_debug")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_VerboseFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_VerboseFlag): reach for [`PyConfig.verbose`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.verbose) or [`PyConfig_Get("verbose")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_QuietFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_QuietFlag): reach for [`PyConfig.quiet`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.quiet) or [`PyConfig_Get("quiet")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_InteractiveFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InteractiveFlag): reach for [`PyConfig.interactive`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.interactive) or [`PyConfig_Get("interactive")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_InspectFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InspectFlag): reach for [`PyConfig.inspect`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.inspect) or [`PyConfig_Get("inspect")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_OptimizeFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_OptimizeFlag): reach for [`PyConfig.optimization_level`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.optimization_level) or [`PyConfig_Get("optimization_level")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_NoSiteFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_NoSiteFlag): reach for [`PyConfig.site_import`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.site_import) or [`PyConfig_Get("site_import")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_BytesWarningFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_BytesWarningFlag): reach for [`PyConfig.bytes_warning`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.bytes_warning) or [`PyConfig_Get("bytes_warning")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_FrozenFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_FrozenFlag): reach for [`PyConfig.pathconfig_warnings`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.pathconfig_warnings) or [`PyConfig_Get("pathconfig_warnings")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_IgnoreEnvironmentFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_IgnoreEnvironmentFlag): reach for [`PyConfig.use_environment`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.use_environment) or [`PyConfig_Get("use_environment")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_DontWriteBytecodeFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_DontWriteBytecodeFlag): reach for [`PyConfig.write_bytecode`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.write_bytecode) or [`PyConfig_Get("write_bytecode")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_NoUserSiteDirectory`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_NoUserSiteDirectory): reach for [`PyConfig.user_site_directory`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.user_site_directory) or [`PyConfig_Get("user_site_directory")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_UnbufferedStdioFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_UnbufferedStdioFlag): reach for [`PyConfig.buffered_stdio`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.buffered_stdio) or [`PyConfig_Get("buffered_stdio")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_HashRandomizationFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_HashRandomizationFlag): reach for [`PyConfig.use_hash_seed`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.use_hash_seed) and [`PyConfig.hash_seed`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.hash_seed) or [`PyConfig_Get("hash_seed")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_IsolatedFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_IsolatedFlag): reach for [`PyConfig.isolated`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.isolated) or [`PyConfig_Get("isolated")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_LegacyWindowsFSEncodingFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_LegacyWindowsFSEncodingFlag): reach for [`PyPreConfig.legacy_windows_fs_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding) or [`PyConfig_Get("legacy_windows_fs_encoding")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - [`Py_LegacyWindowsStdioFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_LegacyWindowsStdioFlag): reach for [`PyConfig.legacy_windows_stdio`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.legacy_windows_stdio) or [`PyConfig_Get("legacy_windows_stdio")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - `Py_FileSystemDefaultEncoding`, `Py_HasFileSystemDefaultEncoding`: reach for [`PyConfig.filesystem_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_encoding) or [`PyConfig_Get("filesystem_encoding")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in their place.

  - `Py_FileSystemDefaultEncodeErrors`: reach for [`PyConfig.filesystem_errors`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_errors) or [`PyConfig_Get("filesystem_errors")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place.

  - `Py_UTF8Mode`: reach for [`PyPreConfig.utf8_mode`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.utf8_mode) or [`PyConfig_Get("utf8_mode")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) in its place. (see [`Py_PreInitialize()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_PreInitialize))

Pair the [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) API with [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig) to assign these options. Alternatively, fetch them at runtime via [`PyConfig_Get()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

[Subject index](INDEX.md) · [Previous source section](initialization-configuration-functions.md) · [Next source section](../python-3-16/bundled-libmpdec.md) · [Next source section](../python-3-18/private-functions-and-replacement-apis.md)
