# Python 3.12.0 alpha 1 / core and builtins / shrink simple python object down words relocating weakreflist pointer

[gh-95245](https://github.com/python/cpython/issues/95245): Shrink a "simple" Python object down from 8 words to 6 by relocating the weakreflist pointer into the pre-header right ahead of the object's dict/values pointer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
