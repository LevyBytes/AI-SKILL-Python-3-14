# urllib.request: `urllib.request.pathname2url()`, `urllib.request.url2pathname()`, `urllib.request.getproxies()`

urllib.request.pathname2url(*path*, ***, *add_scheme=False*)

Turn the supplied local path into a `file:` URL. The path is encoded by this function via the [`quote()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.quote) function.

When *add_scheme* is false (its default), the result leaves off the `file:` scheme prefix. Setting *add_scheme* to true yields a complete URL.

Here the function is demonstrated on Windows:

```python
>>> from urllib.request import pathname2url
>>> path = 'C:\\Program Files'
>>> pathname2url(path, add_scheme=True)
'file:///C:/Program%20Files'

```

Changed in version 3.14: On Windows, a drive letter is no longer uppercased, and a `:` character that does not follow a drive letter no longer triggers an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception.

Changed in version 3.14: A path that starts with a slash now yields a URL carrying an authority section. As an illustration, the path `/etc/hosts` becomes the URL `///etc/hosts`.

Changed in version 3.14: The *add_scheme* parameter was added.

 urllib.request.url2pathname(*url*, ***, *require_scheme=False*, *resolve_host=False*)

Turn the supplied `file:` URL into a local path. The URL is decoded by this function via [`unquote()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.unquote).

When *require_scheme* is false (its default), the supplied value ought to omit a `file:` scheme prefix. When *require_scheme* is true, the supplied value ought to carry the prefix; otherwise a [`URLError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.URLError) is raised.

The URL authority is dropped when it is empty, `localhost`, or the local hostname. Otherwise, when *resolve_host* is true, the authority is resolved through [`socket.gethostbyname()`](https://docs.python.org/3.14/library/socket.html#socket.gethostbyname) and dropped if it lines up with a local IP address (per [**RFC 8089 ??3**](https://datatracker.ietf.org/doc/html/rfc8089.html#section-3)). Should the authority remain unhandled, a UNC path is returned on Windows, while a [`URLError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.URLError) is raised on other platforms.

Here the function is demonstrated on Windows:

```python
>>> from urllib.request import url2pathname
>>> url = 'file:///C:/Program%20Files'
>>> url2pathname(url, require_scheme=True)
'C:\\Program Files'

```

Changed in version 3.14: On Windows, a drive letter is no longer forced to uppercase, and a `:` character not positioned after a drive letter no longer raises an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception.

Changed in version 3.14: When the URL authority matches the local hostname it is now dropped. Otherwise, provided the authority is neither empty nor `localhost`, a UNC path comes back on Windows (as it did before), while a [`URLError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.URLError) is raised elsewhere.

Changed in version 3.14: Any URL query and fragment components, when present, are now dropped.

Changed in version 3.14: The *require_scheme* and *resolve_host* parameters were added.

 urllib.request.getproxies()

A dictionary mapping each scheme to a proxy server URL is what this helper function returns. Across every operating system it first inspects the environment for variables named `<scheme>_proxy`, doing so case-insensitively, and when none is found it turns to proxy details from System Configuration on macOS and the Systems Registry on Windows. Should both a lowercase and an uppercase environment variable be present (and conflict), the lowercase one wins.

Note

When the `REQUEST_METHOD` environment variable is set — typically a sign that your script runs inside a CGI environment — the `HTTP_PROXY` environment variable (uppercase `_PROXY`) is disregarded. The reason is that a client can inject that variable through the "Proxy:" HTTP header. Should you require an HTTP proxy within a CGI environment, either invoke `ProxyHandler` explicitly or ensure the variable name is lowercase (or at minimum the `_proxy` suffix).

These classes are provided:

[Subject index](INDEX.md) · [Previous](urllib-request-urlopen-to-urllib-request-build-opener.md) · [Continue](urllib-request-request-class.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)
