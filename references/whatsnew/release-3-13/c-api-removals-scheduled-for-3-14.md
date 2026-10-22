# What's New In Python 3.13 / C API Changes / Deprecated C APIs / Pending removal in Python 3.14

#### Pending removal in Python 3.14

- The `ma_version_tag` field within [`PyDictObject`](https://docs.python.org/3.14/c-api/dict.html#c.PyDictObject), as used by extension modules ([**PEP 699**](https://peps.python.org/pep-0699/); [gh-101193](https://github.com/python/cpython/issues/101193)).

- Building [`immutable types`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) whose bases are mutable ([gh-95388](https://github.com/python/cpython/issues/95388)).

[Subject index](INDEX.md) · [Previous source section](c-api-changes-deprecated-c-apis.md) · [Next source section](c-api-removals-scheduled-for-3-15.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-changes-deprecated-c-apis.md)
