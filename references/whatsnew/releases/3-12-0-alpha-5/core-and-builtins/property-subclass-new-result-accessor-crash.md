# Python 3.12.0 alpha 5 / core and builtins / patch segfault inside property getter setter deleter surfaced once property

[gh-100942](https://github.com/python/cpython/issues/100942): Patch a segfault inside property.getter/setter/deleter that surfaced once a property subclass overrode `__new__` to hand back a non-property instance.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
