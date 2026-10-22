# 3.3.8. Python Debug Build

### 3.3.8. Python Debug Build

A debug build means Python compiled with the `--with-pydebug` configure option.

What a debug build does:

- Shows every warning by default: in the [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module the list of default warning filters is empty.

- Appends `d` onto [`sys.abiflags`](https://docs.python.org/3.14/library/sys.html#sys.abiflags).

- Adds the `sys.gettotalrefcount()` function.

- Adds the [`-X showrefcount`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line option.

- Adds the [`-d`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-d) command line option plus the [`PYTHONDEBUG`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDEBUG) environment variable for debugging the parser.

- Adds support for the `__lltrace__` variable: switches on low-level tracing inside the bytecode evaluation loop whenever the variable is defined.

- Sets up [debug hooks on memory allocators](https://docs.python.org/3.14/c-api/memory.html#default-memory-allocators) so buffer overflow and other memory errors are caught.

- Defines the `Py_DEBUG` and `Py_REF_DEBUG` macros.

- Bring in runtime checks: the relevant code sits between `#ifdef Py_DEBUG` and `#endif`. To switch on the `assert(...)` and `_PyObject_ASSERT(...)` assertions, leave the `NDEBUG` macro undefined (the `--with-assertions` configure option is also worth a look). Chief runtime checks:

  - Apply sanity checks to the arguments passed to functions.

  - When Unicode and int objects are built, their memory is seeded with a recognizable pattern so that use of uninitialized objects can be spotted.

  - Make certain that functions capable of clearing or swapping out the active exception are never invoked while an exception is already raised.

  - Verify that deallocator functions leave the active exception untouched.

  - The garbage collector (the [`gc.collect()`](https://docs.python.org/3.14/library/gc.html#gc.collect) function) performs a few elementary consistency checks across objects.

  - The `Py_SAFE_DOWNCAST()` macro watches for integer underflow and overflow whenever a wide type is downcast to a narrower one.

Have a look as well at the [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) and at the `--with-trace-refs` configure option.

Changed in version 3.8: Release builds now share ABI compatibility with debug builds: setting the `Py_DEBUG` macro no longer pulls in the `Py_TRACE_REFS` macro (refer to the `--with-trace-refs` option). Even so, debug builds continue to surface additional symbols beyond release builds, and code compiled against a debug build may not run against a release build.

[Subject index](INDEX.md) · [Previous source section](without-remote-debug.md) · [Following source section](with-pydebug.md)
