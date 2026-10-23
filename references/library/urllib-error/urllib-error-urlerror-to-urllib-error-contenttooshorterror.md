# urllib.error`urllib.error` - Exception classes raised by urllib.request

## urllib.error - Exception classes raised by urllib.request

### `urllib.error` - Exception classes raised by urllib.request

**Source code:** [Lib/urllib/error.py](https://github.com/python/cpython/tree/3.14/Lib/urllib/error.py)

---

Exception classes for the exceptions thrown by [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request) are defined within the `urllib.error` module. Its base exception class is `URLError`.

Where suitable, `urllib.error` raises the exceptions listed below:

 *exception *urllib.error.URLError

Whenever the handlers hit trouble, they throw this exception (or one derived from it). It descends from [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 reason

What caused this error. This may take the form of a message string or some other exception instance.

Changed in version 3.3: Formerly `URLError` derived from [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError), a name that now stands as an alias for [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 *exception *urllib.error.HTTPError(*url*, *code*, *msg*, *hdrs*, *fp*)

Even though it is an exception (one that subclasses `URLError`), an `HTTPError` can equally serve as an ordinary, non-exceptional file-like return value — precisely what [`urlopen()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.urlopen) hands back. That proves handy when you deal with unusual HTTP errors, authentication challenges among them.

 url

Holds the URL of the request. This stands as an alias for the *filename* attribute.

 code

An HTTP status code per the definition in [**RFC 2616**](https://datatracker.ietf.org/doc/html/rfc2616.html). That number lines up with an entry in the dictionary of codes held by [`http.server.BaseHTTPRequestHandler.responses`](https://docs.python.org/3.14/library/http.server.html#http.server.BaseHTTPRequestHandler.responses).

 reason

Typically a string that spells out why this error occurred. It serves as an alias for the *msg* attribute.

 headers

The HTTP response headers belonging to the HTTP request that triggered the `HTTPError`. It acts as an alias for the *hdrs* attribute.

Added in version 3.4.

 fp

A file-like object from which the body of the HTTP error may be read.

 *exception *urllib.error.ContentTooShortError(*msg*, *content*)

This exception gets thrown once the [`urlretrieve()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.urlretrieve) function notices that the volume of downloaded data falls short of what was anticipated (the figure stated by the *Content-Length* header).

 content

The data that was downloaded (and presumably cut short).

[Subject index](INDEX.md) · [Continue](../urllib/urllib-url-handling-modules.md)
