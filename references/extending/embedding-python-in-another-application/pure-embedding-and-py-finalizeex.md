# Pure Embedding - PyObject, Py_Initialize, PyUnicode_DecodeFSDefault, PyImport_Import, Py_DECREF, PyObject_GetAttrString, PyCallable_Check, PyTuple_New, PyLong_FromLong, PyTuple_SetItem, PyObject_CallObject, PyLong_AsLong, PyErr_Print, PyErr_Occurred, Py_XDECREF, Py_FinalizeEx

### 1.3. Pure Embedding

This opening program sets out to run a function held in a Python script. As with the section on the very high level interface, the Python interpreter does not deal with the application directly (though the following section will alter that).

Here is the code that runs a function defined inside a Python script:

The complete program is in the [upstream source](https://docs.python.org/3.14/extending/embedding.html#pure-embedding).

By way of `argv[1]` this code reads in a Python script, then calls whatever function `argv[2]` names. The remaining entries of the `argv` array become its integer arguments. Supposing you compile and link the program (we'll dub the resulting executable **call**) and run it against a Python script like the one below:

[Subject index](INDEX.md) · [Previous source section](beyond-very-high-level-embedding-an-overview.md) · [Next source section](pure-embedding-and-pyobject-callobject.md)
