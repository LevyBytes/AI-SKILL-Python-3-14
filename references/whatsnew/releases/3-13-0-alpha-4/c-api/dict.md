# Python 3.13.0 alpha 4 / c api / dict

[gh-112066](https://github.com/python/cpython/issues/112066): Introduced [`PyDict_SetDefaultRef()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_SetDefaultRef), which stores a key plus value into a dictionary whenever that key has not yet been set. The behavior mirrors [`dict.setdefault()`](https://docs.python.org/3.14/library/stdtypes.html#dict.setdefault), though it hands back an integer flag signaling whether the key already existed. It likewise resembles [`PyDict_SetDefault()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_SetDefault), aside from yielding a strong reference rather than a borrowed reference.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
