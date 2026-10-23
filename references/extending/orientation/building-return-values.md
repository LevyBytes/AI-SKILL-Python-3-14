# Building Arbitrary Values - PyArg_ParseTuple, PyObject, Py_BuildValue

### 1.9. Building Arbitrary Values

This function serves as the inverse of [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple). Its declaration reads:

```c
PyObject *Py_BuildValue(const char *format, ...);

```

It understands a collection of format units resembling the ones that [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) understands, except that the arguments (these are inputs to the function rather than outputs) must be plain values instead of pointers. It hands back a new Python object, fit for returning out of a C function that Python called.

One way it diverges from [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple): whereas that function demands a tuple for its first argument (because Python argument lists are always tuples internally), [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue) won't invariably produce a tuple. It produces a tuple solely when its format string holds two or more format units. An empty format string yields `None`; a format string with precisely one format unit yields whichever object that unit describes. Wrap the format string in parentheses to compel it to yield a tuple of size 0 or one.

Examples (the call on the left, the resulting Python value on the right):

```none
Py_BuildValue("")                        None
Py_BuildValue("i", 123)                  123
Py_BuildValue("iii", 123, 456, 789)      (123, 456, 789)
Py_BuildValue("s", "hello")              'hello'
Py_BuildValue("y", "hello")              b'hello'
Py_BuildValue("ss", "hello", "world")    ('hello', 'world')
Py_BuildValue("s#", "hello", 4)          'hell'
Py_BuildValue("y#", "hello", 4)          b'hell'
Py_BuildValue("()")                      ()
Py_BuildValue("(i)", 123)                (123,)
Py_BuildValue("(ii)", 123, 456)          (123, 456)
Py_BuildValue("(i,i)", 123, 456)         (123, 456)
Py_BuildValue("[i,i]", 123, 456)         [123, 456]
Py_BuildValue("{s:i,s:i}",
              "abc", 123, "def", 456)    {'abc': 123, 'def': 456}
Py_BuildValue("((ii)(ii)) (ii)",
              1, 2, 3, 4, 5, 6)          (((1, 2), (3, 4)), (5, 6))

```

[Subject index](INDEX.md) · [Previous source section](keyword-arguments-and-module-registration.md) · [Next source section](reference-counts.md)
