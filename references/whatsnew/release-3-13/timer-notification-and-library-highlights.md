# What's New In Python 3.13 / Summary ? Release Highlights - os, random, ssl, typing, warnings

The [`os`](https://docs.python.org/3.14/library/os.html#module-os) module gained a [suite of new functions](https://docs.python.org/3.14/library/os.html#os-timerfd) for handling Linux’s timer notification file descriptors.

- The [`random`](https://docs.python.org/3.14/library/random.html#module-random) module now ships a [command-line interface](https://docs.python.org/3.14/library/random.html#random-cli).

Security improvements:

- [`ssl.create_default_context()`](https://docs.python.org/3.14/library/ssl.html#ssl.create_default_context) now turns on [`ssl.VERIFY_X509_PARTIAL_CHAIN`](https://docs.python.org/3.14/library/ssl.html#ssl.VERIFY_X509_PARTIAL_CHAIN) and [`ssl.VERIFY_X509_STRICT`](https://docs.python.org/3.14/library/ssl.html#ssl.VERIFY_X509_STRICT) as its default flags.

C API improvements:

- The [`Py_mod_gil`](https://docs.python.org/3.14/c-api/module.html#c.Py_mod_gil) slot now signals that an extension module is able to run with the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) turned off.

- The [PyTime C API](https://docs.python.org/3.14/c-api/time.html) is new, exposing access to system clocks.

- [`PyMutex`](https://docs.python.org/3.14/c-api/synchronization.html#c.PyMutex) is a newly added lightweight mutex that takes up just one byte.

- A new [suite of functions](https://docs.python.org/3.14/c-api/monitoring.html#c-api-monitoring) exists for emitting [**PEP 669**](https://peps.python.org/pep-0669/) monitoring events from the C API.

New typing features:

- [**PEP 696**](https://peps.python.org/pep-0696/): Type parameters ([`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar), [`typing.ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec), and [`typing.TypeVarTuple`](https://docs.python.org/3.14/library/typing.html#typing.TypeVarTuple)) can now take defaults.

- [**PEP 702**](https://peps.python.org/pep-0702/): A new [`warnings.deprecated()`](https://docs.python.org/3.14/library/warnings.html#warnings.deprecated) decorator brings the ability to flag deprecations both within the type system and at runtime.

- [**PEP 705**](https://peps.python.org/pep-0705/): [`typing.ReadOnly`](https://docs.python.org/3.14/library/typing.html#typing.ReadOnly) lets you flag a member of a [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) as read-only where type checkers are concerned.

- [**PEP 742**](https://peps.python.org/pep-0742/): [`typing.TypeIs`](https://docs.python.org/3.14/library/typing.html#typing.TypeIs) delivers more intuitive narrowing of types, serving as an alternative to [`typing.TypeGuard`](https://docs.python.org/3.14/library/typing.html#typing.TypeGuard).

Platform support:

- [**PEP 730**](https://peps.python.org/pep-0730/): Apple’s iOS counts as an officially supported platform now, at [**tier 3**](https://peps.python.org/pep-0011/#tier-3).

- [**PEP 738**](https://peps.python.org/pep-0738/): Android counts as an officially supported platform now, at [**tier 3**](https://peps.python.org/pep-0011/#tier-3).

- `wasm32-wasi` is supported as of now as a [**tier 2**](https://peps.python.org/pep-0011/#tier-2) platform.

- `wasm32-emscripten` no longer counts as an officially supported platform.

Important removals:

- PEP 594: The final 19 ?dead batteries? (legacy stdlib modules) are gone from the standard library: `aifc`, `audioop`, `cgi`, `cgitb`, `chunk`, `crypt`, `imghdr`, `mailcap`, `msilib`, `nis`, `nntplib`, `ossaudiodev`, `pipes`, `sndhdr`, `spwd`, `sunau`, `telnetlib`, `uu` and `xdrlib`.

- Drop the **2to3** tool plus the `lib2to3` module (which were deprecated in Python 3.11).

- Drop the `tkinter.tix` module (deprecated back in Python 3.6).

- Drop the `locale.resetlocale()` function.

[Subject index](INDEX.md) · [Previous source section](summary-release-highlights.md) · [Next source section](summary-release-highlights.md) · [Release/subject declaration](summary-release-highlights.md)
