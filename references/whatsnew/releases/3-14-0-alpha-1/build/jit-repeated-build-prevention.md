# Python 3.14.0 alpha 1 / build / address bug where experimental jit might get rebuilt repeatedly

[gh-118943](https://github.com/python/cpython/issues/118943): Address a bug where the experimental JIT might get rebuilt repeatedly under the `make regen-all` target, opening the door to race conditions on builds with heavy parallelism.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
