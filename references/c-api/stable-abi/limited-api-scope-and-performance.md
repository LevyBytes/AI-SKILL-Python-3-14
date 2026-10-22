# Limited API Scope and Performance

### Limited API Scope and Performance

The aim of the Limited API is to permit all that the full C API permits, though perhaps at some performance cost.

As an illustration, [`PyList_GetItem()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_GetItem) is offered, whereas its “unsafe” macro counterpart [`PyList_GET_ITEM()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_GET_ITEM) is not. That macro can run faster since it may lean on version-specific implementation details of the list object.

When `Py_LIMITED_API` is not defined, a number of C API functions get inlined or swapped out for macros. Defining `Py_LIMITED_API` turns that inlining off, which buys stability as Python's data structures evolve, though it may cost some performance.

By omitting the `Py_LIMITED_API` definition, you can build a Limited API extension carrying a version-specific ABI. That may boost performance on that Python version while narrowing compatibility. Building with `Py_LIMITED_API` instead produces an extension you can ship where a version-specific one isn't on hand – for instance, against prereleases of a forthcoming Python version.

[Subject index](INDEX.md) · [Previous source contract](stable-abi.md) · [Following source contract](limited-api-caveats.md)
