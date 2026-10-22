# Python 3.14.1 final / security / plistlib

[gh-119342](https://github.com/python/cpython/issues/119342): Address a possible memory denial of service inside the [`plistlib`](https://docs.python.org/3.14/library/plistlib.html#module-plistlib) module. Reading a Plist file from an untrusted source could cause an arbitrary quantity of memory to be allocated. Possible consequences ranged from a [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError), swapping, out of memory (OOM) killed processes or containers, through to outright system crashes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
