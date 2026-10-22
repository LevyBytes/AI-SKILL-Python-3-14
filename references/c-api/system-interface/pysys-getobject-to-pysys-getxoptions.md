# system interface C API: `PySys_GetObject()`, `PySys_SetObject()`, `PySys_ResetWarnOptions()`, `PySys_WriteStdout()`, `PySys_WriteStderr()`, `PySys_FormatStdout()`, `PySys_FormatStderr()`, `PySys_GetXOptions()`

### System Functions

The following are helper routines that expose capabilities of the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module to C code. Each one operates on the current interpreter thread’s `sys` module’s dict, which lives inside the internal thread state structure.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySys_GetObject(const char *name)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yield the object *name* out of the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module, or `NULL` when it is absent, and do so without setting an exception.

 int PySys_SetObject(const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *v)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Assign *name* within the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module to *v*, except when *v* is `NULL`, whereupon *name* is removed from the sys module. Yields `0` upon success, `-1` upon error.

 void PySys_ResetWarnOptions()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Restore [`sys.warnoptions`](https://docs.python.org/3.14/library/sys.html#sys.warnoptions) to an empty list. You may invoke this routine ahead of [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize).

Deprecated since version 3.13, will be removed in version 3.15: Empty out [`sys.warnoptions`](https://docs.python.org/3.14/library/sys.html#sys.warnoptions) along with `warnings.filters` as the replacement.

 void PySys_WriteStdout(const char *format, ...)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Emit the output string given by *format* onto [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout). No exceptions get raised, even when truncation takes place (described below).

*format* ought to cap the overall size of the formatted output string at 1000 bytes or fewer – past 1000 bytes the output string gets truncated. Practically, that rules out any unbounded “%s” formats; constrain them with “%.&lt;N&gt;s”, where &lt;N&gt; is a decimal number worked out so that &lt;N&gt; added to the largest possible size of any other formatted text stays at or under 1000 bytes. Be careful as well with “%f”, since it can emit hundreds of digits for extremely large numbers.

Should a problem arise, or [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) be unset, the formatted message goes to the actual (C level) *stdout*.

 void PySys_WriteStderr(const char *format, ...)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Like `PySys_WriteStdout()`, except that it writes to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) or *stderr* in its place.

 void PySys_FormatStdout(const char *format, ...)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A routine akin to PySys_WriteStdout() that formats the message via [`PyUnicode_FromFormatV()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormatV) and refrains from cutting the message down to an arbitrary length.

Added in version 3.2.

 void PySys_FormatStderr(const char *format, ...)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Like `PySys_FormatStdout()`, except that it writes to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) or *stderr* in its place.

Added in version 3.2.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySys_GetXOptions()

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Yield the present dictionary of [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) options, in the same vein as [`sys._xoptions`](https://docs.python.org/3.14/library/sys.html#sys._xoptions). Upon error, `NULL` comes back and an exception is set.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous source contract](py-fopen-to-py-fclose.md) · [Following source contract](pysys-audit-to-pysys-addaudithook.md)
