# Python 3.12.0 beta 1 / core and builtins / stdtypes

[gh-104142](https://github.com/python/cpython/issues/104142): Resolve a case in which [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) or [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) repetition might not honor [**PEP 683**](https://peps.python.org/pep-0683/).

[bpo-39610](https://bugs.python.org/issue?@action=redirect&bpo=39610): Calling `len()` on 0-dimensional [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) objects (for example `memoryview(ctypes.c_uint8(42))`) now raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). It used to return `1`, which clashed with `mem_0d[0]` raising an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
