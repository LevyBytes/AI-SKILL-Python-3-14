# Python 3.11.0 alpha 7 / build / build and platforms

[bpo-40280](https://bugs.python.org/issue?@action=redirect&bpo=40280): A configure option [`--enable-wasm-dynamic-linking`](https://docs.python.org/3.14/using/configure.html#cmdoption-enable-wasm-dynamic-linking) is added to switch on `dlopen` plus MAIN_MODULE / SIDE_MODULE for `wasm32-emscripten`.

[bpo-47032](https://bugs.python.org/issue?@action=redirect&bpo=47032): Windows install builds now fail properly, returning a non-zero exit code, whenever some portion of the build fails.

[bpo-47024](https://bugs.python.org/issue?@action=redirect&bpo=47024): OpenSSL is bumped to 1.1.1n for the macOS installers as well as every Windows build.

[bpo-46973](https://bugs.python.org/issue?@action=redirect&bpo=46973): A `regen-configure` make target is added that regenerates the configure script using Christian's container image `quay.io/tiran/cpython_autoconf:269`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
