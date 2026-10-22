# What's New In Python 3.11 / Build Changes — tkinter

### Build Changes

- CPython now carries [**PEP 11**](https://peps.python.org/pep-0011/) [**Tier 3 support**](https://peps.python.org/pep-0011/#tier-3) covering cross compilation toward the [WebAssembly](https://webassembly.org/) targets [Emscripten](https://emscripten.org/) (`wasm32-unknown-emscripten`, i.e. Python in the browser) plus [WebAssembly System Interface (WASI)](https://wasi.dev/) (`wasm32-unknown-wasi`). Earlier projects such as [Pyodide](https://pyodide.org/) inspired this work. These targets supply only a narrow slice of POSIX APIs; Python standard library capabilities and modules tied to networking, processes, threading, signals, mmap, and users/groups are missing or fail to operate.

> (Emscripten contributed by Christian Heimes and Ethan Smith in [gh-84461](https://github.com/python/cpython/issues/84461) and WASI contributed by Christian Heimes in [gh-90473](https://github.com/python/cpython/issues/90473); platforms promoted in [gh-95085](https://github.com/python/cpython/issues/95085))

- To build CPython you now need:

  - A [C11](https://en.cppreference.com/w/c/11) compiler together with its standard library. [Optional C11 features](https://en.wikipedia.org/wiki/C11_(C_standard_revision)#Optional_features) are not needed. (Contributed by Victor Stinner in [bpo-46656](https://bugs.python.org/issue?@action=redirect&bpo=46656), [bpo-45440](https://bugs.python.org/issue?@action=redirect&bpo=45440) and [bpo-46640](https://bugs.python.org/issue?@action=redirect&bpo=46640).)

  - Backing for [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) floating-point numbers. (Contributed by Victor Stinner in [bpo-46917](https://bugs.python.org/issue?@action=redirect&bpo=46917).)

- The `Py_NO_NAN` macro is gone. Because CPython now mandates IEEE 754 floats, NaN values can always be relied upon. (Contributed by Victor Stinner in [bpo-46656](https://bugs.python.org/issue?@action=redirect&bpo=46656).)

- The [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) package now demands [Tcl/Tk](https://www.tcl.tk) at version 8.5.12 or above. (Contributed by Serhiy Storchaka in [bpo-46996](https://bugs.python.org/issue?@action=redirect&bpo=46996).)

- For the majority of stdlib extension modules, the build dependencies along with compiler flags and linker flags are now figured out by **configure**. The libffi, libnsl, libsqlite3, zlib, bzip2, liblzma, libcrypt, Tcl/Tk, and uuid flags get detected through [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/) (where it is present). [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) now relies on a pkg-config command to discover where the [Tcl/Tk](https://www.tcl.tk) development headers plus libraries reside. (Contributed by Christian Heimes and Erlend Egeberg Aasland in [bpo-45847](https://bugs.python.org/issue?@action=redirect&bpo=45847), [bpo-45747](https://bugs.python.org/issue?@action=redirect&bpo=45747), and [bpo-45763](https://bugs.python.org/issue?@action=redirect&bpo=45763).)

- libpython no longer links against libcrypt. (Contributed by Mike Gilbert in [bpo-45433](https://bugs.python.org/issue?@action=redirect&bpo=45433).)

- CPython is now buildable using the [ThinLTO](https://clang.llvm.org/docs/ThinLTO.html) option by handing `thin` to [`--with-lto`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-lto), i.e. `--with-lto=thin`. (Contributed by Donghee Na and Brett Holman in [bpo-44340](https://bugs.python.org/issue?@action=redirect&bpo=44340).)

- Freelists for object structs are now able to be turned off. A fresh **configure** option `--without-freelists` lets you switch off every freelist apart from the empty tuple singleton. (Contributed by Christian Heimes in [bpo-45522](https://bugs.python.org/issue?@action=redirect&bpo=45522).)

- `Modules/Setup` together with `Modules/makesetup` were refined and tidied up. Extension modules can now be assembled via `makesetup`. Apart from a handful of test modules, all of them can be linked statically into a primary binary or library. (Contributed by Brett Cannon and Christian Heimes in [bpo-45548](https://bugs.python.org/issue?@action=redirect&bpo=45548), [bpo-45570](https://bugs.python.org/issue?@action=redirect&bpo=45570), [bpo-45571](https://bugs.python.org/issue?@action=redirect&bpo=45571), and [bpo-43974](https://bugs.python.org/issue?@action=redirect&bpo=43974).)

Note

Set the environment variables `TCLTK_CFLAGS` and `TCLTK_LIBS` to point manually at where the Tcl/Tk headers and libraries live. The **configure** options `--with-tcltk-includes` and `--with-tcltk-libs` are gone.

Under RHEL 7 and CentOS 7 the development packages ship neither `tcl.pc` nor `tk.pc`; for those, use `TCLTK_LIBS="-ltk8.5 -ltkstub8.5 -ltcl8.5"`. The directory `Misc/rhel7` holds `.pc` files plus directions for building Python against the Tcl/Tk and OpenSSL shipped by RHEL 7 and CentOS 7.

- CPython will from now on default to 30-bit digits for its Python [`int`](https://docs.python.org/3.14/library/functions.html#int) implementation. Formerly the default chose 30-bit digits on platforms where `SIZEOF_VOID_P >= 8`, falling back to 15-bit digits elsewhere. You can still ask explicitly for 15-bit digits through either the [`--enable-big-digits`](https://docs.python.org/3.14/using/configure.html#cmdoption-enable-big-digits) option passed to the configure script or (on Windows) the `PYLONG_BITS_IN_DIGIT` variable inside `PC/pyconfig.h`, although that option could disappear in some future release. (Contributed by Mark Dickinson in [bpo-45569](https://bugs.python.org/issue?@action=redirect&bpo=45569).)

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-11.md) · [Next source section](c-api-changes-new-features.md) · [Release/subject declaration](summary-release-highlights.md)
