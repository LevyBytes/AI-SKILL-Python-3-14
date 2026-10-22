# Python 3.13.0 alpha 3 / build / files and paths

[gh-114013](https://github.com/python/cpython/issues/114013): Adjust `Tools/wasm/wasi.py` so the path to `python.wasm` is left out of `HOSTRUNNER`. That environment variable should describe only how the WASI host runs, with `python.wasm` plus its flags tacked on after the `HOSTRUNNER`. The fix gets `make test` working.

[gh-112305](https://github.com/python/cpython/issues/112305): The `check-clean-src` step on out of tree builds was fixed so it spots stray `$(srcdir)/Python/frozen_modules/*.h` files and points to the right source tree cleanup steps for restoring a working build.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
