# Overview

### Memory Management

### Overview

Within Python, a private heap holds every Python object and data structure, and memory management revolves around that heap. Internally, the *Python memory manager* takes responsibility for keeping this private heap in order. Several components make up the Python memory manager, each handling some facet of dynamic storage — among them sharing, segmentation, preallocation, and caching.

A raw memory allocator sits at the bottom and guarantees, by talking to the operating system's memory manager, that the private heap holds enough space for all of Python's data. Layered above that raw allocator are a number of object-specific allocators that work over the very same heap, each applying its own memory policy tuned to the quirks of a given object type. Integers, for instance, are handled in the heap by a scheme distinct from the one used for strings, tuples, or dictionaries, since integers carry their own storage demands and their own balance between speed and space. In this way the Python memory manager hands off portions of the job to those object-specific allocators, while still guaranteeing that none of them stray outside the private heap.

Keep in mind that the interpreter alone runs the management of the Python heap, and the user cannot steer it — not even users who routinely pass around object pointers that reference memory blocks within that heap. Whenever Python objects or other internal buffers need heap space, the Python memory manager supplies it on demand by way of the Python/C API functions catalogued in this document.

Extension authors, in order to steer clear of memory corruption, must never reach for the C library's exported functions — `malloc()`, `calloc()`, `realloc()` and `free()` — to manipulate Python objects directly. Doing so intermixes calls to the C allocator with calls to the Python memory manager, and because the two rely on different algorithms over different heaps, the outcome is fatal. That said, for purposes that stand on their own, you may freely grab and give back memory blocks through the C library allocator, the way the example below shows:

```c
PyObject *res;
char *buf = (char *) malloc(BUFSIZ); /* for I/O */

if (buf == NULL)
    return PyErr_NoMemory();
...Do some I/O operation involving buf...
res = PyBytes_FromString(buf);
free(buf); /* malloc'ed */
return res;

```

Here, the C library allocator services the I/O buffer's memory request. The Python memory manager comes into play solely to allocate the bytes object handed back as the result.

That said, in the bulk of cases the advice is to draw memory from the Python heap, precisely because the Python memory manager governs that heap. Such an approach is mandatory, for example, whenever the interpreter gains new object types coded in C. There is also a second motive for choosing the Python heap: you want to *inform* the Python memory manager of how much memory the extension module needs. Even where the memory you ask for serves only internal, highly specialized ends, routing every memory request through the Python memory manager gives the interpreter a truer picture of its total memory footprint. As a result, in some scenarios the Python memory manager will, or will not, set off the right responses — garbage collection, memory compaction, or other preventive steps. Bear in mind that when you lean on the C library allocator as the earlier example did, the I/O buffer's allocated memory slips entirely past the Python memory manager.

See also

Through the [`PYTHONMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOC) environment variable, you can select which memory allocators Python employs.

The [`PYTHONMALLOCSTATS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOCSTATS) environment variable, once set, makes the pymalloc memory allocator emit statistics each time a fresh pymalloc object arena gets created, as well as during shutdown.

[Subject index](INDEX.md) · [Following source contract](allocator-domains.md)
