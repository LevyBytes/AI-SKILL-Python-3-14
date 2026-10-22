# urllib.request — HTTPRedirectHandler Objects

### HTTPRedirectHandler Objects

Note

Certain HTTP redirections call for the client code in this module to take action. When that happens, [`HTTPError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.HTTPError) is raised. Consult [**RFC 2616**](https://datatracker.ietf.org/doc/html/rfc2616.html) for the exact meaning of each redirection code.

As a security measure, an [`HTTPError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.HTTPError) exception gets raised whenever the HTTPRedirectHandler receives a redirected URL that is not an HTTP, HTTPS or FTP URL.

 HTTPRedirectHandler.redirect_request(*req*, *fp*, *code*, *msg*, *hdrs*, *newurl*)

Give back a `Request` or `None` as the answer to a redirect. The default implementations of the `http_error_30*()` methods invoke this whenever the server sends back a redirection. When a redirection ought to happen, give back a fresh `Request` so that `http_error_30*()` can carry out the redirect to *newurl*. Otherwise, raise [`HTTPError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.HTTPError) if no other handler ought to attempt this URL, or give back `None` when you cannot but some other handler might.

Note

This method's default implementation does not adhere strictly to [**RFC 2616**](https://datatracker.ietf.org/doc/html/rfc2616.html), which states that 301 and 302 responses to `POST` requests are not to be redirected automatically without the user confirming. Out in the real world, browsers do permit these responses to be redirected automatically, switching the POST over to a `GET`, and the default implementation mirrors that behavior.

 HTTPRedirectHandler.http_error_301(*req*, *fp*, *code*, *msg*, *hdrs*)

Redirect to the `Location:` or `URI:` URL. The parent `OpenerDirector` invokes this method on receiving an HTTP ‘moved permanently’ response.

 HTTPRedirectHandler.http_error_302(*req*, *fp*, *code*, *msg*, *hdrs*)

The same as `http_error_301()`, but called for the ‘found’ response.

 HTTPRedirectHandler.http_error_303(*req*, *fp*, *code*, *msg*, *hdrs*)

The same as `http_error_301()`, but called for the ‘see other’ response.

 HTTPRedirectHandler.http_error_307(*req*, *fp*, *code*, *msg*, *hdrs*)

The same as `http_error_301()`, but called for the ‘temporary redirect’ response. Switching the request method from `POST` over to `GET` is not permitted here.

 HTTPRedirectHandler.http_error_308(*req*, *fp*, *code*, *msg*, *hdrs*)

The same as `http_error_301()`, but called for the ‘permanent redirect’ response. Switching the request method from `POST` over to `GET` is likewise not permitted here.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](basehandler-http-error-default.md) · [Continue](httpcookieprocessor-cookiejar.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)
