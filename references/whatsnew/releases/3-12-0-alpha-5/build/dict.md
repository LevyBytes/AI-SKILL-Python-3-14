# Python 3.12.0 alpha 5 / build / dict

[gh-101152](https://github.com/python/cpython/issues/101152): Following [**PEP 699**](https://peps.python.org/pep-0699/), extension modules now see the `ma_version_tag` field on [`PyDictObject`](https://docs.python.org/3.14/c-api/dict.html#c.PyDictObject) as deprecated. Touching that field raises a compiler warning during compilation. The field is due to disappear in Python 3.14.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
