# urllib.parse — URL Parsing — Signature and initial contract

urllib.parse.urlsplit(*urlstring*, *scheme=None*, *allow_fragments=True*)

Split a URL into five pieces, yielding a 5-item [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) `SplitResult` or `SplitResultBytes`. This mirrors a URL’s overall layout: `scheme://netloc/path?query#fragment`. Every tuple element is a string and may be empty. The pieces themselves are left whole (the network location, for instance, stays as one string), and % escapes go unexpanded. None of the delimiters shown above appear in the result, with the exception of a leading slash in the *path* piece, which stays when present. As an illustration:

```pycon
>>> from urllib.parse import urlsplit
>>> urlsplit("scheme://netloc/path?query#fragment")
SplitResult(scheme='scheme', netloc='netloc', path='/path',
            query='query', fragment='fragment')
>>> o = urlsplit("http://docs.python.org:80/3/library/urllib.parse.html?"
...              "highlight=params#url-parsing")
>>> o
SplitResult(scheme='http', netloc='docs.python.org:80',
            path='/3/library/urllib.parse.html',
            query='highlight=params', fragment='url-parsing')
>>> o.scheme
'http'
>>> o.netloc
'docs.python.org:80'
>>> o.hostname
'docs.python.org'
>>> o.port
80
>>> o._replace(fragment="").geturl()
'http://docs.python.org:80/3/library/urllib.parse.html?highlight=params'

```

In keeping with the syntax rules of [**RFC 1808**](https://datatracker.ietf.org/doc/html/rfc1808.html), `urlsplit()` treats something as a netloc only when ‘//’ properly introduces it. Failing that, the input is assumed to be a relative URL and is therefore taken to begin with a path piece.

```pycon
>>> from urllib.parse import urlsplit
>>> urlsplit('//www.cwi.nl:80/%7Eguido/Python.html')
SplitResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
            query='', fragment='')
>>> urlsplit('www.cwi.nl/%7Eguido/Python.html')
SplitResult(scheme='', netloc='', path='www.cwi.nl/%7Eguido/Python.html',
            query='', fragment='')
>>> urlsplit('help/Python.html')
SplitResult(scheme='', netloc='', path='help/Python.html',
            query='', fragment='')

```

The *scheme* argument supplies the default addressing scheme, applied only when the URL itself names none. It must match the type (text or bytes) of *urlstring*, though the default of `''` is always permitted and is converted to `b''` automatically where that fits.

When the *allow_fragments* argument is false, fragment identifiers go unrecognized. They are instead folded into the path, parameters, or query piece, and the returned `fragment` becomes the empty string.

What comes back is a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple), so its elements are reachable either by index or via named attributes, namely:

| Attribute | Index | Value | Value if not present |
| --- | --- | --- | --- |
| `scheme` | 0 | URL scheme specifier | *scheme* parameter |
| `netloc` | 1 | Network location part | empty string |
| `path` | 2 | Hierarchical path | empty string |
| `query` | 3 | Query component | empty string |
| `fragment` | 4 | Fragment identifier | empty string |
| `username` |  | User name | `None` |
| `password` |  | Password | `None` |
| `hostname` |  | Host name (lower case) | `None` |
| `port` |  | Port number as integer, if present | `None` |

Accessing the `port` attribute raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when the URL holds an invalid port. The Structured Parse Results section has more detail on the result object.

A `netloc` attribute containing unmatched square brackets raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

If characters in the `netloc` attribute decompose under NFKC normalization (the form the IDNA encoding relies on) into any of `/`, `?`, `#`, `@`, or `:`, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. Decomposing the URL prior to parsing avoids the error.

In line with parts of the [WHATWG spec](https://url.spec.whatwg.org/#concept-basic-url-parser) that revise [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html), leading C0 control and space characters are trimmed off the URL. The `\n`, `\r`, and tab `\t` characters get removed from the URL wherever they occur.

Like every named tuple, this subclass carries a handful of extra methods and attributes worth knowing. `_replace()` is one such method. Calling `_replace()` yields a fresh `SplitResult` object with the named fields swapped for new values.

```pycon
>>> from urllib.parse import urlsplit
>>> u = urlsplit('//www.cwi.nl:80/%7Eguido/Python.html')
>>> u
SplitResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
            query='', fragment='')
>>> u._replace(scheme='http')
SplitResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
            query='', fragment='')

```

[Subject index](INDEX.md) · [Previous](url-parsing.md) · [Continue](url-parsing-contract-warning.md) · [Owning module, declaration or section: urllib.parse](urllib-parse-parse-urls-into-components.md) · [Owning module, declaration or section: URL Parsing](url-parsing.md)
