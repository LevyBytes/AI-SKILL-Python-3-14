# Pure Embedding — PyObject, Py_Initialize, PyUnicode_DecodeFSDefault, PyImport_Import, Py_DECREF, PyObject_GetAttrString, PyCallable_Check, PyTuple_New, PyLong_FromLong, PyTuple_SetItem, PyObject_CallObject, PyLong_AsLong, PyErr_Print, PyErr_Occurred, Py_XDECREF, Py_FinalizeEx

### 1.3. Pure Embedding

This opening program sets out to run a function held in a Python script. As with the section on the very high level interface, the Python interpreter does not deal with the application directly (though the following section will alter that).

Here is the code that runs a function defined inside a Python script:

```c
#define PY_SSIZE_T_CLEAN
#include <Python.h>

int
main(int argc, char *argv[])
{
    PyObject *pName, *pModule, *pFunc;
    PyObject *pArgs, *pValue;
    int i;

    if (argc < 3) {
        fprintf(stderr,"Usage: call pythonfile funcname [args]\n");
        return 1;
    }

    Py_Initialize();
    pName = PyUnicode_DecodeFSDefault(argv[1]);
    /* Error checking of pName left out */

    pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (pModule != NULL) {
        pFunc = PyObject_GetAttrString(pModule, argv[2]);
        /* pFunc is a new reference */

        if (pFunc && PyCallable_Check(pFunc)) {
            pArgs = PyTuple_New(argc - 3);
            for (i = 0; i < argc - 3; ++i) {
                pValue = PyLong_FromLong(atoi(argv[i + 3]));
                if (!pValue) {
                    Py_DECREF(pArgs);
                    Py_DECREF(pModule);
                    fprintf(stderr, "Cannot convert argument\n");
                    return 1;
                }
                /* pValue reference stolen here: */
                PyTuple_SetItem(pArgs, i, pValue);
            }
            pValue = PyObject_CallObject(pFunc, pArgs);
            Py_DECREF(pArgs);
            if (pValue != NULL) {
                printf("Result of call: %ld\n", PyLong_AsLong(pValue));
                Py_DECREF(pValue);
            }
            else {
                Py_DECREF(pFunc);
                Py_DECREF(pModule);
                PyErr_Print();
                fprintf(stderr,"Call failed\n");
                return 1;
            }
        }
        else {
            if (PyErr_Occurred())
                PyErr_Print();
            fprintf(stderr, "Cannot find function \"%s\"\n", argv[2]);
        }
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
    }
    else {
        PyErr_Print();
        fprintf(stderr, "Failed to load \"%s\"\n", argv[1]);
        return 1;
    }
    if (Py_FinalizeEx() < 0) {
        return 120;
    }
    return 0;
}

```

By way of `argv[1]` this code reads in a Python script, then calls whatever function `argv[2]` names. The remaining entries of the `argv` array become its integer arguments. Supposing you compile and link the program (we'll dub the resulting executable **call**) and run it against a Python script like the one below:

[Subject index](INDEX.md) · [Previous source section](beyond-very-high-level-embedding-an-overview.md) · [Next source section](pure-embedding-and-pyobject-callobject.md)
