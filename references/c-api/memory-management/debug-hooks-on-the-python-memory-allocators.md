# Debug hooks on the Python memory allocators

### Debug hooks on the Python memory allocators

Whenever [Python is built in debug mode](https://docs.python.org/3.14/using/configure.html#debug-build), the call to `PyMem_SetupDebugHooks()` happens during [Python preinitialization](https://docs.python.org/3.14/c-api/init_config.html#c-preinit), arranging debug hooks across the Python memory allocators so that memory errors get caught.

By way of the [`PYTHONMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOC) environment variable, you can put debug hooks onto a Python that was compiled for release (ex: `PYTHONMALLOC=debug`).

The `PyMem_SetupDebugHooks()` function can be used to set debug hooks after calling `PyMem_SetAllocator()`.

What these debug hooks do is stuff dynamically allocated memory blocks with distinctive, recognizable bit patterns. Memory just allocated gets the byte `0xCD` (`PYMEM_CLEANBYTE`), and memory just freed gets the byte `0xDD` (`PYMEM_DEADBYTE`). Around each memory block sit "forbidden bytes" carrying the byte `0xFD` (`PYMEM_FORBIDDENBYTE`). Runs of such bytes rarely amount to valid addresses, floats, or ASCII strings.

Runtime checks:

- Catch API violations. As one case, spot a `PyObject_Free()` invoked against a block that `PyMem_Malloc()` had allocated.

- Catch a write that lands ahead of where the buffer begins (buffer underflow).

- Catch a write that lands past where the buffer ends (buffer overflow).

- Confirm that an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) exists at the time the allocator functions of the `PYMEM_DOMAIN_OBJ` (ex: `PyObject_Malloc()`) and `PYMEM_DOMAIN_MEM` (ex: `PyMem_Malloc()`) domains run.

When something goes wrong, the debug hooks turn to the [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) module to recover the traceback pointing at where a memory block was allocated. That traceback shows up only when `tracemalloc` happens to be tracing Python memory allocations and the particular memory block was among those traced.

Let *S* = `sizeof(size_t)`. At either end of every requested block of *N* bytes, `2*S` bytes get tacked on. What follows is the memory layout, with p standing for the address a malloc-like or realloc-like function returns (`p[i:j]` denotes the slice of bytes running from `*(p+i)` inclusive through `*(p+j)` exclusive; observe that negative indices are not treated the way a Python slice treats them):

`p[-2*S:-S]`

The byte count that was first requested. Stored as a big-endian size_t (which reads more easily in a memory dump).

`p[-S]`

API identifier (ASCII character):

- `'r'` for `PYMEM_DOMAIN_RAW`.

- `'m'` for `PYMEM_DOMAIN_MEM`.

- `'o'` for `PYMEM_DOMAIN_OBJ`.

`p[-S+1:0]`

Copies of PYMEM_FORBIDDENBYTE. Used to catch under- writes and reads.

`p[0:N]`

The memory you asked for, packed with copies of PYMEM_CLEANBYTE so that any read of uninitialized memory is flagged. Whenever a realloc-style call asks for a bigger block, the fresh surplus bytes likewise receive PYMEM_CLEANBYTE. A free-style call instead stamps these bytes over with PYMEM_DEADBYTE, which exposes reads of memory that has been freed. When a realloc-style call shrinks a block, the leftover old bytes are filled with PYMEM_DEADBYTE as well.

`p[N:N+S]`

A run of PYMEM_FORBIDDENBYTE copies, there to expose stray writes and reads past the bounds.

`p[N+S:N+2*S]`

Comes into play solely when the `PYMEM_DEBUG_SERIALNO` macro has been defined, which is not the case out of the box.

A serial number that climbs by 1 with every malloc-style or realloc-style call. Stored as a big-endian `size_t`. Should “bad memory” turn up afterward, that serial number is a handy hook for placing a breakpoint on a later run so you can pin down the exact moment this block went out. Incrementing happens in just one spot — the static function bumpserialno() within obmalloc.c — which exists precisely to make setting such a breakpoint painless.

Before doing anything else, a realloc-style or free-style call confirms that the PYMEM_FORBIDDENBYTE bytes guarding both ends remain untouched. Once they have been disturbed, a diagnostic is sent to stderr and the run is halted through Py_FatalError(). The second common way things break is a memory fault that arises when a program picks up one of these special bit patterns and treats it as though it were an address. Stepping into a debugger at that point and inspecting the object, you will most likely find it packed entirely with PYMEM_DEADBYTE (a sign that freed memory is in use) or PYMEM_CLEANBYTE (a sign that uninitialized memory is in use).

Changed in version 3.6: The `PyMem_SetupDebugHooks()` function operates on a release-mode build of Python as well now. When an error occurs, the debug hooks reach for [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) to recover the traceback for where a block was allocated. On top of that, the hooks now verify that an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is present whenever calls land in the `PYMEM_DOMAIN_OBJ` and `PYMEM_DOMAIN_MEM` domains.

Changed in version 3.8: The byte patterns `0xCB` (`PYMEM_CLEANBYTE`), `0xDB` (`PYMEM_DEADBYTE`) and `0xFB` (`PYMEM_FORBIDDENBYTE`) gave way to `0xCD`, `0xDD` and `0xFD`, matching the values the Windows CRT debug `malloc()` and `free()` employ.

[Subject index](INDEX.md) · [Previous source contract](pymem-setallocator-to-pymem-setupdebughooks.md) · [Following source contract](the-pymalloc-allocator.md)
