# Python 3.12.0 alpha 5 / windows / single runtime installed py exe launcher filters correctly

[gh-101467](https://github.com/python/cpython/issues/101467): With a single runtime installed, the `py.exe` launcher now filters correctly. It additionally treats tag prefix matches the right way, so `-3.1` will not match `3.11` yet still matches `3.1-32`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
