# What's new in Python 3.14 / urllib — urllib.error, urllib.request

### urllib

- Strengthen the HTTP digest authentication algorithm for [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request) by adding SHA-256 digest authentication per [**RFC 7616**](https://datatracker.ietf.org/doc/html/rfc7616.html). (Contributed by Calvin Bui in [gh-128193](https://github.com/python/cpython/issues/128193).)

- Better usability and standards conformance while parsing and producing `file:` URLs.

Within [`url2pathname()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.url2pathname):

  - Take a full URL whenever the fresh *require_scheme* argument is turned on.

  - Drop the URL authority should it equal the local hostname.

  - Drop the URL authority should it resolve to a local IP address once the fresh *resolve_host* argument is turned on.

  - Drop the URL query plus fragment portions.

  - Raise [`URLError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.URLError) whenever a URL authority is not local, with the exception of Windows, where a UNC path is returned as previously.

Within [`pathname2url()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.pathname2url):

  - Hand back a full URL whenever the fresh *add_scheme* argument is turned on.

  - Add an empty URL authority whenever a path opens with a slash. As an example, the path `/etc/hosts` becomes the URL `///etc/hosts`.

Under Windows, drive letters no longer get uppercased, and `:` characters that do not follow a drive letter no longer trigger an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception.

(Contributed by Barney Gale in [gh-125866](https://github.com/python/cpython/issues/125866).)

### urllib

- The `Quoter` class is gone from [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse); it had carried a deprecation since Python 3.11. (Contributed by Nikita Sobolev in [gh-118827](https://github.com/python/cpython/issues/118827).)

- The `URLopener` plus `FancyURLopener` classes are gone from [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request); both had been deprecated as far back as Python 3.3.

Swap `myopener.open()` for [`urlopen()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.urlopen). Swap `myopener.retrieve()` for [`urlretrieve()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.urlretrieve). Where you tailored the opener classes, instead feed custom handlers into [`build_opener()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.build_opener). (Contributed by Barney Gale in [gh-84850](https://github.com/python/cpython/issues/84850).)

[Subject index](INDEX.md) · [Previous source section](unittest.md) · [Next source section](uuid.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](sqlite3.md) · [Next source section](new-deprecations.md)
