# Python 3.14 changes: Initialization APIs and configuration migration

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

  -

[Subject index](INDEX.md) · [Previous source section](c-api-removals-scheduled-for-3-15.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-python-configuration-c-api.md) · [Release/subject declaration](c-api-changes-deprecated-c-apis.md) · [Release/subject declaration](c-api-removals-scheduled-for-3-15.md) · [Following release/subject continuation](bytecode-global-configuration-removals.md)
