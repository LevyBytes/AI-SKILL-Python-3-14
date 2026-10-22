# Python 3.14.0 release candidate 1 / core and builtins / repair several problems affecting perf trampolines x86 64 aarch64

[gh-136541](https://github.com/python/cpython/issues/136541): Repair several problems affecting the perf trampolines on x86-64 and aarch64. Those trampolines were generated incorrectly in some cases, which could keep the perf integration from operating properly. Pablo Galindo contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
