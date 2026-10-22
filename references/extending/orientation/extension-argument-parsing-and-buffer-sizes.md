# Extracting Parameters in Extension Functions — PyArg_ParseTuple, PyObject, Py_ssize_t

### 1.7. Extracting Parameters in Extension Functions

The [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) function carries the following declaration:

```c
int PyArg_ParseTuple(PyObject *arg, const char *format, ...);

```

The *arg* argument has to be a tuple object holding an argument list handed from Python to a C function. The *format* argument has to be a format string, with syntax detailed under [Parsing arguments and building values](https://docs.python.org/3.14/c-api/arg.html#arg-parsing) within the Python/C API Reference Manual. Every remaining argument has to be the address of a variable whose type the format string dictates.

Keep in mind that although [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) verifies the Python arguments carry the necessary types, it has no way to validate the addresses of the C variables handed to the call: blunder there and your code will likely crash or at the very least scribble over random bits of memory. So tread carefully!

Be aware that any Python object references handed to the caller are *borrowed* references; refrain from decrementing their reference count!

A handful of sample calls:

```c
#define PY_SSIZE_T_CLEAN
#include <Python.h>

```

```c
int ok;
int i, j;
long k, l;
const char *s;
Py_ssize_t size;

ok = PyArg_ParseTuple(args, ""); /* No arguments */
    /* Python call: f() */

```

```c
ok = PyArg_ParseTuple(args, "s", &s); /* A string */
    /* Possible Python call: f('whoops!') */

```

```c
ok = PyArg_ParseTuple(args, "lls", &k, &l, &s); /* Two longs and a string */
    /* Possible Python call: f(1, 2, 'three') */

```

```c
ok = PyArg_ParseTuple(args, "(ii)s#", &i, &j, &s, &size);
    /* A pair of ints and a string, whose size is also returned */
    /* Possible Python call: f((1, 2), 'three') */

```

```c
{
    const char *file;
    const char *mode = "r";
    int bufsize = 0;
    ok = PyArg_ParseTuple(args, "s|si", &file, &mode, &bufsize);
    /* A string, and optionally another string and an integer */
    /* Possible Python calls:
       f('spam')
       f('spam', 'w')
       f('spam', 'wb', 100000) */
}

```

```c
{
    int left, top, right, bottom, h, v;
    ok = PyArg_ParseTuple(args, "((ii)(ii))(ii)",
             &left, &top, &right, &bottom, &h, &v);
    /* A rectangle and a point */
    /* Possible Python call:
       f(((0, 0), (400, 300)), (10, 10)) */
}

```

[Subject index](INDEX.md) · [Previous source section](c-callback-keyword-arguments-and-reference-cleanup.md) · [Next source section](complex-extension-argument-parsing.md)
