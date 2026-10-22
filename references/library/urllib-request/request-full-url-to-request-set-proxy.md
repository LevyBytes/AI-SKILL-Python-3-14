# urllib.request: Request URL, headers, methods and proxy configuration

### Request Objects

The methods below outline `Request`'s public interface, so any of them may be overridden in subclasses. Several public attributes are also defined, which clients can use to examine the parsed request.

 Request.full_url

The original URL handed to the constructor.

Changed in version 3.4.

Request.full_url is a property equipped with a setter, a getter, and a deleter. Reading `full_url` gives back the original request URL together with the fragment, when one was present.

 Request.type

The URI scheme.

 Request.host

The URI authority, usually a host, though it may also include a port set off by a colon.

 Request.origin_req_host

The original host for the request, port omitted.

 Request.selector

The URI path. When the `Request` goes through a proxy, selector will hold the full URL handed to the proxy.

 Request.data

The entity body for the request, or `None` when none was given.

Changed in version 3.4: Altering the value of `Request.data` now removes the "Content-Length" header when it had earlier been set or computed.

 Request.unverifiable

boolean, indicates whether the request is unverifiable as defined by [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html).

 Request.method

The HTTP request method to apply. Its value defaults to [`None`](https://docs.python.org/3.14/library/constants.html#None), meaning `get_method()` will carry out its usual computation of the method to use. You can set its value (thereby overriding the default computation in `get_method()`) either by supplying a default at the class level within a `Request` subclass, or by passing a value to the `Request` constructor through the *method* argument.

Added in version 3.3.

Changed in version 3.4: Subclasses may now supply a default value; formerly the only way to set it was through the constructor argument.

 Request.get_method()

Return a string naming the HTTP request method. When `Request.method` is not `None`, return its value; otherwise return `'GET'` when `Request.data` is `None`, or `'POST'` when it is not. This carries meaning only for HTTP requests.

Changed in version 3.3: get_method now looks at the value of `Request.method`.

 Request.add_header(*key*, *val*)

Attach another header to the request. At present every handler except HTTP handlers ignores headers; with HTTP handlers they join the list of headers sent to the server. Note that no two headers may share a name, and a later call overwrites an earlier one when the *key* collides. For now this loses no HTTP functionality, since every header whose meaning depends on multiple uses has a (header-specific) means of achieving the same result with just one header. Note that headers added through this method also carry over to redirected requests.

 Request.add_unredirected_header(*key*, *header*)

Attach a header that will be left out of a redirected request.

 Request.has_header(*header*)

Return whether the instance carries the named header (checking both regular and unredirected).

 Request.remove_header(*header*)

Remove the named header from the request instance (from both the regular and unredirected headers).

Added in version 3.4.

 Request.get_full_url()

Return the URL supplied to the constructor.

Changed in version 3.4.

Returns `Request.full_url`

 Request.set_proxy(*host*, *type*)

[Subject index](INDEX.md) · [Previous](urllib-request-httperrorprocessor-class.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md) · [Required continuation of the source contract](request-get-header-to-request-header-items.md)
