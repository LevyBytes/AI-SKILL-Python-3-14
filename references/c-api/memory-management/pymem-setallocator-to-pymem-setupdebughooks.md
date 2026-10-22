# memory management C API: `PyMem_SetAllocator()`, `PyMem_SetupDebugHooks()`

void PyMem_SetAllocator(PyMemAllocatorDomain domain, PyMemAllocatorEx *allocator)

Set the memory block allocator of the specified domain.

When zero bytes are requested, the new allocator is required to hand back a separate non-`NULL` pointer.

Within the `PYMEM_DOMAIN_RAW` domain, the allocator has to be thread-safe: at the moment the allocator runs, no [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) is [attached](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

Across the other domains, the allocator likewise has to be thread-safe, since separate interpreters that share no [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) may invoke it.

Should the new allocator not be a hook (that is, it does not call through to the previous allocator), you have to call the `PyMem_SetupDebugHooks()` function so that the debug hooks get reinstalled atop the new allocator.

See also [`PyPreConfig.allocator`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.allocator) and [Preinitialize Python with PyPreConfig](https://docs.python.org/3.14/c-api/init_config.html#c-preinit).

Warning

`PyMem_SetAllocator()` does have the following contract:

- You may call it once [`Py_PreInitialize()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_PreInitialize) has run and before [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) runs, so as to put a custom memory allocator in place. Beyond the constraints the domain itself imposes, the installed allocator faces no restrictions (the Raw Domain, for one, lets the allocator run without an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state)). For details, consult the section covering allocator domains.

- Should you call it once Python has wrapped up initialization (that is, after [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) has run) the allocator **must** wrap the existing allocator. Swapping the present allocator out for some arbitrary other one is **not supported**.

Changed in version 3.12: All allocators must be thread-safe.

 void PyMem_SetupDebugHooks(void)

Setup debug hooks in the Python memory allocators to detect memory errors.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pymemallocatorex.md) · [Owning structure and shared ABI conditions](pymemallocatordomain-to-pymem-getallocator.md) · [Following source contract](debug-hooks-on-the-python-memory-allocators.md)
