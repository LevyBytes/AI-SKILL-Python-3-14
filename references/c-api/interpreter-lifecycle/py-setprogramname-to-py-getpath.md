# interpreter lifecycle C API: `Py_SetProgramName()`

### Process-wide parameters

 void Py_SetProgramName(const wchar_t *name)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This API remains available for backward compatibility: assigning [`PyConfig.program_name`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.program_name) is the preferred approach now, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

If you call this function at all, do so before the first call to `Py_Initialize()`. It hands the interpreter the value of the `argv[0]` argument passed to the program's `main()` function (converted to wide characters). Both `Py_GetPath()` and a handful of the other functions below use this to locate the Python run-time libraries relative to where the interpreter executable lives. By default the value is `'python'`. The argument must reference a zero-terminated wide character string held in static storage whose contents stay constant for as long as the program runs. The Python interpreter contains no code that alters the contents of this storage.

Apply [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale) to decode a bytes string into a wchar_t* string.

Deprecated since version 3.11, will be removed in version 3.15.

 wchar_t *Py_GetProgramName()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the program name assigned through [`PyConfig.program_name`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.program_name), or otherwise the default. The string that comes back refers to static storage; callers must not alter its value.

Avoid calling this function ahead of `Py_Initialize()`, or it returns `NULL`.

Changed in version 3.10: It now returns `NULL` if called before `Py_Initialize()`.

Deprecated since version 3.13, will be removed in version 3.15: As a replacement, reach for [`PyConfig_Get("executable")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable)).

 wchar_t *Py_GetPrefix()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the *prefix* used for installed platform-independent files. A set of intricate rules derives this from the program name assigned via [`PyConfig.program_name`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.program_name) along with certain environment variables; as an example, when the program name is `'/usr/local/bin/python'`, the prefix works out to `'/usr/local'`. The returned string refers to static storage; callers must not alter its value. This maps to the **prefix** variable found in the top-level `Makefile` and the [`--prefix`](https://docs.python.org/3.14/using/configure.html#cmdoption-prefix) argument given to the **configure** script when building. Python code can read the value as `sys.base_prefix`. Its usefulness is limited to Unix. The function that follows is also relevant.

Avoid calling this function ahead of `Py_Initialize()`, or it returns `NULL`.

Changed in version 3.10: It now returns `NULL` if called before `Py_Initialize()`.

Deprecated since version 3.13, will be removed in version 3.15: As a replacement, reach for [`PyConfig_Get("base_prefix")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.base_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_prefix)). Turn to `PyConfig_Get("prefix")` ([`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix)) whenever [virtual environments](https://docs.python.org/3.14/library/venv.html#venv-def) must be accommodated.

 wchar_t *Py_GetExecPrefix()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the *exec-prefix* used for installed platform-*dependent* files. A set of intricate rules derives this from the program name assigned via [`PyConfig.program_name`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.program_name) along with certain environment variables; as an example, when the program name is `'/usr/local/bin/python'`, the exec-prefix works out to `'/usr/local'`. The returned string refers to static storage; callers must not alter its value. This maps to the **exec_prefix** variable found in the top-level `Makefile` and the `--exec-prefix` argument given to the **configure** script when building. Python code can read the value as `sys.base_exec_prefix`. Its usefulness is limited to Unix.

Background: The exec-prefix is distinct from the prefix in cases where platform dependent files (executables and shared libraries, say) get installed into a separate directory tree. Under a typical installation, the platform dependent files might land in the `/usr/local/plat` subtree while the platform independent ones land in `/usr/local`.

Broadly, a platform amounts to a pairing of hardware and software families; for instance, Sparc machines running the Solaris 2.x operating system count as one platform, whereas Intel machines running Solaris 2.x form another, and Intel machines running Linux make up still another. Distinct major revisions of one operating system typically count as separate platforms too. Non-Unix operating systems present a different case; their installation conventions differ so widely that prefix and exec-prefix carry no meaning and are set to the empty string. Keep in mind that compiled Python bytecode files are platform independent (though they are not independent of the Python version that compiled them!).

System administrators will understand how to set up the **mount** or **automount** programs so that `/usr/local` is shared among platforms while `/usr/local/plat` stays a separate filesystem per platform.

Avoid calling this function ahead of `Py_Initialize()`, or it returns `NULL`.

Changed in version 3.10: It now returns `NULL` if called before `Py_Initialize()`.

Deprecated since version 3.13, will be removed in version 3.15: As a replacement, reach for [`PyConfig_Get("base_exec_prefix")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.base_exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_exec_prefix)). Turn to `PyConfig_Get("exec_prefix")` ([`sys.exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.exec_prefix)) whenever [virtual environments](https://docs.python.org/3.14/library/venv.html#venv-def) must be accommodated.

 wchar_t *Py_GetProgramFullPath()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the full program name of the Python executable; this gets computed as a by-product of working out the default module search path from the program name (assigned by [`PyConfig.program_name`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.program_name)). The returned string refers to static storage; callers must not alter its value. Python code can read the value as `sys.executable`.

Avoid calling this function ahead of `Py_Initialize()`, or it returns `NULL`.

Changed in version 3.10: It now returns `NULL` if called before `Py_Initialize()`.

Deprecated since version 3.13, will be removed in version 3.15: As a replacement, reach for [`PyConfig_Get("executable")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable)).

 wchar_t *Py_GetPath()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the default module search path; this gets computed from the program name (assigned by [`PyConfig.program_name`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.program_name)) plus certain environment variables. The returned string holds a sequence of directory names that a platform dependent delimiter character separates. That delimiter is `':'` under Unix and macOS, and `';'` under Windows. The returned string refers to static storage; callers must not alter its value. On interpreter startup the list [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) starts out with this value; it can be (and normally is) adjusted afterward to alter the search path that modules load from.

Avoid calling this function ahead of `Py_Initialize()`, or it returns `NULL`.

Changed in version 3.10: It now returns `NULL` if called before `Py_Initialize()`.

Deprecated since version 3.13, will be removed in version 3.15: As a replacement, reach for [`PyConfig_Get("module_search_paths")`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) ([`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path)).

[Subject index](INDEX.md) · [Previous source contract](cautions-regarding-runtime-finalization.md) · [Following source contract](py-getversion-to-py-getbuildinfo.md)
