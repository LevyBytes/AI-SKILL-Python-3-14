# What’s New In Python 3.12 / Summary – Release highlights - hashlib, tokenize, typing, unittest, venv

- Owing to what shifted in PEP 701, emitting tokens through the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module runs up to 64% quicker.

Security improvements:

- Swap out the builtin [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) routines for SHA1, SHA3, SHA2-384, SHA2-512, and MD5 in favor of formally verified code drawn from the [HACL*](https://github.com/hacl-star/hacl-star/) project. Those builtin routines stay on as fallbacks, invoked solely whenever OpenSSL fails to supply them.

C API improvements:

- PEP 697, unstable C API tier

- PEP 683, immortal objects

CPython implementation improvements:

- PEP 709, comprehension inlining

- [CPython support](https://docs.python.org/3.14/howto/perf_profiling.html#perf-profiling) for the Linux `perf` profiler

- Implement stack overflow protection on supported platforms

New typing features:

- PEP 692, using [`TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) to annotate [**kwargs](https://docs.python.org/3.14/glossary.html#term-argument)

- PEP 698, [`typing.override()`](https://docs.python.org/3.14/library/typing.html#typing.override) decorator

Important deprecations, removals or restrictions:

- [**PEP 623**](https://peps.python.org/pep-0623/): Drop `wstr` out of Unicode objects within the C API of Python, which trims each [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object by no fewer than 8 bytes.

- [**PEP 632**](https://peps.python.org/pep-0632/): Drop the `distutils` package. Guidance on swapping out the APIs it once offered lives in [**the migration guide**](https://peps.python.org/pep-0632/#migration-advice). Should you still depend on `distutils` at Python 3.12 or later, the third-party [Setuptools](https://setuptools.pypa.io/en/latest/deprecated/distutils-legacy.html) package keeps shipping it.

- [gh-95299](https://github.com/python/cpython/issues/95299): Stop pre-installing `setuptools` into virtual environments built by [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv). Consequently `distutils`, `setuptools`, `pkg_resources`, and `easy_install` are no longer present out of the box; to obtain them, run `pip install setuptools` from inside the [activated](https://docs.python.org/3.14/library/venv.html#venv-explanation) virtual environment.

- Gone now are the `asynchat`, `asyncore`, and `imp` modules, together with a number of [`unittest.TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) method aliases.

[Subject index](INDEX.md) · [Previous source section](summary-release-highlights.md) · [Next source section](pep-695-type-parameter-syntax.md) · [Release/subject declaration](summary-release-highlights.md)
