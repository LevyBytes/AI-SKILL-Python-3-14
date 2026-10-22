# What's New In Python 3.10 / Build Changes — atexit, ensurepip, sqlite3

### Build Changes

- [**PEP 644**](https://peps.python.org/pep-0644/): Building Python now demands OpenSSL 1.1.1 or a later release. Support for OpenSSL 1.0.2 has been dropped. (Contributed by Christian Heimes in [bpo-43669](https://bugs.python.org/issue?@action=redirect&bpo=43669).)

- Building Python now depends on the C99 functions `snprintf()` and `vsnprintf()` being present. (Contributed by Victor Stinner in [bpo-36020](https://bugs.python.org/issue?@action=redirect&bpo=36020).)

- The [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) module now needs at least SQLite 3.7.15. (Contributed by Sergey Fedoseev and Erlend E. Aasland in [bpo-40744](https://bugs.python.org/issue?@action=redirect&bpo=40744) and [bpo-40810](https://bugs.python.org/issue?@action=redirect&bpo=40810).)

- From now on the [`atexit`](https://docs.python.org/3.14/library/atexit.html#module-atexit) module is required to be compiled as a built-in module at all times. (Contributed by Victor Stinner in [bpo-42639](https://bugs.python.org/issue?@action=redirect&bpo=42639).)

- Add [`--disable-test-modules`](https://docs.python.org/3.14/using/configure.html#cmdoption-disable-test-modules) option to the `configure` script: when set, the test modules get neither compiled nor installed. (Contributed by Xavier de Gaye, Thomas Petazzoni and Peixing Xin in [bpo-27640](https://bugs.python.org/issue?@action=redirect&bpo=27640).)

- Add [`--with-wheel-pkg-dir=PATH option`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-wheel-pkg-dir) to the `./configure` script. When you supply it, the [`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip) module searches that directory for `setuptools` and `pip` wheel packages: when both exist there, those wheel packages take the place of the bundled ensurepip wheel packages.

Several Linux distribution packaging guidelines advise against shipping bundled dependencies. As one case, Fedora places wheel packages under the `/usr/share/python-wheels/` directory and skips installation of the `ensurepip._bundled` package.

(Contributed by Victor Stinner in [bpo-42856](https://bugs.python.org/issue?@action=redirect&bpo=42856).)

- Add a new [`configure --without-static-libpython option`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-static-libpython) so the `libpythonMAJOR.MINOR.a` static library is skipped during the build and the `python.o` object file is not installed.

(Contributed by Victor Stinner in [bpo-43103](https://bugs.python.org/issue?@action=redirect&bpo=43103).)

- The `configure` script will now call upon the `pkg-config` utility, when it is present, to locate the Tcl/Tk headers and libraries. Just as before, you can name those locations directly through the `--with-tcltk-includes` and `--with-tcltk-libs` configuration options. (Contributed by Manolis Stamatogiannakis in [bpo-42603](https://bugs.python.org/issue?@action=redirect&bpo=42603).)

- Add [`--with-openssl-rpath`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-openssl-rpath) option to `configure` script. This option makes it easier to build Python against a custom OpenSSL installation, for example `./configure --with-openssl=/path/to/openssl --with-openssl-rpath=auto`. (Contributed by Christian Heimes in [bpo-43466](https://bugs.python.org/issue?@action=redirect&bpo=43466).)

[Subject index](INDEX.md) · [Previous source section](bytecode-migration-changes.md) · [Next source section](c-api-changes-pep-652-maintaining-the-stable-abi.md) · [Release/subject declaration](summary-release-highlights.md)
