# Pure Embedding — Py_Initialize, PyUnicode_DecodeFSDefault, PyImport_Import, PyObject_GetAttrString, PyCallable_Check, Py_XDECREF, PyObject_CallObject

```python
def multiply(a,b):
    print("Will compute", a, "times", b)
    c = 0
    for i in range(0, a):
        c = c + b
    return c

```

then what you get back should be:

```shell
$ call multiply multiply 3 2
Will compute 3 times 2
Result of call: 6

```

Even though the program runs long for what little it accomplishes, the greater part of its code goes to converting data between Python and C and to reporting errors. The portion that actually matters for embedding Python begins at

```c
Py_Initialize();
pName = PyUnicode_DecodeFSDefault(argv[1]);
/* Error checking of pName left out */
pModule = PyImport_Import(pName);

```

With the interpreter up and running, [`PyImport_Import()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_Import) brings the script in. That routine expects a Python string for its argument, and the [`PyUnicode_DecodeFSDefault()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_DecodeFSDefault) data conversion routine is what builds it.

```c
pFunc = PyObject_GetAttrString(pModule, argv[2]);
/* pFunc is a new reference */

if (pFunc && PyCallable_Check(pFunc)) {
    ...
}
Py_XDECREF(pFunc);

```

With the script now in memory, [`PyObject_GetAttrString()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetAttrString) fetches the name we are after. Provided the name is present and the returned object can be called, it is fair to treat it as a function. The program then goes on to assemble a tuple of arguments in the usual way. The Python function is finally called by means of:

```c
pValue = PyObject_CallObject(pFunc, pArgs);

```

When the function comes back, `pValue` holds either `NULL` or a reference to the function's return value. Remember to drop the reference once you have looked at the value.

[Subject index](INDEX.md) · [Previous source section](pure-embedding-and-py-finalizeex.md) · [Next source section](extending-embedded-python-and-pyimport-appendinittab.md) · [Owning section and setup](pure-embedding-and-py-finalizeex.md)
