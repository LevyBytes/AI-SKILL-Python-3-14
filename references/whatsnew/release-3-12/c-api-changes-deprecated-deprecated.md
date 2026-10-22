# Python 3.12 changes: Dictionary version tags and global configuration deprecations

### Deprecated

- Following [**PEP 699**](https://peps.python.org/pep-0699/), extension modules now see the `ma_version_tag` field on [`PyDictObject`](https://docs.python.org/3.14/c-api/dict.html#c.PyDictObject) marked as deprecated. Touching that field triggers a compiler warning while compiling. Python 3.14 will drop the field entirely. (Contributed by Ramvikrams and Kumar Aditya in [gh-101193](https://github.com/python/cpython/issues/101193). PEP by Ken Jin.)

- Deprecate global configuration variable:

  - [`Py_DebugFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_DebugFlag): use [`PyConfig.parser_debug`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.parser_debug)

  - [`Py_VerboseFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_VerboseFlag): use [`PyConfig.verbose`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.verbose)

  - [`Py_QuietFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_QuietFlag): use [`PyConfig.quiet`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.quiet)

  - [`Py_InteractiveFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InteractiveFlag): use [`PyConfig.interactive`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.interactive)

  - [`Py_InspectFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InspectFlag): use [`PyConfig.inspect`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.inspect)

  - [`Py_OptimizeFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_OptimizeFlag): use [`PyConfig.optimization_level`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.optimization_level)

  - [`Py_NoSiteFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_NoSiteFlag): use [`PyConfig.site_import`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.site_import)

  - [`Py_BytesWarningFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_BytesWarningFlag): use [`PyConfig.bytes_warning`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.bytes_warning)

  - [`Py_FrozenFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_FrozenFlag): use [`PyConfig.pathconfig_warnings`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.pathconfig_warnings)

  - [`Py_IgnoreEnvironmentFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_IgnoreEnvironmentFlag): use [`PyConfig.use_environment`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.use_environment)

  - [`Py_DontWriteBytecodeFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_DontWriteBytecodeFlag): use [`PyConfig.write_bytecode`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.write_bytecode)

  - [`Py_NoUserSiteDirectory`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_NoUserSiteDirectory): use [`PyConfig.user_site_directory`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.user_site_directory)

  - [`Py_UnbufferedStdioFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_UnbufferedStdioFlag): use [`PyConfig.buffered_stdio`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.buffered_stdio)

  - [`Py_HashRandomizationFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_HashRandomizationFlag): use [`PyConfig.use_hash_seed`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.use_hash_seed) and [`PyConfig.hash_seed`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.hash_seed)

  - [`Py_IsolatedFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_IsolatedFlag): use [`PyConfig.isolated`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.isolated)

  - [`Py_LegacyWindowsFSEncodingFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_LegacyWindowsFSEncodingFlag): use [`PyPreConfig.legacy_windows_fs_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding)

  - [`Py_LegacyWindowsStdioFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_LegacyWindowsStdioFlag): use [`PyConfig.legacy_windows_stdio`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.legacy_windows_stdio)

  - `Py_FileSystemDefaultEncoding`: use [`PyConfig.filesystem_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_encoding)

  -

[Subject index](INDEX.md) · [Previous source section](c-api-changes-porting-to-python-3-12.md) · [Next source section](filesystem-encoding-c-api-deprecations.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md)
