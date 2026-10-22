# urllib.request: `urllib.request.Request`

*class *urllib.request.Request(*url*, *data=None*, *headers={}*, *origin_req_host=None*, *unverifiable=False*, *method=None*)

An abstraction over a URL request is what this class represents.

*url* ought to be a string holding a valid, correctly encoded URL.

*data* must be an object carrying extra data to send to the server, or `None` when none is required. At present only HTTP requests make use of *data*. The object types accepted include bytes, file-like objects, and iterables of bytes-like objects. When neither a `Content-Length` nor a `Transfer-Encoding` header field is supplied, `HTTPHandler` will set these headers based on the *data* type. `Content-Length` applies when sending bytes objects, whereas `Transfer-Encoding: chunked` as laid out in [**RFC 7230**](https://datatracker.ietf.org/doc/html/rfc7230.html), Section 3.3.1 applies when sending files and other iterables.

For an HTTP POST request method, *data* ought to be a buffer in the standard *application/x-www-form-urlencoded* format. The [`urllib.parse.urlencode()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlencode) function accepts a mapping or a sequence of 2-tuples and produces an ASCII string in this format. Encode it to bytes before passing it as the *data* parameter.

*headers* ought to be a dictionary, and is handled as though `add_header()` had been invoked with each key and value as arguments. A common use is to "spoof" the `User-Agent` header value, which a browser sends to identify itself — certain HTTP servers accept requests only from common browsers and reject scripts. For instance, Mozilla Firefox might present itself as `"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"`, whereas [`urllib`](https://docs.python.org/3.14/library/urllib.html#module-urllib)'s default user agent string is `"Python-urllib/2.6"` (on Python 2.6). Every header key goes out in camel case.

A suitable `Content-Type` header ought to accompany a present *data* argument. When this header is absent and *data* is not `None`, `Content-Type: application/x-www-form-urlencoded` is added as the default.

The remaining two arguments matter only for the proper handling of third-party HTTP cookies:

*origin_req_host* ought to be the request-host of the origin transaction, as specified by [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html). Its default is `http.cookiejar.request_host(self)`. This is the host name or IP address of the user-initiated original request. As an example, when the request retrieves an image embedded in an HTML document, this ought to be the request-host belonging to the request that fetched the page containing that image.

*unverifiable* ought to convey whether the request is unverifiable, as specified by [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html). Its default is `False`. A request counts as unverifiable when the user had no opportunity to approve its URL. As an example, when the request fetches an image inside an HTML document and the user had no chance to approve fetching that image automatically, this should be true.

*method* ought to be a string naming the HTTP request method to apply (for example `'HEAD'`). When supplied, its value lands in the `method` attribute and is consumed by `get_method()`. The default is `'GET'` when *data* is `None`, otherwise `'POST'`. A subclass may declare a different default method by setting the `method` attribute within the class itself.

Note

The request will misbehave when the data object cannot supply its content more than once (such as a file or a single-use iterable) and the request is retried because of HTTP redirects or authentication. The *data* goes to the HTTP server immediately following the headers. The library offers no support for a 100-continue expectation.

Changed in version 3.3: `Request.method` argument is added to the Request class.

Changed in version 3.4: The default `Request.method` can be declared at the class level.

Changed in version 3.6: No error is raised when the `Content-Length` is absent and *data* is neither `None` nor a bytes object. Chunked transfer encoding is used as the fallback instead.

[Subject index](INDEX.md) · [Previous](urllib-request-pathname2url-to-urllib-request-getproxies.md) · [Continue](urllib-request-openerdirector-class.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)
