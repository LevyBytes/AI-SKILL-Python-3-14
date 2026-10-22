# urllib.parse: `urllib.parse.urljoin()`, `urllib.parse.urldefrag()`, `urllib.parse.unwrap()`

urllib.parse.urljoin(*base*, *url*, *allow_fragments=True*)

Build a full (“absolute”) URL by merging a “base URL” (*base*) with a second URL (*url*). Loosely speaking, it borrows pieces of the base URL—particularly the addressing scheme, the network location, and (part of) the path—to supply whatever the relative URL is missing. As an illustration:

```python
>>> from urllib.parse import urljoin
>>> urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html')
'http://www.cwi.nl/%7Eguido/FAQ.html'

```

The *allow_fragments* argument carries the same meaning and default it has for `urlsplit()`.

Note

When *url* is an absolute URL (one beginning with `//` or `scheme://`), the *url*’s hostname and/or scheme end up in the result. As an illustration:

```pycon
>>> urljoin('http://www.cwi.nl/%7Eguido/Python.html',
...         '//www.python.org/%7Eguido')
'http://www.python.org/%7Eguido'

```

To avoid that behavior, run the *url* through `urlsplit()` and `urlunsplit()` first, stripping out any *scheme* and *netloc* pieces.

Warning

Since an absolute URL can be handed in as the `url` parameter, calling `urljoin` with an attacker-controlled `url` is generally **not secure**. Take `urljoin("https://website.com/users/", username)`: should `username` be able to hold an absolute URL, what `urljoin` returns will be that absolute URL.

Changed in version 3.5: The behavior was updated to align with the semantics laid out in [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html).

 urllib.parse.urldefrag(*url*)

When *url* holds a fragment identifier, give back a revised copy of *url* without that fragment identifier, plus the fragment identifier on its own as a separate string. When *url* has no fragment identifier, give back *url* untouched along with an empty string.

What comes back is a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple); its elements are reachable by index or via named attributes:

| Attribute | Index | Value | Value if not present |
| --- | --- | --- | --- |
| `url` | 0 | URL with no fragment | empty string |
| `fragment` | 1 | Fragment identifier | empty string |

The Structured Parse Results section has more detail on the result object.

Changed in version 3.2: The result became a structured object instead of a plain 2-tuple.

 urllib.parse.unwrap(*url*)

Pull the url out of a wrapped URL (that is, a string laid out as `<URL:scheme://host/path>`, `<scheme://host/path>`, `URL:scheme://host/path`, or `scheme://host/path`). When *url* is not a wrapped URL, it comes back unchanged.

[Subject index](INDEX.md) · [Previous](urllib-parse-parse-qs-to-urllib-parse-urlunparse.md) · [Continue](url-parsing-security.md) · [Owning module, declaration or section: urllib.parse](urllib-parse-parse-urls-into-components.md) · [Owning module, declaration or section: URL Parsing](url-parsing.md)
