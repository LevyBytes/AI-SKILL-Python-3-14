# General API Guidelines

### General API Guidelines

The bulk of the C API can be called safely from multiple threads, though a handful of cases do not qualify.

- **Struct Fields**: Reading a field straight out of a Python C API object or struct stops being thread-safe once that same field can be written by another thread at the same time.

- **Macros**: Accessor macros such as [`PyList_GET_ITEM`](https://docs.python.org/3.14/c-api/list.html#c.PyList_GET_ITEM) and [`PyList_SET_ITEM`](https://docs.python.org/3.14/c-api/list.html#c.PyList_SET_ITEM), along with ones like [`PySequence_Fast_GET_SIZE`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Fast_GET_SIZE) that operate on whatever [`PySequence_Fast()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Fast) hands back, skip both error handling and locking entirely. As a result they are unsafe across threads whenever the underlying container might be altered at the same moment.

- **Borrowed References**: Any C API call handing back a [borrowed references](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) can lose its thread-safety once the object holding that reference is changed in parallel. The dedicated borrowed-reference discussion below covers the details.

[Subject index](INDEX.md) · [Previous source context](single-phase-initialization.md) · [Following source context](container-thread-safety.md)
