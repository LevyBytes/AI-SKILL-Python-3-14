# introduction C API: Stolen references and list/tuple construction

Reference theft is uncommon among the functions; the two well-known cases are [`PyList_SetItem()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_SetItem) and [`PyTuple_SetItem()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_SetItem), each of which steals a reference to the supplied item (yet not to the list or tuple receiving that item!). The reason these functions were built to steal a reference is a frequent pattern for filling a list or tuple with freshly allocated objects; as an illustration, building the tuple `(1, 2, "three")` might be written as follows (setting aside error handling for now; a cleaner approach appears further down):

```c
PyObject *t;

t = PyTuple_New(3);
PyTuple_SetItem(t, 0, PyLong_FromLong(1L));
PyTuple_SetItem(t, 1, PyLong_FromLong(2L));
PyTuple_SetItem(t, 2, PyUnicode_FromString("three"));

```

In this snippet, [`PyLong_FromLong()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromLong) hands back a new reference, and that reference is at once stolen by [`PyTuple_SetItem()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_SetItem). Should you still need an object after its reference gets stolen, call [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) to obtain an extra reference prior to invoking the reference-stealing function.

As an aside, the sole means of assigning tuple elements is [`PyTuple_SetItem()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_SetItem); both [`PySequence_SetItem()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_SetItem) and [`PyObject_SetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_SetItem) decline the operation because tuples cannot be mutated. Reserve `PyTuple_SetItem()` for tuples that you yourself are constructing.

The matching code for filling a list relies on [`PyList_New()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_New) together with [`PyList_SetItem()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_SetItem).

That said, in real-world code you'll seldom build and fill a list or tuple this way. A general-purpose function exists, [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue), which assembles most everyday objects out of C values according to a *format string*. As an example, the prior two snippets above could instead be expressed like this (which additionally handles the error checking):

```c
PyObject *tuple, *list;

tuple = Py_BuildValue("(iis)", 1, 2, "three");
list = Py_BuildValue("[iis]", 1, 2, "three");

```

Far more often you'll reach for [`PyObject_SetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_SetItem) and similar calls on items whose references are merely borrowed, such as the parameters handed to whatever function you happen to be writing. Under those conditions, the reference handling is a lot more sensible, since there's no need to acquire a fresh reference solely to hand it off ("let it be stolen"). To demonstrate, the function below assigns every element of a list (really, any mutable sequence) to one supplied item:

```c
int
set_all(PyObject *target, PyObject *item)
{
    Py_ssize_t i, n;

    n = PyObject_Length(target);
    if (n < 0)
        return -1;
    for (i = 0; i < n; i++) {
        PyObject *index = PyLong_FromSsize_t(i);
        if (!index)
            return -1;
        if (PyObject_SetItem(target, index, item) < 0) {
            Py_DECREF(index);
            return -1;
        }
        Py_DECREF(index);
    }
    return 0;
}

```

Things differ a bit when it comes to what functions hand back. Although handing a reference to most functions leaves your ownership duties for that reference unchanged, plenty of functions returning a reference to an object grant you ownership of that reference. The rationale is straightforward: frequently the object coming back is built on the spot, so the reference you receive is the object's only reference. Consequently, the general-purpose functions returning object references, such as [`PyObject_GetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetItem) and [`PySequence_GetItem()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_GetItem), invariably hand back a new reference (ownership of the reference passes to the caller).

Bear in mind that ownership of a reference a function returns hinges solely on the particular function you invoke — *the plumage* (the type of object handed in as a function argument) *doesn't enter into it!* So pulling an item out of a list via [`PyList_GetItem()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_GetItem) leaves you without ownership of the reference — yet fetching that very item from that very list through [`PySequence_GetItem()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_GetItem) (which, as it turns out, accepts identical arguments) does give you ownership of the returned object's reference.

Below is a demonstration of writing a function that totals the items contained in a list of integers; the first version uses [`PyList_GetItem()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_GetItem) and the second uses [`PySequence_GetItem()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_GetItem).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](reference-counts.md) · [Owning C API section and shared conditions](reference-ownership-transfer.md) · [Following source contract](reference-count-details-long-to-long.md)
