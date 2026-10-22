# Python 3.13.0 alpha 1 / build / build and platforms

[gh-89886](https://github.com/python/cpython/issues/89886): Regenerating `configure` henceforth demands Autoconf 2.71 and aclocal 1.16.4.

[gh-109191](https://github.com/python/cpython/issues/109191): Repaired a compile error that arose when building against recent libedit releases.

[gh-109054](https://github.com/python/cpython/issues/109054): Repaired building of the `_testcapi` extension on Linux AArch64, where linking against libatomic is required once `<cpython/pyatomic.h>` gets used: the `_Py_atomic_or_uint64()` function leans on libatomic `__atomic_fetch_or_8()` on this platform. The configure script henceforth tests whether linking against libatomic is needed and emits a fresh LIBATOMIC variable used to build the _testcapi extension. Victor Stinner authored the patch.

[gh-63760](https://github.com/python/cpython/issues/63760): Repaired the Solaris build by no longer redefining the `gethostname()` function. Solaris has shipped the function since 2005. Victor Stinner authored the patch, building on an original patch from Jakub Kulík.

[gh-108447](https://github.com/python/cpython/issues/108447): Repaired the x86_64 GNU/Hurd build

[gh-106962](https://github.com/python/cpython/issues/106962): Spot MPI compilers inside `configure`.

[gh-90005](https://github.com/python/cpython/issues/90005): Repaired a regression inside `configure` where we might end up accidentally linking against `libbsd`.

[gh-102404](https://github.com/python/cpython/issues/102404): Documented the steps for carrying out a WASI build on Linux. Also brought in Tools/wasm/build_wasi.sh to serve as a reference implementation backing the docs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
