# Python 3.13.0 alpha 1 / tests / python

[gh-91960](https://github.com/python/cpython/issues/91960): Omit `test_gdb` whenever gdb cannot recover Python frame objects: that is, once a frame reads `<optimized out>`. When Python is compiled using ?clang -Og?, gdb may fail to recover the *frame* parameter of `_PyEval_EvalFrameDefault()`. Under that condition, tests such as `py_bt()` will probably break. Lacking access to Python frames, `python-gdb.py` is mostly clueless on retrieving the Python traceback. Furthermore, `test_gdb` is no longer omitted on macOS when Python is compiled with Clang. Victor Stinner authored the patch.

[gh-108834](https://github.com/python/cpython/issues/108834): Once regrtest reruns failed tests under verbose mode (`./python -m test --rerun`), those tests now rerun inside fresh worker processes instead of executing within the main process. Should a test crash or get killed by a timeout, the main process can spot and deal with the killed worker process. The reruns happen in parallel whenever the `-jN` option drives tests in parallel. Victor Stinner authored the patch.

[gh-103053](https://github.com/python/cpython/issues/103053): Corrected test_tools.test_freeze on FreeBSD by running ?make distclean? rather than ?make clean? inside the copied source tree, which also strips out the ?python? program. Victor Stinner authored the patch.

[gh-110152](https://github.com/python/cpython/issues/110152): Dropped `Tools/scripts/run_tests.py` together with `make hostrunnertest`. Simply invoke `./python -m test --slow-ci`, `make buildbottest`, or `make test` in their place. The Python test runner (regrtest) by itself now copes with cross-compilation and HOSTRUNNER. On top of that it appends options to Python ? fast `-u -E -W default -bb` ? whenever the `--fast-ci` or `--slow-ci` option is supplied. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
