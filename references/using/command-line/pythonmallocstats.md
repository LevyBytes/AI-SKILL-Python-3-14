# PYTHONMALLOCSTATS

PYTHONMALLOCSTATS

When set to a non-empty string, Python prints statistics from the [pymalloc memory allocator](https://docs.python.org/3.14/c-api/memory.html#pymalloc) or the [mimalloc memory allocator](https://docs.python.org/3.14/c-api/memory.html#mimalloc) (whichever happens to be active) each time a fresh object arena is allocated, plus at shutdown.

This variable gets disregarded when the `PYTHONMALLOC` environment variable is applied to compel the `malloc()` allocator of the C library, or when Python is configured lacking both `pymalloc` and `mimalloc` support.

Changed in version 3.6: This variable works now on Python compiled in release mode as well. When assigned an empty string, it has no effect anymore.

[Subject index](INDEX.md) · [Previous source section](pythonmalloc.md) · [Following source section](pythonlegacywindowsfsencoding.md)
