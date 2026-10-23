# More Suggestions - tp_richcompare, PyObject_TypeCheck, PyErr_SetString, PyExc_TypeError

### 3.7. More Suggestions

To find out how a given method ought to be written for your new data type, obtain the [CPython](https://docs.python.org/3.14/glossary.html#term-CPython) source code. Head into the `Objects` directory and grep the C source files for `tp_` followed by the function name you are after (say, `tp_richcompare`). That search turns up examples of the very function you mean to write.

Should you need to confirm that a given object is an actual instance of the type you are building, call the [`PyObject_TypeCheck()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_TypeCheck) function. One example of how it might be used looks roughly like this:

```c
if (!PyObject_TypeCheck(some_object, &MyType)) {
    PyErr_SetString(PyExc_TypeError, "arg #1 not a mything");
    return NULL;
}

```

See also

Grab CPython source releases for download.

[https://www.python.org/downloads/source/](https://www.python.org/downloads/source/)

The GitHub home of the CPython project, where its source code is actively developed.

[https://github.com/python/cpython](https://github.com/python/cpython)

[Subject index](INDEX.md) · [Previous source section](weak-reference-support-and-tp-free.md)
