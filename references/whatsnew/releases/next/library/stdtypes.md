# Python next / library / stdtypes

[gh-151295](https://github.com/python/cpython/issues/151295): Resolved a use-after-free segfault within [`bytes.join()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.join) plus [`bytearray.join()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.join) that might arise when an entry’s [`__buffer__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__buffer__) concurrently alters the sequence undergoing the join. From now on that alteration surfaces as a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) rather than crashing.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
