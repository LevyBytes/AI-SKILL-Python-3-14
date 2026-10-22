# Python 3.14.0 alpha 2 / core and builtins / platform

[gh-126195](https://github.com/python/cpython/issues/126195): On macOS Apple Silicon, JIT throughput rises 1.4% through the use of platform-specific memory protection APIs. Patch by Diego Russo.

[gh-126795](https://github.com/python/cpython/issues/126795): Raise the threshold governing JIT code warmup. Subject to platform and workload, this may yield 1-9% better performance plus 3-5% lower memory use.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
