# Default Memory Allocators

### Default Memory Allocators

Default memory allocators:

| Configuration | Name | PyMem_RawMalloc | PyMem_Malloc | PyObject_Malloc |
| --- | --- | --- | --- | --- |
| Release build | `"pymalloc"` | `malloc` | `pymalloc` | `pymalloc` |
| Debug build | `"pymalloc_debug"` | `malloc` + debug | `pymalloc` + debug | `pymalloc` + debug |
| Release build, without pymalloc | `"malloc"` | `malloc` | `malloc` | `malloc` |
| Debug build, without pymalloc | `"malloc_debug"` | `malloc` + debug | `malloc` + debug | `malloc` + debug |
| Free-threaded build | `"mimalloc"` | `mimalloc` | `mimalloc` | `mimalloc` |
| Free-threaded debug build | `"mimalloc_debug"` | `mimalloc` + debug | `mimalloc` + debug | `mimalloc` + debug |

Legend:

- Name: value for [`PYTHONMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOC) environment variable.

- `malloc`: system allocators from the standard C library, C functions: `malloc()`, `calloc()`, `realloc()` and `free()`.

- `pymalloc`: pymalloc memory allocator.

- `mimalloc`: mimalloc memory allocator.

- "+ debug": with debug hooks on the Python memory allocators.

- "Debug build": [Python build in debug mode](https://docs.python.org/3.14/using/configure.html#debug-build).

[Subject index](INDEX.md) · [Previous source contract](pytype-genericalloc.md) · [Following source contract](pymemallocatorex.md)
