# Python 3.12.0 alpha 1 / build / functions and types

[gh-94773](https://github.com/python/cpython/issues/94773): `deepfreeze.py` now copes with code objects whose frozensets hold incompatible, unsortable types.

[gh-93207](https://github.com/python/cpython/issues/93207): Compiling Python now demands `va_start()` carry two arguments, as in `va_start(args, format),`. The single-argument form of `va_start()` is no longer used. Kumar Aditya wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
