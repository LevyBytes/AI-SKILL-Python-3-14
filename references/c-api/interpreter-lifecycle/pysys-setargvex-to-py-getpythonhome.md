# interpreter lifecycle C API: `PySys_SetArgvEx()`, `PySys_SetArgv()`, `Py_SetPythonHome()`

void PySys_SetArgvEx(int argc, wchar_t **argv, int updatepath)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This API remains available for backward compatibility: assigning [`PyConfig.argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.argv), [`PyConfig.parse_argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.parse_argv) and [`PyConfig.safe_path`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.safe_path) is the preferred approach now, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Assign [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) from *argc* and *argv*. These parameters resemble the ones handed to the program's `main()` function, except that the first entry ought to name the script file due to run rather than the executable that hosts the Python interpreter. When no script is going to run, the first entry within *argv* may be an empty string. If this function cannot initialize `sys.argv`, it signals a fatal condition by way of [`Py_FatalError()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_FatalError).

When *updatepath* equals zero, that is everything the function does. When *updatepath* is non-zero, the function additionally adjusts [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) following this algorithm:

- When `argv[0]` carries the name of a script that exists, the absolute path of the directory holding that script gets prepended to [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

- Otherwise (meaning *argc* is `0` or `argv[0]` does not reference an existing file name), an empty string gets prepended to [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path), equivalent to prepending the current working directory (`"."`).

Apply [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale) to decode a bytes string into a wchar_t* string.

The [`PyConfig.orig_argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.orig_argv) and [`PyConfig.argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.argv) members of the [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config) are also relevant.

Note

For applications that embed the Python interpreter to do more than run a single script, passing `0` as *updatepath* is advised, with the application updating [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) on its own when wanted. See [**CVE 2008-5983**](https://www.cve.org/CVERecord?id=CVE-2008-5983).

For versions earlier than 3.1.3, you can reach the same outcome by hand-popping the first [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) element once `PySys_SetArgv()` has been called, for instance with:

```c
PyRun_SimpleString("import sys; sys.path.pop(0)\n");

```

Added in version 3.1.3.

Deprecated since version 3.11, will be removed in version 3.15.

 void PySys_SetArgv(int argc, wchar_t **argv)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This API remains available for backward compatibility: assigning [`PyConfig.argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.argv) and [`PyConfig.parse_argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.parse_argv) is the preferred approach now, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

This function operates like `PySys_SetArgvEx()` with *updatepath* set to `1`, unless the **python** interpreter was launched with the [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I).

Apply [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale) to decode a bytes string into a wchar_t* string.

The [`PyConfig.orig_argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.orig_argv) and [`PyConfig.argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.argv) members of the [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config) are also relevant.

Changed in version 3.4: The *updatepath* value depends on [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I).

Deprecated since version 3.11, will be removed in version 3.15.

 void Py_SetPythonHome(const wchar_t *home)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This API remains available for backward compatibility: assigning [`PyConfig.home`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.home) is the preferred approach now, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Assign the default "home" directory, namely where the standard Python libraries reside. Consult [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) for what the argument string signifies.

The argument must reference a zero-terminated character string held in static storage whose contents stay constant for as long as the program runs. The Python interpreter contains no code that alters the contents of this storage.

Apply [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale) to decode a bytes string into a wchar_t* string.

Deprecated since version 3.11, will be removed in version 3.15.

 wchar_t *Py_GetPythonHome()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the default "home", namely the value assigned through [`PyConfig.home`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.home), or the value held by the [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) environment variable when that is set.

Avoid calling this function ahead of `Py_Initialize()`, or it returns `NULL`.

Changed in version 3.10: It now returns `NULL` if called before `Py_Initialize()`.

Deprecated since version 3.13, will be removed in version 3.15: As a replacement, reach for [`PyConfig_Get("home")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) or alternatively the [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) environment variable.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-setprogramname-to-py-getpath.md) · [Previous source contract](py-getversion-to-py-getbuildinfo.md)
