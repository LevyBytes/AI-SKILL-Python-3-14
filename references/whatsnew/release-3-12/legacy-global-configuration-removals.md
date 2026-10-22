# What’s New In Python 3.12 / C API Changes / Deprecated / Pending removal in Python 3.15

- [`Py_LegacyWindowsFSEncodingFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_LegacyWindowsFSEncodingFlag): switch to [`PyPreConfig.legacy_windows_fs_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding) or [`PyConfig_Get("legacy_windows_fs_encoding")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - [`Py_LegacyWindowsStdioFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_LegacyWindowsStdioFlag): switch to [`PyConfig.legacy_windows_stdio`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.legacy_windows_stdio) or [`PyConfig_Get("legacy_windows_stdio")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - `Py_FileSystemDefaultEncoding`, `Py_HasFileSystemDefaultEncoding`: switch to [`PyConfig.filesystem_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_encoding) or [`PyConfig_Get("filesystem_encoding")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - `Py_FileSystemDefaultEncodeErrors`: switch to [`PyConfig.filesystem_errors`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_errors) or [`PyConfig_Get("filesystem_errors")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

  - `Py_UTF8Mode`: switch to [`PyPreConfig.utf8_mode`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.utf8_mode) or [`PyConfig_Get("utf8_mode")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get). (refer to [`Py_PreInitialize()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_PreInitialize))

To apply these settings, pair the [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) API with [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig). At runtime, their values can instead be read through [`PyConfig_Get()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

[Subject index](INDEX.md) · [Previous source section](c-api-changes-deprecated-pending-removal-in-python-3-15.md) · [Next source section](c-api-changes-deprecated-pending-removal-in-python-3-16.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-changes-deprecated-deprecated.md) · [Release/subject declaration](c-api-changes-deprecated-pending-removal-in-python-3-15.md) · [Preceding release/subject continuation](c-api-changes-deprecated-pending-removal-in-python-3-15.md)
