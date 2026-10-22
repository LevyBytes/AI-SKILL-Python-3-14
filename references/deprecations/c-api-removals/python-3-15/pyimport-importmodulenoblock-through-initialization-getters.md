# C API pending removal in 3.15: PyImport_ImportModuleNoBlock(); PyWeakref_GetObject() and PyWeakref_GET_OBJECT(); Py_UNICODE type together with the Py_UNICODE_WIDE macro; PyUnicode_AsDecodedObject(); PyUnicode_AsDecodedUnicode(); PyUnicode_AsEncodedObject(); PyUnicode_AsEncodedUnicode(); Initialization getters

## Pending removal in Python 3.15

### Pending removal in Python 3.15

- The [`PyImport_ImportModuleNoBlock()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModuleNoBlock): reach for [`PyImport_ImportModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModule) in its place.

- [`PyWeakref_GetObject()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetObject) and [`PyWeakref_GET_OBJECT()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GET_OBJECT): reach for [`PyWeakref_GetRef()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetRef) in their place. To obtain `PyWeakref_GetRef()` on Python 3.12 and earlier, lean on the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/).

- The [`Py_UNICODE`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UNICODE) type together with the `Py_UNICODE_WIDE` macro: reach for `wchar_t` in their place.

- `PyUnicode_AsDecodedObject()`: reach for [`PyCodec_Decode()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_Decode) in its place.

- `PyUnicode_AsDecodedUnicode()`: reach for [`PyCodec_Decode()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_Decode) in its place; be aware that certain codecs (say, “base64”) can hand back a type besides [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), for instance [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

- `PyUnicode_AsEncodedObject()`: reach for [`PyCodec_Encode()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_Encode) in its place.

- `PyUnicode_AsEncodedUnicode()`: reach for [`PyCodec_Encode()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_Encode) in its place; be aware that certain codecs (say, “base64”) can hand back a type besides [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), for instance [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

- Python initialization functions, which were deprecated back in Python 3.13:

  - [`Py_GetPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPath): reach for [`PyConfig_Get("module_search_paths")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path)) in its place.

  - [`Py_GetPrefix()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPrefix): reach for [`PyConfig_Get("base_prefix")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.base_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_prefix)) in its place. Use `PyConfig_Get("prefix")` ([`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix)) when [virtual environments](https://docs.python.org/3.14/library/venv.html#venv-def) have to be handled.

  - [`Py_GetExecPrefix()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetExecPrefix): reach for [`PyConfig_Get("base_exec_prefix")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.base_exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_exec_prefix)) in its place. Use `PyConfig_Get("exec_prefix")` ([`sys.exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.exec_prefix)) when [virtual environments](https://docs.python.org/3.14/library/venv.html#venv-def) have to be handled.

  - [`Py_GetProgramFullPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramFullPath): reach for [`PyConfig_Get("executable")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable)) in its place.

  - [`Py_GetProgramName()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramName): reach for [`PyConfig_Get("executable")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable)) in its place.

  - [`Py_GetPythonHome()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPythonHome): reach for [`PyConfig_Get("home")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) or the [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) environment variable in its place.

To obtain [`PyConfig_Get()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) on Python 3.13 and earlier, lean on the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/).

[Subject index](INDEX.md) · [Previous source section](../python-3-14/dict-version-tag-and-immutable-type-base-removals.md) · [Next source section](initialization-configuration-functions.md) · [Previous source section](../../language-library-removals/unscheduled/typing-unittest-url-wsgi-xml-and-cache-removals.md)
