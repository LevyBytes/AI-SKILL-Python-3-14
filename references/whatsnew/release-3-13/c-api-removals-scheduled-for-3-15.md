# What's New In Python 3.13 / C API Changes / Deprecated C APIs / Pending removal in Python 3.15 — sys, venv

#### Pending removal in Python 3.15

- The [`PyImport_ImportModuleNoBlock()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModuleNoBlock): reach for [`PyImport_ImportModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModule) in its place.

- [`PyWeakref_GetObject()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetObject) and [`PyWeakref_GET_OBJECT()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GET_OBJECT): reach for [`PyWeakref_GetRef()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetRef) in their place. To obtain `PyWeakref_GetRef()` on Python 3.12 and earlier, rely on the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/).

- The [`Py_UNICODE`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UNICODE) type plus the `Py_UNICODE_WIDE` macro: reach for `wchar_t` in their place.

- `PyUnicode_AsDecodedObject()`: reach for [`PyCodec_Decode()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_Decode) in its place.

- `PyUnicode_AsDecodedUnicode()`: reach for [`PyCodec_Decode()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_Decode) in its place; be aware that certain codecs (for instance, “base64”) can hand back a type besides [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), such as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

- `PyUnicode_AsEncodedObject()`: reach for [`PyCodec_Encode()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_Encode) in its place.

- `PyUnicode_AsEncodedUnicode()`: reach for [`PyCodec_Encode()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_Encode) in its place; be aware that certain codecs (for instance, “base64”) can hand back a type besides [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), such as [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

- Python initialization functions carrying a deprecation since Python 3.13:

  - [`Py_GetPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPath): reach for [`PyConfig_Get("module_search_paths")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path)) in its place.

  - [`Py_GetPrefix()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPrefix): reach for [`PyConfig_Get("base_prefix")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.base_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_prefix)) in its place. Where [virtual environments](https://docs.python.org/3.14/library/venv.html#venv-def) come into play, instead use `PyConfig_Get("prefix")` ([`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix)).

  - [`Py_GetExecPrefix()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetExecPrefix): reach for [`PyConfig_Get("base_exec_prefix")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.base_exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_exec_prefix)) in its place. Where [virtual environments](https://docs.python.org/3.14/library/venv.html#venv-def) come into play, instead use `PyConfig_Get("exec_prefix")` ([`sys.exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.exec_prefix)).

  - [`Py_GetProgramFullPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramFullPath): reach for [`PyConfig_Get("executable")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable)) in its place.

  - [`Py_GetProgramName()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramName): reach for [`PyConfig_Get("executable")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable)) in its place.

  - [`Py_GetPythonHome()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPythonHome): reach for [`PyConfig_Get("home")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) or fall back to the [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) environment variable.

To obtain [`PyConfig_Get()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) on Python 3.13 and earlier, rely on the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/).

- Functions used to configure Python’s initialization, carrying a deprecation since Python 3.11:

  - `PySys_SetArgvEx()`: Set [`PyConfig.argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.argv) instead.

  - `PySys_SetArgv()`: Set [`PyConfig.argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.argv) instead.

  - `Py_SetProgramName()`: Set [`PyConfig.program_name`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.program_name) instead.

  - `Py_SetPythonHome()`: Set [`PyConfig.home`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.home) instead.

  - [`PySys_ResetWarnOptions()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_ResetWarnOptions): clears [`sys.warnoptions`](https://docs.python.org/3.14/library/sys.html#sys.warnoptions) along with `warnings.filters` as the replacement.

[Subject index](INDEX.md) · [Previous source section](c-api-removals-scheduled-for-3-14.md) · [Next source section](initialization-configuration-api-removals.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-changes-deprecated-c-apis.md)
