# Python 3.13.0 alpha 2 / tests / debug

[gh-111808](https://github.com/python/cpython/issues/111808): Tie the default value of `test.support.infinite_recursion()` to whether optimizations were enabled while compiling the interpreter. That helps platforms such as WASI, whose stack size shrinks sharply in debug builds.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
