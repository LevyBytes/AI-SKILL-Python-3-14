# Python 3.12.0 beta 1 / c api / threads and concurrency

[gh-104109](https://github.com/python/cpython/issues/104109): The public C-API gained `Py_NewInterpreterFromConfig()` along with `PyInterpreterConfig` (though not the stable ABI — at least not for now). That function lets you spin up a fresh interpreter with assorted features turned on. It landed in service of PEP 684 (per-interpreter GIL).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
