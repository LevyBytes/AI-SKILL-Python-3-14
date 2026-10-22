# Python 3.13.0 alpha 3 / macos / build and platforms

[gh-110459](https://github.com/python/cpython/issues/110459): On macOS, invoking `configure ... --with-openssl-rpath=X/Y/Z` no longer misses OpenSSL during detection.

[gh-65701](https://github.com/python/cpython/issues/65701): Framework builds of Python are unsupported by the **freeze** tool. Note this and exit promptly whenever the tool is run against such a build.

[gh-111973](https://github.com/python/cpython/issues/111973): Move the macOS installer onto SQLite 3.44.2.

[gh-110017](https://github.com/python/cpython/issues/110017): Switch off a signal handling stress test under macOS owing to a macOS defect (FB13453490).

[gh-110820](https://github.com/python/cpython/issues/110820): Ensure the preprocessor definitions `ALIGNOF_MAX_ALIGN_T`, `SIZEOF_LONG_DOUBLE` and `HAVE_GCC_ASM_FOR_X64` come out right for Universal 2 builds under macOS.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
