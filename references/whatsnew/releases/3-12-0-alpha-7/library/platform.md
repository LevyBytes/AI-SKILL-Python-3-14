# Python 3.12.0 alpha 7 / library / platform

[gh-102491](https://github.com/python/cpython/issues/102491): Speed up importing `platform` by dropping the IronPython version parsing. That IronPython version parsing never actually worked (refer to [https://github.com/IronLanguages/ironpython3/issues/1667](https://github.com/IronLanguages/ironpython3/issues/1667)).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
