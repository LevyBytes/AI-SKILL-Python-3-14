# Python 3.13.0 alpha 3 / core and builtins / sidestep undefined behaviour running perf trampolines holding off freeing

[gh-112367](https://github.com/python/cpython/issues/112367): Sidestep undefined behaviour when running the perf trampolines by holding off on freeing the code arenas until shutdown. Pablo Galindo wrote the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
