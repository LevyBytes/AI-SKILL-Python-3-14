# Python 3.14.6 final / c api / correct dynamic annotations h header compiled under c together valgrind wrapping

[gh-150907](https://github.com/python/cpython/issues/150907): Correct the `dynamic_annotations.h` header when compiled under C++ together with Valgrind, by wrapping the C++ template in an `extern "C++" scope`. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
