# Python 3.11.0 beta 1 / build / build and platforms

[gh-89452](https://github.com/python/cpython/issues/89452): gdbm-compat now wins out over ndbm whenever both are present on the system. Doing so lets the build steer clear of the troublesome ndbm.h on macOS.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
