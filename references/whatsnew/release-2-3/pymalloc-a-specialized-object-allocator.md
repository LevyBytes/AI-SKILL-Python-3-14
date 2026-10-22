# What’s New in Python 2.3 / Pymalloc: A Specialized Object Allocator

### Pymalloc: A Specialized Object Allocator

Python 2.1 gained Pymalloc, a specialized object allocator authored by Vladimir Marangozov. The goal of Pymalloc is to outpace the system `malloc()` while consuming less memory overhead for the allocation patterns common to Python programs. The allocator calls C's `malloc()` function to acquire sizable pools of memory and then satisfies smaller memory requests out of those pools.

Throughout 2.1 and 2.2, pymalloc remained an experimental feature that stayed off by default; to turn it on you had to compile Python explicitly with the `--with-pymalloc` flag handed to the **configure** script. Within 2.3, pymalloc received additional refinement and is now on by default; you'll need to pass `--without-pymalloc` to switch it off.

Code written in Python sees no difference from this change; pymalloc may, however, surface bugs in C extensions. Anyone authoring C extension modules ought to exercise their code with pymalloc on, since certain faulty code can trigger core dumps at runtime.

One especially frequent mistake leads to trouble. Python's C API offers a set of memory allocation functions that used to be plain aliases for the C library's `malloc()` and `free()`, so if you mistakenly called mismatched functions the error went unnoticed. With the object allocator turned on, those functions are no longer aliases of `malloc()` and `free()`, and freeing memory with the wrong function may earn you a core dump. As an illustration, memory allocated through [`PyObject_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Malloc) must be released with [`PyObject_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Free), not `free()`. A handful of modules shipped with Python tripped over this and needed fixing; surely more third-party modules will run into the same issue.

Along with this change, the bewildering array of memory-allocation interfaces was reduced to two API families. Memory obtained from one family must never be touched by functions belonging to the other. One family allocates blocks of memory, while the other family of functions is dedicated to allocating Python objects.

- For allocating and freeing a plain block of memory, reach for the "raw memory" family: [`PyMem_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Malloc), [`PyMem_Realloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Realloc), and [`PyMem_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Free).

- The "object memory" family serves as the gateway to the pymalloc facility outlined above and leans toward handling a great many "small" allocations: [`PyObject_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Malloc), [`PyObject_Realloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Realloc), and [`PyObject_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Free).

- For allocating and freeing Python objects, turn to the "object" family [`PyObject_New`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_New), [`PyObject_NewVar`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar), and [`PyObject_Del()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_Del).

Owing to extensive effort by Tim Peters, pymalloc in 2.3 additionally offers debugging features for catching memory overwrites and double frees, both in extension modules and inside the interpreter itself. To switch this support on, build a debugging version of the Python interpreter by invoking **configure** with `--with-pydebug`.

For the benefit of extension writers, a header file `Misc/pymemcompat.h` ships with the Python 2.3 source, letting Python extensions adopt the 2.3 memory-allocation interfaces while compiling against any Python release going back to 1.5.2. Just copy this file out of Python's source distribution and bundle it with your extension's source.

See also

[https://hg.python.org/cpython/file/default/Objects/obmalloc.c](https://hg.python.org/cpython/file/default/Objects/obmalloc.c)

For complete details of the pymalloc implementation, read the comments at the top of the file `Objects/obmalloc.c` within the Python source code. The link above takes you to that file inside the python.org SVN browser.

[Subject index](INDEX.md) · [Previous source section](the-optparse-module.md) · [Next source section](build-and-c-api-changes.md) · [Release/subject declaration](standard-set-type.md)
