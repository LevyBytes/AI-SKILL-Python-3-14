# Python 3.13.0 alpha 1 / tests / compiler and parser

[gh-105776](https://github.com/python/cpython/issues/105776): Repaired test_cppext when the C compiler command carries the `-std=c11` option by stripping `-std=` options off the compiler command. Victor Stinner authored the patch.

[gh-103053](https://github.com/python/cpython/issues/103053): Bypass test_freeze_simple_script() inside test_tools.test_freeze whenever Python is compiled via `./configure --enable-optimizations`, i.e. with Profile Guided Optimization (PGO): doing so merely drags the test out too long. Plenty of other CIs exercise the freeze tool using different (quicker) compiler flags. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
