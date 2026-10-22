# Python 3.13.0 alpha 3 / core and builtins / compiler and parser

[gh-112388](https://github.com/python/cpython/issues/112388): Repaired an error that led the parser into attempting to overwrite tokenizer errors. pablo Galindo wrote the patch

[gh-107901](https://github.com/python/cpython/issues/107901): The compiler now duplicates basic blocks holding an eval breaker check that lack a line number and have several predecessors.

[gh-107901](https://github.com/python/cpython/issues/107901): The compiler was altered so that synthetic jumps located somewhere other than a loop end skip the eval breaker check.

[gh-89811](https://github.com/python/cpython/issues/89811): Verify that `tp_version_tag` is valid before running bytecode specializations that depend on this value being usable.

[gh-113602](https://github.com/python/cpython/issues/113602): Repaired an error that led the parser into trying to clobber existing errors and then crashing along the way. Pablo Galindo wrote the patch

[gh-113297](https://github.com/python/cpython/issues/113297): Repaired a segfault inside the compiler triggered by a with statement carrying 19 context managers.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
