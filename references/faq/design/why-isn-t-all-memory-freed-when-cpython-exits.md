# Why isn't all memory freed when CPython exits?

### Why isn't all memory freed when CPython exits?

Objects referenced from the global namespaces of Python modules don't always get deallocated as Python shuts down. This can occur when circular references are present. There are likewise certain chunks of memory allocated by the C library that simply cannot be freed (a tool like Purify, for example, will grumble about these). Python, however, is aggressive about tidying memory on exit and does attempt to destroy every last object.

Should you wish to compel Python to delete particular things upon deallocation, use the [`atexit`](https://docs.python.org/3.14/library/atexit.html#module-atexit) module to run a function that forces those deletions.

[Subject index](INDEX.md)
