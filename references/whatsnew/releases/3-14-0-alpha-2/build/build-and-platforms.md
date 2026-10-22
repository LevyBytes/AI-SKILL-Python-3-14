# Python 3.14.0 alpha 2 / build / build and platforms

[gh-126691](https://github.com/python/cpython/issues/126691): The `--with-emscripten-target` configure flag is gone. We merged the `node` and `browser` options, and one build now serves regardless of which target runtime is used.

[gh-124932](https://github.com/python/cpython/issues/124932): Cross builds may now use an install `prefix` that differs from the `host_prefix` consumed by `getpath.py`. For Emscripten this defaults to `/`, while on the remaining platforms the default carries over the previous behavior.

[gh-125946](https://github.com/python/cpython/issues/125946): Android support now begins at version 7.0 (API level 24) as the minimum.

[gh-125940](https://github.com/python/cpython/issues/125940): Building for Android now handles [16 KB page sizes](https://developer.android.com/guide/practices/page-sizes).

[gh-115382](https://github.com/python/cpython/issues/115382): Repair cross compile failures that appeared once the host and target SOABIs were identical.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
