# Python 3.14.0 alpha 3 / core and builtins / fix broken corner cases produced nan nanj complex multiplication

[gh-120010](https://github.com/python/cpython/issues/120010): Fix the broken corner cases that produced `(nan+nanj)` from complex multiplication, for instance `(1e300+1j)*(nan+infj)`. Sergey B Kirpichev wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
