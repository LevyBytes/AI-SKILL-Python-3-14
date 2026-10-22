# int PyDict_Next(PyObject *p, Py_ssize_t *ppos, PyObject **pkey, PyObject **pvalue)

int PyDict_Next([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *ppos, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **pkey, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **pvalue)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*
Walk through every key-value pair held in the dictionary *p*. Before the first call that kicks off the iteration, the [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) that *ppos* points at has to be set to `0`; the function then yields true for each pair found and yields false after every pair has been delivered. As for *pkey* and *pvalue*, each should either reference a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* variable that receives the matching key and value, or else be `NULL`. Whatever references come back through them are borrowed. Leave *ppos* untouched throughout the iteration. The value it carries stands for offsets inside the dictionary's internal layout, and because that layout is sparse, those offsets do not run in sequence.

For example:

```c
PyObject *key, *value;
Py_ssize_t pos = 0;

while (PyDict_Next(self->dict, &pos, &key, &value)) {
    /* do something interesting with the values... */
    ...
}

```

Refrain from mutating the dictionary *p* while iterating. Reassigning the values tied to existing keys as you go is fine, provided the collection of keys itself stays fixed. To illustrate:

```c
PyObject *key, *value;
Py_ssize_t pos = 0;

while (PyDict_Next(self->dict, &pos, &key, &value)) {
    long i = PyLong_AsLong(value);
    if (i == -1 && PyErr_Occurred()) {
        return -1;
    }
    PyObject *o = PyLong_FromLong(i + 1);
    if (o == NULL)
        return -1;
    if (PyDict_SetItem(self->dict, key, o) < 0) {
        Py_DECREF(o);
        return -1;
    }
    Py_DECREF(o);
}

```

Absent external synchronization, this function offers no thread safety on the [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build. To hold a lock on the dictionary as you iterate across it, reach for [`Py_BEGIN_CRITICAL_SECTION`](https://docs.python.org/3.14/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION):

```c
Py_BEGIN_CRITICAL_SECTION(self->dict);
while (PyDict_Next(self->dict, &pos, &key, &value)) {
    ...
}
Py_END_CRITICAL_SECTION();

```

Note

Under the free-threaded build, you may safely call this function from within a critical section. That said, the references handed back for *pkey* and *pvalue* are [borrowed](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) and stay good only for as long as the critical section is held. Whenever you must work with these objects beyond the critical section, or where that section might be suspended, build a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) instead (with [`Py_NewRef()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_NewRef), say).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pydictobject-to-pydict-copy.md) · [Previous source contract](pydict-items-to-pydict-get-size.md) · [Previous source contract](pydict-merge.md)
