# Python 3.13.0 alpha 1 / library / exceptions and tracebacks

[gh-106670](https://github.com/python/cpython/issues/106670): Hand the Pdb debugger a brand-new `exceptions` command. With it you can hop across chained exceptions while doing post mortem debugging.

[gh-109033](https://github.com/python/cpython/issues/109033): Exceptions thrown by the os.utime builtin function now carry the related filename

[gh-105375](https://github.com/python/cpython/issues/105375): Address a bug within `_Unpickler_SetInputStream()` where, on failure, an exception could wind up being overwritten.

[gh-105375](https://github.com/python/cpython/issues/105375): Address bugs in `_ssl` initialisation that could yield leaked references plus overwritten exceptions.

[gh-105375](https://github.com/python/cpython/issues/105375): Address bugs within `_ctypes` where exceptions could wind up being overwritten.

[gh-105375](https://github.com/python/cpython/issues/105375): Address bugs within `_elementtree` where exceptions could be overwritten.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
