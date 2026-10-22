# Python 3.13.0 alpha 1 / library / files and paths

[gh-103631](https://github.com/python/cpython/issues/103631): Repaired `pathlib.PurePosixPath(pathlib.PureWindowsPath(...))` so it again converts path separators, restoring the behavior seen in 3.11.

[gh-103200](https://github.com/python/cpython/issues/103200): Adjusted the cache-repopulation behavior of zipimport.invalidate_caches(). Repopulation now occurs when files get fetched with an invalid cache, instead of at the moment the cache becomes invalidated.

[gh-110038](https://github.com/python/cpython/issues/110038): Corrected a problem whereby `KqueueSelector.select()` failed to surface every ready event in certain situations where a file descriptor had been registered for reading as well as writing.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
