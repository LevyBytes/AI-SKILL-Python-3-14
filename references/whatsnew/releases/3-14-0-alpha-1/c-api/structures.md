# Python 3.14.0 alpha 1 / c api / structures

[gh-120600](https://github.com/python/cpython/issues/120600): Throughout the limited C API for 3.14 onward, [`Py_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_TYPE) becomes an opaque function call so the implementation stays hidden. Victor Stinner wrote the patch.

[gh-123465](https://github.com/python/cpython/issues/123465): [`Py_RELATIVE_OFFSET`](https://docs.python.org/3.14/c-api/structures.html#c.Py_RELATIVE_OFFSET) is now permitted within [`PyMemberDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMemberDef) on the dedicated offset member `"__vectorcalloffset__"`, plus on those frowned-upon dedicated offset members `"__dictoffset__"` together with `"__weaklistoffset__"`

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
