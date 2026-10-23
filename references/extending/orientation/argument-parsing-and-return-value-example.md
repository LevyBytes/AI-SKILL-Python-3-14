# Back to the Example - PyArg_ParseTuple, PyLong_FromLong, Py_RETURN_NONE, Py_INCREF, Py_None

### 1.3. Back to the Example

Returning to our example function, by now you ought to be able to make sense of this statement:

```c
if (!PyArg_ParseTuple(args, "s", &command))
    return NULL;

```

It hands back `NULL` (the error indicator for functions that return object pointers) whenever an error turns up in the argument list, leaning on the exception that [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) set. Otherwise the argument’s string value has been copied into the local variable `command`. Since this is a pointer assignment, you are not meant to alter the string it points at (which is why, in Standard C, the variable `command` really ought to be declared as `const char *command`).

Following that is a call to the Unix function `system()`, to which we pass the string we just obtained from [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple):

```c
sts = system(command);

```

Our `spam.system()` function then has to return the `sts` value as a Python object. The function [`PyLong_FromLong()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromLong) accomplishes this.

```c
return PyLong_FromLong(sts);

```

Here it yields an integer object. (Indeed, in Python even integers live as objects on the heap!)

When you have a C function that returns nothing useful (a function returning void), its matching Python function must return `None`. The idiom you need for that (which the [`Py_RETURN_NONE`](https://docs.python.org/3.14/c-api/none.html#c.Py_RETURN_NONE) macro implements) is:

```c
Py_INCREF(Py_None);
return Py_None;

```

[`Py_None`](https://docs.python.org/3.14/c-api/none.html#c.Py_None) serves as the C name for Python’s special object `None`. Unlike a `NULL` pointer — which signals “error” in most settings, as we have already seen — it is a true Python object.

[Subject index](INDEX.md) · [Previous source section](intermezzo-errors-and-exceptions-and-pylong-fromlong.md) · [Next source section](method-tables-and-initialization-registration.md)
