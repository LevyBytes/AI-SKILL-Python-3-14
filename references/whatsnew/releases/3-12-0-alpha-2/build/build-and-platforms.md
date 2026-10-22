# Python 3.12.0 alpha 2 / build / build and platforms

[gh-98949](https://github.com/python/cpython/issues/98949): Remove the unused build-time dependency on `readelf`.

[gh-98707](https://github.com/python/cpython/issues/98707): Skip the vendored `libmpdec` headers whenever [`--with-system-libmpdec`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-system-libmpdec) is handed to **configure**. Likewise skip the vendored `libexpat` headers whenever [`--with-system-expat`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-system-expat) is handed to **configure**.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
