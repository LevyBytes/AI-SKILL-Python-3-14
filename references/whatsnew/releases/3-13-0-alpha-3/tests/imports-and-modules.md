# Python 3.13.0 alpha 3 / tests / imports and modules

[gh-113633](https://github.com/python/cpython/issues/113633): Adopt module state within the _testcapi extension module.

[gh-108927](https://github.com/python/cpython/issues/108927): Eliminate an ordering dependency among same-process tests: a test owning submodules (such as test_importlib) trailing one that imports its submodule (such as test_importlib.util) and sitting ahead of a test (such as test_unittest or test_compileall) that consumes that submodule.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
