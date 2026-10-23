# Borrowed references and implicit interpreter calls - Py_DECREF, PyObject, PyList_GetItem, PyList_SetItem, PyLong_FromLong, PyObject_Print, tp_dealloc, PyTypeObject, tp_finalize, Py_INCREF, Py_BEGIN_ALLOW_THREADS, Py_END_ALLOW_THREADS

A handful of scenarios exist in which what looks like innocuous use of a borrowed reference turns out to be trouble. Each one traces back to the interpreter being triggered implicitly, which may prompt whoever owns a reference to discard it.

The foremost case worth understanding is calling [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) against some unrelated object at the same moment you hold a borrowed reference to an item in a list. As an example:

```c
void
bug(PyObject *list)
{
    PyObject *item = PyList_GetItem(list, 0);

    PyList_SetItem(list, 1, PyLong_FromLong(0L));
    PyObject_Print(item, stdout, 0); /* BUG! */
}

```

The routine starts by borrowing a reference to `list[0]`, next swaps `list[1]` for the value `0`, and ends by printing that borrowed reference. Seems innocent, doesn't it? It isn't!

Trace execution down into [`PyList_SetItem()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_SetItem). Because the list holds references to every element it contains, swapping out item 1 forces it to release the element that was there before. Imagine that earlier item 1 happened to be an instance of a class you defined, and imagine further that the class carried a `__del__()` method. With that instance sitting at a reference count of 1, releasing it triggers its `__del__()` method. Under the hood, `PyList_SetItem()` runs [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) on the item being replaced, which fires that item's matching [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) function. As deallocation proceeds, `tp_dealloc` reaches [`tp_finalize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_finalize), which for class instances corresponds to the `__del__()` method (consult [**PEP 442**](https://peps.python.org/pep-0442/)). The whole chain unfolds synchronously inside that one `PyList_SetItem()` call.

Being authored in Python, the `__del__()` method is free to run any Python code at all. Might it somehow break the reference to `item` held inside `bug()`? Absolutely! Provided the `__del__()` method can reach the list that was handed to `bug()`, it could run something amounting to `del list[0]`; if that happened to be the final reference to the object, the memory backing it would be released, which leaves `item` dangling.

Once the root cause is clear, the fix is straightforward: bump the reference count up for a little while. Here is how the corrected routine looks:

```c
void
no_bug(PyObject *list)
{
    PyObject *item = PyList_GetItem(list, 0);

    Py_INCREF(item);
    PyList_SetItem(list, 1, PyLong_FromLong(0L));
    PyObject_Print(item, stdout, 0);
    Py_DECREF(item);
}

```

This actually happened. Some earlier Python release shipped forms of this very defect, and a developer burned plenty of hours inside a C debugger trying to work out why his `__del__()` methods kept breaking…

A second way borrowed references cause grief is a thread-related twist. Ordinarily the Python interpreter keeps several threads from stepping on one another, thanks to a [global lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) guarding the whole of Python's object space. That said, you can let go of this lock briefly via the macro [`Py_BEGIN_ALLOW_THREADS`](https://docs.python.org/3.14/c-api/threads.html#c.Py_BEGIN_ALLOW_THREADS) and take it back with [`Py_END_ALLOW_THREADS`](https://docs.python.org/3.14/c-api/threads.html#c.Py_END_ALLOW_THREADS). People do this routinely around blocking I/O calls so other threads can keep the CPU busy while one waits on I/O. Predictably, the function below suffers the identical flaw as the earlier one:

```c
void
bug(PyObject *list)
{
    PyObject *item = PyList_GetItem(list, 0);
    Py_BEGIN_ALLOW_THREADS
    ...some blocking I/O call...
    Py_END_ALLOW_THREADS
    PyObject_Print(item, stdout, 0); /* BUG! */
}

```

[Subject index](INDEX.md) · [Next source section](null-pointer-reference-counting.md) · [Preceding cross-file owner and contract](ownership-rules-and-pydict-setitem.md)
