# Examples

### Examples

Below is the Overview section's example, reworked so the I/O buffer comes off the Python heap through the first set of functions:

```c
PyObject *res;
char *buf = (char *) PyMem_Malloc(BUFSIZ); /* for I/O */

if (buf == NULL)
    return PyErr_NoMemory();
/* ...Do some I/O operation involving buf... */
res = PyBytes_FromString(buf);
PyMem_Free(buf); /* allocated with PyMem_Malloc */
return res;

```

That very code expressed through the type-oriented set of functions:

```c
PyObject *res;
char *buf = PyMem_New(char, BUFSIZ); /* for I/O */

if (buf == NULL)
    return PyErr_NoMemory();
/* ...Do some I/O operation involving buf... */
res = PyBytes_FromString(buf);
PyMem_Free(buf); /* allocated with PyMem_New */
return res;

```

Observe that throughout both examples above, the buffer is only ever touched by functions drawn from one and the same set. That is deliberate: a single memory block must stay within one memory API family, which keeps the chance of crossing allocators down to the smallest possible. The code below holds a pair of mistakes, and one of them carries the *fatal* label because it brings together two distinct allocators that work on separate heaps.

```c
char *buf1 = PyMem_New(char, BUFSIZ);
char *buf2 = (char *) malloc(BUFSIZ);
char *buf3 = (char *) PyMem_Malloc(BUFSIZ);
...
PyMem_Del(buf3);  /* Wrong -- should be PyMem_Free() */
free(buf2);       /* Right -- allocated via malloc() */
free(buf1);       /* Fatal -- should be PyMem_Free()  */

```

Beyond the functions meant for raw memory blocks taken from the Python heap, Python objects themselves are created and freed through [`PyObject_New`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_New), [`PyObject_NewVar`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar) and `PyObject_Free()`.

The chapter that follows, on building and defining new object types in C, covers these in detail.

[Subject index](INDEX.md) · [Previous source contract](pytracemalloc-track-to-pytracemalloc-untrack.md)
