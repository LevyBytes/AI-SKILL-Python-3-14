# What's New In Python 3.13 / Free-threaded CPython — sys

### Free-threaded CPython

CPython now carries trial support for a free-threaded mode in which the [global interpreter lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) (GIL) is turned off. Because this is experimental, it stays disabled by default. Running free-threaded requires a separate executable, generally named `python3.13t` or `python3.13t.exe`. Pre-built binaries flagged as *free-threaded* can be set up via the official [Windows](https://docs.python.org/3.14/using/windows.html#install-freethreaded-windows) and [macOS](https://docs.python.org/3.14/using/mac.html#install-freethreaded-macos) installers, or you can compile CPython from source using the [`--disable-gil`](https://docs.python.org/3.14/using/configure.html#cmdoption-disable-gil) option.

With free-threaded execution you can fully exploit the available compute by running threads at the same time across the CPU cores you have. Not every program gains from this for free, but software built with threading in view will go faster on multi-core machines. **The free-threaded mode is experimental** and effort continues to refine it: anticipate certain bugs together with a notable slowdown on single-threaded workloads. Free-threaded CPython builds can optionally run with the GIL switched on at runtime by way of the [`PYTHON_GIL`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_GIL) environment variable or the [`-X gil=1`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command-line option.

To find out whether your current interpreter has free-threading, note that [`python -VV`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-V) and [`sys.version`](https://docs.python.org/3.14/library/sys.html#sys.version) include ?experimental free-threading build?. The new `sys._is_gil_enabled()` function lets you verify whether the GIL is genuinely off in the active process.

C-API extension modules have to be compiled expressly against the free-threaded build. Extensions that can run with the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) off ought to use the [`Py_mod_gil`](https://docs.python.org/3.14/c-api/module.html#c.Py_mod_gil) slot. Extensions relying on single-phase init ought to call [`PyUnstable_Module_SetGIL()`](https://docs.python.org/3.14/c-api/module.html#c.PyUnstable_Module_SetGIL) to declare whether they can run with the GIL off. Importing C extensions that omit these mechanisms forces the GIL back on, unless the GIL was deliberately switched off through the [`PYTHON_GIL`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_GIL) environment variable or the [`-X gil=0`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) option. Installing packages with C extensions on the free-threaded build calls for pip 24.1 or later.

A wide community of people contributing to Python and to third-party projects helped test and turn on free-threading support, making this work feasible across many individuals and organizations.

> Among the notable contributors are: Sam Gross, Ken Jin, Donghee Na, Itamar Oren, Matt Page, Brett Simmers, Dino Viehland, Carl Meyer, Nathan Goldbaum, Ralf Gommers, Lysandros Nikolaou, and many others.

A number of these contributors work at Meta, which has supplied considerable engineering resources toward this effort.

See also

[**PEP 703**](https://peps.python.org/pep-0703/) ?Making the Global Interpreter Lock Optional in CPython? lays out the rationale and details around this work.

[Porting Extension Modules to Support Free-Threading](https://py-free-threading.github.io/porting/): A community-maintained porting guide for extension authors.

[Subject index](INDEX.md) · [Previous source section](improved-error-messages.md) · [Next source section](an-experimental-just-in-time-compiler.md) · [Release/subject declaration](summary-release-highlights.md)
