# Python 3.12.0 alpha 1 / build / build and platforms

[gh-96729](https://github.com/python/cpython/issues/96729): Make sure Windows releases produced with `Tools\msi\buildrelease.bat` can be upgraded both to and from official Python releases.

[gh-94801](https://github.com/python/cpython/issues/94801): Repair a `configure` script regression that made certain header checks disregard custom `CPPFLAGS`. That regression had entered via [gh-94802](https://github.com/python/cpython/issues/94802).

[gh-94801](https://github.com/python/cpython/issues/94801): While hunting for headers and libraries, `configure` now applies custom flags such as `ZLIB_CFLAGS` and `ZLIB_LIBS`.

[gh-94682](https://github.com/python/cpython/issues/94682): Build against and test with OpenSSL 1.1.1q

[gh-90005](https://github.com/python/cpython/issues/90005): What `_dbm` needs is now discovered during the configure step.

[gh-94280](https://github.com/python/cpython/issues/94280): The pegen regeneration helper on Windows was revised to locate and run Python 3.9 or newer. Although pegen regeneration had already needed 3.9 or above, earlier the helper might have picked an older interpreter.

[gh-93584](https://github.com/python/cpython/issues/93584): Resolve a `Makefile` race that surfaced while installing a PGO build. Every `test` and `install` target now hangs off the `all` target.

[gh-93491](https://github.com/python/cpython/issues/93491): `configure` is now able to recognize and report the [**PEP 11**](https://peps.python.org/pep-0011/) support tiers.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
