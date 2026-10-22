# interpreter lifecycle C API: `Py_GetVersion()`, `Py_GetPlatform()`, `Py_GetCopyright()`, `Py_GetCompiler()`, `Py_GetBuildInfo()`

const char *Py_GetVersion()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the version of this Python interpreter. The result is a string resembling something along the lines of

```c
"3.0a5+ (py3k:63103M, May 12 2008, 00:53:55) \n[GCC 4.2.3]"

```

That first word (everything up to the first space character) is the running Python version; its leading characters give the major and minor version split by a period. The returned string refers to static storage; callers must not alter its value. Python code can read the value as [`sys.version`](https://docs.python.org/3.14/library/sys.html#sys.version).

The [`Py_Version`](https://docs.python.org/3.14/c-api/apiabiversion.html#c.Py_Version) constant is also worth noting.

 const char *Py_GetPlatform()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the platform identifier matching the current platform. On Unix this comes from the "official" operating system name lowercased and followed by the major revision number; for example, with Solaris 2.x, which also goes by SunOS 5.x, the value reads `'sunos5'`. On macOS it reads `'darwin'`. On Windows it reads `'win'`. The returned string refers to static storage; callers must not alter its value. Python code can read the value as `sys.platform`.

 const char *Py_GetCopyright()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the official copyright string belonging to the current Python version, such as

`'Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam'`

The returned string refers to static storage; callers must not alter its value. Python code can read the value as `sys.copyright`.

 const char *Py_GetCompiler()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back a note of the compiler that built the current Python version, enclosed in square brackets, for instance:

```c
"[GCC 2.7.2.2]"

```

The returned string refers to static storage; callers must not alter its value. Python code can read the value as part of the variable `sys.version`.

 const char *Py_GetBuildInfo()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back details about the sequence number plus the build date and time of the running Python interpreter instance, such as

```c
"#67, Aug  1 1997, 22:34:28"

```

The returned string refers to static storage; callers must not alter its value. Python code can read the value as part of the variable `sys.version`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-setprogramname-to-py-getpath.md) · [Following source contract](pysys-setargvex-to-py-getpythonhome.md)
