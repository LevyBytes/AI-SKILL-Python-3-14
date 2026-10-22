# Python 3.14 changes: Bytecode, environment and global configuration removals

[`Py_IgnoreEnvironmentFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_IgnoreEnvironmentFlag): Prefer [`PyConfig.use_environment`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.use_environment) or [`PyConfig_Get("use_environment")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) as the replacement.

  - [`Py_DontWriteBytecodeFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_DontWriteBytecodeFlag): Prefer [`PyConfig.write_bytecode`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.write_bytecode) or [`PyConfig_Get("write_bytecode")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) as the replacement.

  - [`Py_NoUserSiteDirectory`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_NoUserSiteDirectory): Prefer [`PyConfig.user_site_directory`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.user_site_directory) or [`PyConfig_Get("user_site_directory")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) as the replacement.

  - [`Py_UnbufferedStdioFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_UnbufferedStdioFlag): Prefer [`PyConfig.buffered_stdio`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.buffered_stdio) or [`PyConfig_Get("buffered_stdio")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) as the replacement.

  - [`Py_HashRandomizationFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_HashRandomizationFlag): Prefer [`PyConfig.use_hash_seed`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.use_hash_seed) and [`PyConfig.hash_seed`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.hash_seed) or [`PyConfig_Get("hash_seed")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) as the replacement.

  - [`Py_IsolatedFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_IsolatedFlag): Prefer [`PyConfig.isolated`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.isolated) or [`PyConfig_Get("isolated")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) as the replacement.

  - [`Py_LegacyWindowsFSEncodingFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_LegacyWindowsFSEncodingFlag): Prefer [`PyPreConfig.legacy_windows_fs_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding) or [`PyConfig_Get("legacy_windows_fs_encoding")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) as the replacement.

  - [`Py_LegacyWindowsStdioFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_LegacyWindowsStdioFlag): Prefer [`PyConfig.legacy_windows_stdio`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.legacy_windows_stdio) or [`PyConfig_Get("legacy_windows_stdio")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) as the replacement.

  - `Py_FileSystemDefaultEncoding`, `Py_HasFileSystemDefaultEncoding`: Prefer [`PyConfig.filesystem_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_encoding) or [`PyConfig_Get("filesystem_encoding")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) as the replacement.

  - `Py_FileSystemDefaultEncodeErrors`: Prefer [`PyConfig.filesystem_errors`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_errors) or [`PyConfig_Get("filesystem_errors")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) as the replacement.

  - `Py_UTF8Mode`: Prefer [`PyPreConfig.utf8_mode`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.utf8_mode) or [`PyConfig_Get("utf8_mode")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) as the replacement. (see [`Py_PreInitialize()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_PreInitialize))

To set any of these options, reach for the [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) API together with [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig). At runtime, [`PyConfig_Get()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) is available to read their current values.

[Subject index](INDEX.md) · [Next source section](c-api-removals-scheduled-for-3-16.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-python-configuration-c-api.md) · [Release/subject declaration](c-api-changes-deprecated-c-apis.md) · [Release/subject declaration](c-api-removals-scheduled-for-3-15.md) · [Preceding release/subject continuation](initialization-configuration-api-removals.md)
