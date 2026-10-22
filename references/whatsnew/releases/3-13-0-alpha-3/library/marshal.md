# Python 3.13.0 alpha 3 / library / marshal

[gh-113626](https://github.com/python/cpython/issues/113626): Add support for the *allow_code* argument within the [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal) module. Supplying `allow_code=False` blocks serialization and de-serialization of code objects, which is incompatible across Python versions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
