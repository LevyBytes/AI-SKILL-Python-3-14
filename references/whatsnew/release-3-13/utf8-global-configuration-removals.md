# Python 3.13 changes: UTF-8 mode and remaining global configuration replacements

`Py_UTF8Mode`: switch to [`PyPreConfig.utf8_mode`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.utf8_mode) or [`PyConfig_Get("utf8_mode")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get). (refer to [`Py_PreInitialize()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_PreInitialize))

To apply these settings, pair the [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) API with [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig). At runtime, their values can instead be read through [`PyConfig_Get()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get).

[Subject index](INDEX.md) · [Previous source section](initialization-configuration-api-removals.md) · [Next source section](c-api-removals-scheduled-for-3-16.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-changes-deprecated-c-apis.md) · [Release/subject declaration](c-api-removals-scheduled-for-3-15.md)
