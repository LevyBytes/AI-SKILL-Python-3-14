# Python 3.11.0 alpha 3 / build / build and platforms

[bpo-45950](https://bugs.python.org/issue?@action=redirect&bpo=45950): For freezing and deepfreezing, the build system once more relies on a **_bootstrap_python** interpreter. To accelerate the build process, the build tools **_bootstrap_python** and **_freeze_module** are no longer built with LTO.

[bpo-40280](https://bugs.python.org/issue?@action=redirect&bpo=40280): `configure` now probes for the functions `fork1, getegid, geteuid, getgid, getppid, getuid, opendir, pipe, system, wait, ttyname`.

[bpo-40280](https://bugs.python.org/issue?@action=redirect&bpo=40280): For cross building, `configure` now permits the machine `wasm32` or `wasm64` together with the OS `wasi` or `emscripten`, for example `wasm32-unknown-emscripten`, `wasm32-wasi`, or `wasm32-unknown-wasi`.

[bpo-45873](https://bugs.python.org/issue?@action=redirect&bpo=45873): Eliminate the `_bootstrap_python` build step. The deepfreeze.py script now runs through `$(PYTHON_FOR_REGEN)`, which may be Python 3.7 or newer (3.8 or newer on Windows).

[bpo-45723](https://bugs.python.org/issue?@action=redirect&bpo=45723): A fresh **configure** option, `--with-pkg-config`, lets you turn off or mandate pkg-config.

[bpo-45743](https://bugs.python.org/issue?@action=redirect&bpo=45743): The build system on macOS stopped handing `search_paths_first` to the linker. That flag has served as the default ever since Xcode 4 / macOS 10.6.

[bpo-45723](https://bugs.python.org/issue?@action=redirect&bpo=45723): Compatibility with autoconf 2.71 now extends to `configure.ac`. The deprecated `STDC_HEADERS` and `AC_HEADER_TIME` checks were dropped.

[bpo-45723](https://bugs.python.org/issue?@action=redirect&bpo=45723): A warning is now emitted by `configure` whenever pkg-config cannot be found.

[bpo-45731](https://bugs.python.org/issue?@action=redirect&bpo=45731): A fresh `PY_SQLITE_ENABLE_LOAD_EXTENSION` macro now drives `configure --enable-loadable-sqlite-extensions`, replacing logic that used to live in setup.py.

[bpo-45723](https://bugs.python.org/issue?@action=redirect&bpo=45723): To trim and accelerate configure runs, configure.ac now leans on custom helper macros plus `AC_CACHE_CHECK`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
