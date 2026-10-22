# object.__buffer__(*self*, *flags*)

object.__buffer__(*self*, *flags*)

Invoked when a buffer is requested from *self* (for instance, by the [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) constructor). The *flags* argument is an integer denoting the kind of buffer requested, influencing for example whether the buffer that is returned is read-only or writable. [`inspect.BufferFlags`](https://docs.python.org/3.14/library/inspect.html#inspect.BufferFlags) offers a handy way to interpret the flags. The method must return a `memoryview` object.

**Thread safety:** Under [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) Python, implementations must handle any internal export counter through atomic operations. The method has to be safe for concurrent calls from several threads, and the underlying data of the returned buffer must stay valid until the matching `__release_buffer__()` call finishes. See [Thread safety for memoryview objects](https://docs.python.org/3.14/library/threadsafety.html#thread-safety-memoryview) for details.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-buffer-types.md) · [Previous source section](emulating-buffer-types.md) · [Following source section](object-release-buffer.md)
