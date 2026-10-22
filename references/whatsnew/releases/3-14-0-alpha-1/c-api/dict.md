# Python 3.14.0 alpha 1 / c api / dict

[gh-120858](https://github.com/python/cpython/issues/120858): Inside the free-threaded build, [`PyDict_Next()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Next) stops locking the dictionary. Now the caller has to do that locking around the whole iteration loop.

[gh-124296](https://github.com/python/cpython/issues/124296): Following [**PEP 699**](https://peps.python.org/pep-0699/), [`PyDictObject`](https://docs.python.org/3.14/c-api/dict.html#c.PyDictObject) drops its private `ma_version_tag` version-tag field. Python 3.6 first introduced that field ([**PEP 509**](https://peps.python.org/pep-0509/)), and Python 3.12 marked it deprecated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
