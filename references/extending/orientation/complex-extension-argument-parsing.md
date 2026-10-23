# Extracting Parameters in Extension Functions - Py_complex, PyArg_ParseTuple

```c
{
    Py_complex c;
    ok = PyArg_ParseTuple(args, "D:myfunction", &c);
    /* a complex, also providing a function name for errors */
    /* Possible Python call: myfunction(1+2j) */
}

```

[Subject index](INDEX.md) · [Previous source section](extension-argument-parsing-and-buffer-sizes.md) · [Next source section](keyword-arguments-and-module-registration.md) · [Owning section and setup](extension-argument-parsing-and-buffer-sizes.md)
