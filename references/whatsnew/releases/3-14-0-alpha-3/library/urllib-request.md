# Python 3.14.0 alpha 3 / library / urllib request

[gh-85168](https://github.com/python/cpython/issues/85168): Resolve a case under which [`urllib.request.url2pathname()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.url2pathname) plus [`pathname2url()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.pathname2url) always reached for UTF-8 while quoting and unquoting file URIs. The pair now defers to the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler).

[gh-126601](https://github.com/python/cpython/issues/126601): Resolve a case under which [`urllib.request.pathname2url()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.pathname2url) threw an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) for a Windows path bearing a colon that did not trail a drive letter, for instance ahead of an NTFS alternate data stream.

[gh-127217](https://github.com/python/cpython/issues/127217): Correct [`urllib.request.pathname2url()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.pathname2url) handling of paths that open with several slashes on Posix.

[gh-125866](https://github.com/python/cpython/issues/125866): [`urllib.request.pathname2url()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.pathname2url) now appends an empty authority while building a URL for any path leading with exactly one slash. To illustrate, the path `/etc/hosts` becomes the scheme-less URL `///etc/hosts`. Because of this, authority-free URLs end up produced solely for relative paths.

[gh-125866](https://github.com/python/cpython/issues/125866): [`urllib.request.pathname2url()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.pathname2url) together with [`url2pathname()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.url2pathname) stops uppercasing Windows drive letters.

[gh-127078](https://github.com/python/cpython/issues/127078): Resolve a case under which [`urllib.request.url2pathname()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.url2pathname) neglected to drop a spare slash ahead of a UNC drive within the URL path on Windows.

[gh-126766](https://github.com/python/cpython/issues/126766): Resolve a case under which [`urllib.request.url2pathname()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.url2pathname) neglected to drop any "localhost" authority appearing in the URL.

[gh-127090](https://github.com/python/cpython/issues/127090): Correct the [`urllib.response.addinfourl.url`](https://docs.python.org/3.14/library/urllib.request.html#urllib.response.addinfourl.url) value for `file:` URLs conveying relative paths along with absolute Windows paths. The canonical URL that [`urllib.request.pathname2url()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.pathname2url) emits is now what gets used.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
