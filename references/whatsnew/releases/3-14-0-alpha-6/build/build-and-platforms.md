# Python 3.14.0 alpha 6 / build / build and platforms

[gh-131035](https://github.com/python/cpython/issues/131035): Using `-flto=thin` speeds up build times when compiling with clang-cl on Windows. Chris Eibl supplied the patch.

[gh-130090](https://github.com/python/cpython/issues/130090): Compiling with `PlatformToolset=ClangCL` on Windows now supports PGO (profile guided optimization). Chris Eibl supplied the patch, with invaluable support from Steve Dover.

[gh-129989](https://github.com/python/cpython/issues/129989): A defect whereby the tailcall interpreter stayed enabled even after `--without-tail-call-interp` was passed to the configure script has been fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
