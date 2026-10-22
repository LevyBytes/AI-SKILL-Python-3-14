# initialization config C API: Preconfiguration initialization and allocator selection

### PyPreConfig

 type PyPreConfig

A structure that handles preinitializing Python.

Function to initialize a preconfiguration:

 void PyPreConfig_InitPythonConfig(PyPreConfig *preconfig)

Set up the preconfiguration with Python Configuration.

 void PyPreConfig_InitIsolatedConfig(PyPreConfig *preconfig)

Set up the preconfiguration with Isolated Configuration.

Structure fields:

 int allocator

The chosen Python memory allocators:

- `PYMEM_ALLOCATOR_NOT_SET` (`0`): leave the memory allocators alone (keep the defaults).

- `PYMEM_ALLOCATOR_DEFAULT` (`1`): [default memory allocators](https://docs.python.org/3.14/c-api/memory.html#default-memory-allocators).

- `PYMEM_ALLOCATOR_DEBUG` (`2`): [default memory allocators](https://docs.python.org/3.14/c-api/memory.html#default-memory-allocators) with [debug hooks](https://docs.python.org/3.14/c-api/memory.html#pymem-debug-hooks).

- `PYMEM_ALLOCATOR_MALLOC` (`3`): rely on the C library's `malloc()`.

- `PYMEM_ALLOCATOR_MALLOC_DEBUG` (`4`): require `malloc()` together with [debug hooks](https://docs.python.org/3.14/c-api/memory.html#pymem-debug-hooks).

- `PYMEM_ALLOCATOR_PYMALLOC` (`5`): [Python pymalloc memory allocator](https://docs.python.org/3.14/c-api/memory.html#pymalloc).

- `PYMEM_ALLOCATOR_PYMALLOC_DEBUG` (`6`): [Python pymalloc memory allocator](https://docs.python.org/3.14/c-api/memory.html#pymalloc) with [debug hooks](https://docs.python.org/3.14/c-api/memory.html#pymem-debug-hooks).

- `PYMEM_ALLOCATOR_MIMALLOC` (`6`): rely on `mimalloc`, a quick malloc replacement.

- `PYMEM_ALLOCATOR_MIMALLOC_DEBUG` (`7`): rely on `mimalloc`, a quick malloc replacement, with [debug hooks](https://docs.python.org/3.14/c-api/memory.html#pymem-debug-hooks).

`PYMEM_ALLOCATOR_PYMALLOC` along with `PYMEM_ALLOCATOR_PYMALLOC_DEBUG` are unavailable when Python is [`configured using --without-pymalloc`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-pymalloc).

`PYMEM_ALLOCATOR_MIMALLOC` along with `PYMEM_ALLOCATOR_MIMALLOC_DEBUG` are unavailable when Python is [`configured using --without-mimalloc`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-mimalloc), or when the underlying atomic support is missing.

Refer to [Memory Management](https://docs.python.org/3.14/c-api/memory.html#memory).

Default: `PYMEM_ALLOCATOR_NOT_SET`.

 int configure_locale

Apply the user's preferred locale to the LC_CTYPE locale.

When this equals `0`, the `coerce_c_locale` and `coerce_c_locale_warn` members are forced to `0`.

Refer to the [locale encoding](https://docs.python.org/3.14/glossary.html#term-locale-encoding).

Default: `1` in Python config, `0` in isolated config.

[Subject index](INDEX.md) · [Previous source contract](py-exitstatusexception.md) · [Following source contract](coerce-c-locale-to-utf8-mode.md)
