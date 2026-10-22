# What’s New in Python 2.3 / Build and C API Changes

### Build and C API Changes

The following changes were made to Python's build process and to the C API:

- The cycle detection logic the garbage collection relies on has proven stable, so it has now become mandatory. Compiling Python without it is no longer possible, and the `--with-cycle-gc` switch to **configure** has been dropped.

- By passing `--enable-shared` to Python's **configure** script, Python can now optionally be built as a shared library (`libpython2.3.so`). (Contributed by Ondrej Palkovsky.)

- Deprecation now applies to both the `DL_EXPORT` and `DL_IMPORT` macros. When you write an initialization function for a Python extension module, declare it from now on with the new [`PyMODINIT_FUNC`](https://docs.python.org/3.14/c-api/extension-modules.html#c.PyMODINIT_FUNC) macro; the Python core, meanwhile, will typically lean on the `PyAPI_FUNC` and `PyAPI_DATA` macros.

- Supplying `--without-doc-strings` to the **configure** script lets the interpreter be compiled with no docstrings for the built-in functions and modules. Doing so shrinks the Python executable by roughly 10%, but it also means help for Python's built-ins becomes unavailable. (Contributed by Gustavo Niemeyer.)

- The `PyArg_NoArgs()` macro is now deprecated, and any code relying on it should be updated. From Python 2.2 onward, the method definition table can carry the [`METH_NOARGS`](https://docs.python.org/3.14/c-api/structures.html#c.METH_NOARGS) flag to indicate there are no arguments, allowing the argument checking to be dropped. Where compatibility with Python versions before 2.2 matters, the code could fall back to `PyArg_ParseTuple(args, "")`, though that runs slower than using `METH_NOARGS`.

- [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) now accepts new format characters that span unsigned integers of differing widths: `B` maps to unsigned char, `H` to unsigned short int, `I` to unsigned int, and `K` to unsigned long long.

- A new function, `PyObject_DelItemString(mapping, char *key)`, was introduced as a shorthand for `PyObject_DelItem(mapping, PyString_New(key))`.

- File objects now handle their internal string buffer in a new way, growing it exponentially as the need arises. This makes the benchmark tests in `Lib/test/test_bufio.py` run substantially faster (from 57 seconds down to 1.7 seconds, by one measurement).

- Defining class and static methods on a C extension type is now possible: set either the [`METH_CLASS`](https://docs.python.org/3.14/c-api/structures.html#c.METH_CLASS) flag or the [`METH_STATIC`](https://docs.python.org/3.14/c-api/structures.html#c.METH_STATIC) flag within a method's [`PyMethodDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef) structure.

- Python now bundles a copy of the Expat XML parser's source code, eliminating any reliance on a system version or local installation of Expat.

- If your extension dynamically allocates type objects, take note of a change in the rules governing the [`__module__`](https://docs.python.org/3.14/reference/datamodel.html#type.__module__) and [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#type.__name__) attributes. Briefly, you'll want to make sure the type's dictionary holds a `'__module__'` key; treating the module name as the portion of the type name up to the last period will no longer produce the intended result. For more, see the API reference documentation or the source.

[Subject index](INDEX.md) · [Previous source section](pymalloc-a-specialized-object-allocator.md) · [Next source section](port-specific-changes.md) · [Release/subject declaration](standard-set-type.md)
