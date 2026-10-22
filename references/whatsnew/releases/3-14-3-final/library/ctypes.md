# Python 3.14.3 final / library / ctypes

[gh-142164](https://github.com/python/cpython/issues/142164): The ctypes bitfield overflow error message now reports the offset and size calculation correctly.

[gh-143145](https://github.com/python/cpython/issues/143145): A potential reference leak in ctypes, occurring while building results that carry multiple output parameters on error, has been fixed.

[gh-123241](https://github.com/python/cpython/issues/123241): Sidestep reference count operations while garbage-collecting [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) objects.

[gh-144100](https://github.com/python/cpython/issues/144100): A ctypes crash arising from a deprecated `POINTER(str)` type used in `argtypes` has been fixed. Rather than aborting, ctypes now raises a proper Python exception whenever the pointer target type stays unresolved.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
