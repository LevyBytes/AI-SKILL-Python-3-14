# C API pending removal in 3.14: PyDictObject.ma_version_tag; Immutable types with mutable bases

# C Api Pending Removal In 3.14, C Api Pending Removal In 3.15, C Api Pending Removal In 3.16, C Api Pending Removal In 3.18 ...

## Overview

Topics here span the following removal schedules: Pending removal in Python 3.14; then Python 3.15; next Python 3.16; after that Python 3.18; and finally Pending removal in future versions.

## Pending removal in Python 3.14

### Pending removal in Python 3.14

- Within [`PyDictObject`](https://docs.python.org/3.14/c-api/dict.html#c.PyDictObject), the `ma_version_tag` field for extension modules ([**PEP 699**](https://peps.python.org/pep-0699/); [gh-101193](https://github.com/python/cpython/issues/101193)).

- Building [`immutable types`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) whose bases are mutable ([gh-95388](https://github.com/python/cpython/issues/95388)).

[Subject index](INDEX.md) · [Next source section](../python-3-15/pyimport-importmodulenoblock-through-initialization-getters.md)
