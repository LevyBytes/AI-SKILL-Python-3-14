# API Functions

int PyArg_ParseTupleAndKeywords([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *kw, const char *format, char *const *keywords, ...)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Reads the arguments of a function that accepts positional as well as keyword parameters, depositing them into local variables. You supply *keywords* as a `NULL`-terminated array of keyword parameter names, each a null-terminated C string in ASCII or UTF-8 encoding. A name left empty stands for a [positional-only parameters](https://docs.python.org/3.14/glossary.html#positional-only-parameter). A success yields true; a failure instead yields false and raises whatever exception fits.

Note

In C the *keywords* parameter is declared char *const*, while in C++ it is const char *const*. The `PY_CXX_CONST` macro lets you override that.

Changed in version 3.6: Gained support for [positional-only parameters](https://docs.python.org/3.14/glossary.html#positional-only-parameter).

Changed in version 3.13: The *keywords* parameter now carries the type char *const* under C and const char *const* under C++, no longer char**. Keyword parameter names outside ASCII became supported as well.

 int PyArg_VaParseTupleAndKeywords([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *kw, const char *format, char *const *keywords, va_list vargs)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Works exactly like `PyArg_ParseTupleAndKeywords()`, save for taking a va_list instead of a variadic argument list.

 int PyArg_ValidateKeywordArguments([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Confirms that every key in the keywords argument dictionary is a string. You only need this when `PyArg_ParseTupleAndKeywords()` isn't in play, given that that function performs the check itself.

Added in version 3.2.

 int PyArg_Parse([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args, const char *format, ...)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Reads the lone argument of a function that accepts a single positional parameter, placing it into a local variable. A success yields true; a failure instead yields false and raises whatever exception fits.

Example:

```c
// Function using METH_O calling convention
static PyObject*
my_function(PyObject *module, PyObject *arg)
{
    int value;
    if (!PyArg_Parse(arg, "i:my_function", &value)) {
        return NULL;
    }
    // ... use value ...
}

```

 int PyArg_UnpackTuple([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args, const char *name, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) min, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) max, ...)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A more straightforward way to pull arguments that skips any format string for declaring argument types. A function relying on this approach to obtain its arguments ought to be marked [`METH_VARARGS`](https://docs.python.org/3.14/c-api/structures.html#c.METH_VARARGS) within its function or method tables. Hand the tuple holding the real arguments in as *args*; it genuinely has to be a tuple. That tuple's length has to fall within *min* through *max* inclusive, and *min* and *max* are permitted to coincide. You must also pass further arguments to the function, each a pointer to a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* variable; the call populates them from *args* with [borrowed references](https://docs.python.org/3.14/glossary.html#term-borrowed-reference). Variables matching optional parameters that *args* omits stay untouched, so the caller should initialize them beforehand. The function returns true on success, and false should *args* not be a tuple or carry the wrong element count; a failure also sets an exception.

The following shows this function in use, drawn from the sources of the `_weakref` helper module that handles weak references:

```c
static PyObject *
weakref_ref(PyObject *self, PyObject *args)
{
    PyObject *object;
    PyObject *callback = NULL;
    PyObject *result = NULL;

    if (PyArg_UnpackTuple(args, "ref", 1, 2, &object, &callback)) {
        result = PyWeakref_NewRef(object, callback);
    }
    return result;
}

```

In this example, that `PyArg_UnpackTuple()` call amounts to precisely the same thing as the following `PyArg_ParseTuple()` call:

```c
PyArg_ParseTuple(args, "O|O:ref", &object, &callback)

```

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyarg-parsetuple.md) · [Previous source contract](pyarg-vaparse.md) · [Following source contract](py-cxx-const.md)
