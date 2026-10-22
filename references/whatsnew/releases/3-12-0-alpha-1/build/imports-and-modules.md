# Python 3.12.0 alpha 1 / build / imports and modules

[gh-96269](https://github.com/python/cpython/issues/96269): Shared module targets now rely on the new `MODULE_DEPS` variable, which encompasses `EXPORTSYMS`. That corrects a build ordering problem on the unsupported AIX platform.

[gh-94847](https://github.com/python/cpython/issues/94847): Resolved a `_decimal` module build problem on GCC when building with LTO together with pydebug. Debug builds no longer compel inlining of functions.

[gh-94404](https://github.com/python/cpython/issues/94404): `makesetup` sidesteps a sed quirk seen on macOS and selects the right CFLAGS for object files headed into a shared extension. To dodge collisions with system headers, Module CFLAGS now precede PY_STDMODULE_CFLAGS.

[gh-69093](https://github.com/python/cpython/issues/69093): Fix `Modules/Setup.stdlib.in` rule for `_sqlite3` extension.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
