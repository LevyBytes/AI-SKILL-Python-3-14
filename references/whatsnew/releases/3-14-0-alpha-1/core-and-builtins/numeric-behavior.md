# Python 3.14.0 alpha 1 / core and builtins / numeric behavior

[gh-119462](https://github.com/python/cpython/issues/119462): Keep the invariants of type versioning intact: * A superclass always receives its version number before its subclasses do * Whenever the tag is invalid the version tag is always zero. * Whenever the tag is valid the version tag is always non-.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
