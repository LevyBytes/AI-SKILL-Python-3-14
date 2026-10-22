# Python 3.12.0 alpha 1 / core and builtins / guarantee every frame object built comes valid interpreter frame

[gh-96754](https://github.com/python/cpython/issues/96754): Guarantee that every frame object built comes from a valid interpreter frame. This rules out invalid frames cropping up in backtraces and signal handlers.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
