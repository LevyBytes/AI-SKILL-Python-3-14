# Python 3.14.0 alpha 1 / core and builtins / fix faulty corner cases within complex division they produced

[gh-119372](https://github.com/python/cpython/issues/119372): Fix faulty corner cases within complex division (they produced `(nan+nanj)` output), for instance `1/complex('(inf+infj)')`. Sergey B Kirpichev supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
