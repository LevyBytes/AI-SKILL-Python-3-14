# Python 3.13.0 alpha 4 / core and builtins / frame clear also wipe frame f locals not merely fast locals

[gh-113939](https://github.com/python/cpython/issues/113939): frame.clear(): also wipe frame.f_locals, not merely the fast locals. This matters once frame.f_locals has been touched, since it would then hold references to all the locals too.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
