# Python 3.14.0 alpha 1 / library / urllib parse

[gh-85110](https://github.com/python/cpython/issues/85110): Keep the relative path intact for a netloc-less URL within [`urllib.parse.urlunsplit()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlunsplit) plus [`urllib.parse.urlunparse()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlunparse).

[gh-67693](https://github.com/python/cpython/issues/67693): A fix lands for [`urllib.parse.urlunparse()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlunparse) and [`urllib.parse.urlunsplit()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlunsplit) handling URIs whose path opens with several slashes and which carry no authority. The work builds on a patch from Ashwin Ramaswami.

[gh-76960](https://github.com/python/cpython/issues/76960): Repairs [`urllib.parse.urljoin()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urljoin) and [`urllib.parse.urldefrag()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urldefrag) for URIs that hold empty components. As an example, calling `urljoin()` with the relative reference `?` now produces an empty query and strips the fragment. Empty components (authority, params, query, fragment) are kept in `urljoin()`. Empty components (authority, params, query) are kept in `urldefrag()`.

[gh-118827](https://github.com/python/cpython/issues/118827): The deprecated `Quoter` class is now dropped from [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse); it had been emitting a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) ever since Python 3.11. Nikita Sobolev supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
