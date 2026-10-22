# exceptions C API: `PyErr_WarnEx()`, `PyErr_WarnExplicitObject()`, `PyErr_WarnExplicit()`

### Issuing warnings

Use these functions to raise warnings out of C code. They parallel similar functions that the Python [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module exports. Ordinarily they write a warning message to *sys.stderr*; even so, the user may have asked for warnings to be converted into errors, and when that happens they raise an exception instead. There is also the chance that the functions raise an exception due to trouble within the warning machinery itself. The return value is `0` when no exception is raised, or `-1` when one is raised. (You cannot tell whether a warning message was in fact printed, nor what the reason for the exception was; this is by design.) When an exception is raised, the caller should carry out its usual exception handling (for instance, [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) owned references and return an error value).

 int PyErr_WarnEx([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *category, const char *message, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) stack_level)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Raise a warning message. For *category*, supply either a warning category (described below) or `NULL`; as for *message*, pass a UTF-8 encoded string. The value of *stack_level* is a positive integer giving how many stack frames back to look; the warning is emitted from whichever line is executing in that frame. Here a *stack_level* of 1 points to the function invoking `PyErr_WarnEx()`, 2 to the function one level up, and so on.

Every warning category must derive from `PyExc_Warning`; `PyExc_Warning`, in turn, derives from `PyExc_Exception`; when none is given, `PyExc_RuntimeWarning` serves as the default. Each of the standard Python categories is available through a global variable, and you can find their names enumerated at Warning types.

To learn about warning control, consult the documentation for the [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module along with the [`-W`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) option in the command line documentation. No C API exists for warning control.

 int PyErr_WarnExplicitObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *category, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *message, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filename, int lineno, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *registry)

Raise a warning message while controlling every warning attribute explicitly. This is a thin wrapper over the Python function [`warnings.warn_explicit()`](https://docs.python.org/3.14/library/warnings.html#warnings.warn_explicit); refer there for further details. The *module* and *registry* arguments may be left as `NULL` to obtain the default effect described there.

Added in version 3.4.

 int PyErr_WarnExplicit([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *category, const char *message, const char *filename, int lineno, const char *module, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *registry)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Comparable to `PyErr_WarnExplicitObject()`, the difference being that here *message* along with *module* are UTF-8 encoded strings, while the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) is what decodes *filename*.

[Subject index](INDEX.md) · [Previous source contract](pyerr-badinternalcall-to-pyerr-programtext.md)
