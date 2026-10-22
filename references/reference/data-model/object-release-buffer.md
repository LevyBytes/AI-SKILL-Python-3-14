# object.__release_buffer__(*self*, *buffer*)

object.__release_buffer__(*self*, *buffer*)

Invoked once a buffer has stopped being needed. Here the *buffer* argument is a [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) object that `__buffer__()` previously returned. The method must free any resources tied to the buffer. This method should return `None`.

**Thread safety:** Under [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) Python, atomic operations are required for every decrement of the export counter. Cleanup of resources has to be thread-safe, given that the final release may race against concurrent releases from other threads.

Buffer objects with no cleanup to perform are not obligated to implement this method.

Added in version 3.12.

See also

[**PEP 688**](https://peps.python.org/pep-0688/) - Making the buffer protocol accessible in Python

Introduces the Python `__buffer__` and `__release_buffer__` methods.

[`collections.abc.Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer)

ABC for buffer types.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-buffer-types.md) · [Previous source section](object-buffer.md) · [Following source section](annotations.md)
