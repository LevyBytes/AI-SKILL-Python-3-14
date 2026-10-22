# What’s New In Python 3.12 / Build Changes — compileall

### Build Changes

- Python has stopped relying on `setup.py` to compile shared C extension modules. Things like headers and libraries are discovered by the `configure` script. The `Makefile` is what builds the extensions. The bulk of extensions lean on `pkg-config` and revert to manual detection otherwise. (Contributed by Christian Heimes in [gh-93939](https://github.com/python/cpython/issues/93939).)

- Building Python now demands `va_start()` carrying two parameters, as in `va_start(args, format),`. The single-parameter form of `va_start()` is no longer invoked. (Contributed by Kumar Aditya in [gh-93207](https://github.com/python/cpython/issues/93207).)

- Whenever the Clang compiler will take the flag, CPython now defaults its link time optimization policy to the ThinLTO option. (Contributed by Donghee Na in [gh-89536](https://github.com/python/cpython/issues/89536).)

- Introduce a `COMPILEALL_OPTS` variable into the `Makefile` so that [`compileall`](https://docs.python.org/3.14/library/compileall.html#module-compileall) options (defaulting to `-j0`) can be overridden during `make install`. The 3 separate `compileall` invocations were also folded into one command that produces .pyc files covering every optimization level (0, 1, 2) in a single pass. (Contributed by Victor Stinner in [gh-99289](https://github.com/python/cpython/issues/99289).)

- Introduce platform triplets covering 64-bit LoongArch:

  - loongarch64-linux-gnusf

  - loongarch64-linux-gnuf32

  - loongarch64-linux-gnu

(Contributed by Zhang Na in [gh-90656](https://github.com/python/cpython/issues/90656).)

- `PYTHON_FOR_REGEN` now calls for Python 3.10 or a later release.

- Regenerating `configure` now calls for Autoconf 2.71 alongside aclocal 1.16.4. (Contributed by Christian Heimes in [gh-89886](https://github.com/python/cpython/issues/89886).)

- The Windows builds together with the macOS installers offered through python.org now ship OpenSSL 3.0.

[Subject index](INDEX.md) · [Previous source section](changes-in-the-python-api.md) · [Next source section](c-api-changes-new-features.md) · [Release/subject declaration](summary-release-highlights.md)
