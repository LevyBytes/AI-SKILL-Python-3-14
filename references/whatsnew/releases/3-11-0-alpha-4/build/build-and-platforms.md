# Python 3.11.0 alpha 4 / build / build and platforms

[bpo-44133](https://bugs.python.org/issue?@action=redirect&bpo=44133): Whenever Python is configured using [`--without-static-libpython`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-static-libpython), the build no longer produces the Python static library (libpython.a). Victor Stinner wrote the patch.

[bpo-40280](https://bugs.python.org/issue?@action=redirect&bpo=40280): The `configure` script gains a new option, `--with-emscripten-target`, for choosing browser or node as the Emscripten build target.

[bpo-46315](https://bugs.python.org/issue?@action=redirect&bpo=46315): Added together with corrected `#ifdef HAVE_FEATURE` checks guarding functionality absent on the WASI platform.

[bpo-46263](https://bugs.python.org/issue?@action=redirect&bpo=46263): On FreeBSD platforms, `configure` has stopped setting `MULTIARCH`.

[bpo-46106](https://bugs.python.org/issue?@action=redirect&bpo=46106): Bumped OpenSSL to 1.1.1m across Windows builds, macOS installer builds, and CI. Kumar Aditya wrote the patch.

[bpo-46088](https://bugs.python.org/issue?@action=redirect&bpo=46088): Detect or install the bootstrap Python runtime automatically while building from Visual Studio.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
