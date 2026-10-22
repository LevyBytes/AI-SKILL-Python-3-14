# Call and iterator protocol slots — tp_call, PyObject, PyArg_ParseTuple, PyUnicode_FromFormat, tp_iter, tp_iternext, PyTypeObject

What follows is a simple sample `tp_call` implementation:

```c
static PyObject *
newdatatype_call(PyObject *op, PyObject *args, PyObject *kwds)
{
    newdatatypeobject *self = (newdatatypeobject *) op;
    PyObject *result;
    const char *arg1;
    const char *arg2;
    const char *arg3;

    if (!PyArg_ParseTuple(args, "sss:call", &arg1, &arg2, &arg3)) {
        return NULL;
    }
    result = PyUnicode_FromFormat(
        "Returning -- value: [%d] arg1: [%s] arg2: [%s] arg3: [%s]\n",
        self->obj_UnderlyingDatatypePtr->size,
        arg1, arg2, arg3);
    return result;
}

```

```c
/* Iterators */
getiterfunc tp_iter;
iternextfunc tp_iternext;

```

It is these functions that underpin the iterator protocol. Each handler accepts a single parameter only — the instance on whose behalf it is invoked — and gives back a new reference. Where something goes wrong, they ought to set an exception and hand back `NULL`. The [`tp_iter`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iter) slot maps onto Python's [`__iter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__iter__) method, whereas [`tp_iternext`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iternext) maps onto Python's [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) method.

Every [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) object is required to supply the [`tp_iter`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iter) handler, and that handler has to yield an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) object. The very same rules that govern Python classes hold here too:

- When a collection (lists and tuples among them) is able to back several independent iterators, every invocation of [`tp_iter`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iter) ought to build and return a fresh iterator.

- An object that admits only a single pass of iteration (typically because iterating has side effects, as with file objects) may realize [`tp_iter`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iter) by handing back a new reference to itself — and consequently ought to furnish the [`tp_iternext`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iternext) handler as well.

Every [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) object ought to furnish both [`tp_iter`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iter) and [`tp_iternext`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iternext). The `tp_iter` handler belonging to an iterator should hand back a new reference to that iterator. Meanwhile its `tp_iternext` handler should hand back a new reference to whatever comes next in the iteration, assuming one exists. Once the iteration is spent, `tp_iternext` is free to give back `NULL` while leaving any exception unset, or alternatively to raise [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) *in addition* to giving back `NULL`; skipping the exception buys a marginal performance gain. Whenever a genuine error arises, `tp_iternext` must without fail set an exception and return `NULL`.

[Subject index](INDEX.md) · [Next source section](weak-reference-support-and-tp-free.md) · [Preceding cross-file owner and contract](abstract-protocol-support-and-pyarg-parsetupleandkeywords.md)
