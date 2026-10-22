# wsgiref.util: `wsgiref.util.guess_scheme()`, `wsgiref.util.request_uri()`, `wsgiref.util.application_uri()`, `wsgiref.util.shift_path_info()`, `wsgiref.util.setup_testing_defaults()`, `wsgiref.util.is_hop_by_hop()`

### `wsgiref.util` – WSGI environment utilities

A collection of helper functions for handling WSGI environments lives in this module. As outlined in [**PEP 3333**](https://peps.python.org/pep-3333/), a WSGI environment is a dictionary that holds HTTP request variables. Each function accepting an *environ* argument requires that a WSGI-compliant dictionary be passed; refer to [**PEP 3333**](https://peps.python.org/pep-3333/) for the full specification and to `WSGIEnvironment` for a type alias usable within type annotations.

 wsgiref.util.guess_scheme(*environ*)

Produce a best guess as to whether `wsgi.url_scheme` ought to be “http” or “https” by inspecting the *environ* dictionary for an `HTTPS` environment variable. A string is what gets returned.

The function comes in handy when building a gateway that wraps CGI or some CGI-style protocol like FastCGI. Servers offering these protocols generally set an `HTTPS` variable to “1”, “yes”, or “on” whenever a request arrives over SSL. Accordingly, the function yields “https” when such a value is detected, and otherwise “http”.

 wsgiref.util.request_uri(*environ*, *include_query=True*)

Reconstruct the complete request URI, with the query string included when desired, following the procedure laid out in the “URL Reconstruction” portion of [**PEP 3333**](https://peps.python.org/pep-3333/). When *include_query* is false, the resulting URI omits the query string.

 wsgiref.util.application_uri(*environ*)

Behaves like `request_uri()`, but the `PATH_INFO` and `QUERY_STRING` variables get disregarded. What you get back is the base URI of the application object that the request targets.

 wsgiref.util.shift_path_info(*environ*)

Move a single name out of `PATH_INFO` into `SCRIPT_NAME` and hand back that name. The *environ* dictionary gets *modified* in place; keep a copy if the original `PATH_INFO` or `SCRIPT_NAME` must be preserved.

`None` is returned whenever `PATH_INFO` contains no further path segments.

This routine is generally employed to walk through each piece of a request URI path — for instance, treating the path as a chain of dictionary keys. It rewrites the supplied environment so that it can drive another WSGI application sitting at the target URI. Suppose a WSGI application lives at `/foo`, the request URI path is `/foo/bar/baz`, and the `/foo` application calls `shift_path_info()`: it gets back the string “bar”, and the environment is adjusted to suit a WSGI application at `/foo/bar`. In other words, `SCRIPT_NAME` shifts from `/foo` to `/foo/bar`, while `PATH_INFO` shifts from `/bar/baz` to `/baz`.

If `PATH_INFO` is merely a “/”, this routine hands back an empty string and tacks a trailing slash onto `SCRIPT_NAME`, despite the fact that empty path segments are usually skipped and `SCRIPT_NAME` does not ordinarily finish with a slash. That deliberate behavior lets an application distinguish URIs that end in `/x` from those ending in `/x/` while performing object traversal with this routine.

 wsgiref.util.setup_testing_defaults(*environ*)

Populate *environ* with minimal defaults meant for testing.

This routine supplies the assorted parameters that WSGI needs, among them `HTTP_HOST`, `SERVER_NAME`, `SERVER_PORT`, `REQUEST_METHOD`, `SCRIPT_NAME`, `PATH_INFO`, and every `wsgi.*` variable defined by [**PEP 3333**](https://peps.python.org/pep-3333/). It merely fills in default values and leaves any existing settings for these variables untouched.

The purpose of this routine is to simplify setting up dummy environments when unit-testing WSGI servers and applications. Real WSGI servers or applications should NOT call it, because the data it produces is fake!

Example usage (also consult `demo_app()` for a further example):

```python
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]
    return ret

with make_server('', 8000, simple_app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()

```

Beyond the environment functions listed above, the `wsgiref.util` module also offers these assorted utilities:

 wsgiref.util.is_hop_by_hop(*header_name*)

Yield `True` when ‘header_name’ names an HTTP/1.1 “Hop-by-Hop” header in the sense defined by [**RFC 2616**](https://datatracker.ietf.org/doc/html/rfc2616.html).

[Subject index](INDEX.md) · [Previous](../wsgiref/wsgiref-wsgi-utilities-and-reference-implementation.md) · [Continue](wsgiref-util-filewrapper-class.md)
