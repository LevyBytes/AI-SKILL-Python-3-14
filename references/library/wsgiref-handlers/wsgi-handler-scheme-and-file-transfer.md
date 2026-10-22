# wsgiref.handlers.BaseHandler: `get_scheme()`, `setup_environ()`, `log_exception()`, `error_output()`, `sendfile()`

The figure that the `wsgi.multiprocess` environment variable will carry. Within `BaseHandler` it starts out true, yet the remaining subclasses may begin with a different value (or have one assigned by the constructor).

 wsgi_run_once

The figure that the `wsgi.run_once` environment variable will carry. It starts out false within `BaseHandler`, although `CGIHandler` flips it to true out of the box.

 os_environ

Those environment variables that get folded into every request’s WSGI environment by default. Out of the box this holds a snapshot of `os.environ` taken at the moment `wsgiref.handlers` was imported, but subclasses may roll their own at either the class or the instance level. Bear in mind the dictionary ought to be handled as read-only, given that the default value is shared across several classes and instances.

 server_software

When the `origin_server` attribute has been set, the value stored here drives the default `SERVER_SOFTWARE` WSGI environment variable and likewise supplies a default `Server:` header on HTTP responses. Handlers that are not HTTP origin servers (`BaseCGIHandler` and `CGIHandler`, for instance) pay it no attention.

Changed in version 3.3: The wording “Python” gives way to an implementation-specific label such as “CPython”, “Jython”, and so on.

 get_scheme()

Hands back whichever URL scheme applies to the request at hand. As shipped, the implementation leans on the `guess_scheme()` function out of `wsgiref.util` to surmise from the request’s `environ` variables whether the scheme ought to be “http” or “https”.

 setup_environ()

Populates the `environ` attribute with a complete WSGI environment. The shipped implementation draws on every method and attribute named above, together with the `get_stdin()`, `get_stderr()`, and `add_cgi_vars()` methods and the `wsgi_file_wrapper` attribute. It additionally injects a `SERVER_SOFTWARE` key where one is absent, provided the `origin_server` attribute holds a true value and the `server_software` attribute has been set.

Methods and attributes for customizing exception handling:

 log_exception(*exc_info*)

Records the *exc_info* tuple into the server log. Here *exc_info* takes the form of a `(type, value, traceback)` tuple. The shipped implementation does little more than emit the traceback onto the request’s `wsgi.errors` stream and then flush it. A subclass is free to override this method so as to reshape the format, redirect the output, email the traceback to an administrator, or take whatever else seems fitting.

 traceback_limit

The ceiling on how many frames the default `log_exception()` method will print in its tracebacks. A value of `None` means every frame is shown.

 error_output(*environ*, *start_response*)

A WSGI application whose job is to build an error page for the user. It fires only when an error arises before any headers have gone out to the client.

From within it, the active error is reachable through `sys.exception()`, and that information should be relayed to *start_response* at call time (just as the “Error Handling” section of [**PEP 3333**](https://peps.python.org/pep-3333/) lays out). Specifically, the *start_response* callable ought to honor the `StartResponse` protocol.

The shipped implementation merely draws on the `error_status`, `error_headers`, and `error_body` attributes to assemble an output page. A subclass may override this to yield more dynamic error output.

Be aware, though, that from a security standpoint dumping diagnostics to just any visitor is discouraged; the ideal is that some deliberate step is required to switch diagnostic output on, which is precisely why the shipped implementation ships none.

 error_status

The HTTP status carried by error responses. It ought to be a status string of the kind spelled out in [**PEP 3333**](https://peps.python.org/pep-3333/); the default is a 500 code together with its message.

 error_headers

The HTTP headers carried by error responses. This ought to be a list of WSGI response headers (`(name, value)` tuples), in the manner [**PEP 3333**](https://peps.python.org/pep-3333/) describes. The default list does nothing more than fix the content type at `text/plain`.

 error_body

The body of the error response. This ought to be an HTTP response body bytestring. By default it is the plain text, “A server error occurred. Please contact the administrator.”

Methods and attributes for [**PEP 3333**](https://peps.python.org/pep-3333/)’s “Optional Platform-Specific File Handling” feature:

 wsgi_file_wrapper

Either a `wsgi.file_wrapper` factory that works with `wsgiref.types.FileWrapper`, or else `None`. This attribute defaults to the `wsgiref.util.FileWrapper` class.

 sendfile()

Override this to supply platform-specific file transmission. The method runs only when the application’s return value happens to be an instance of the class named by the `wsgi_file_wrapper` attribute. Returning a true value signals that the file went out successfully and that the default transmission code should be skipped. As shipped, this method simply returns a false value.

Miscellaneous methods and attributes:

 origin_server

Give this attribute a true value whenever the handler’s `_write()` and `_flush()` talk straight to the client, as opposed to going through a CGI-style gateway protocol that expects the HTTP status inside a dedicated `Status:` header.

The attribute defaults to true under `BaseHandler`, yet to false under `BaseCGIHandler` and `CGIHandler`.

 http_version

When `origin_server` holds true, this string attribute fixes the HTTP version of the response handed to the client. Its default is `"1.0"`.

[Subject index](INDEX.md) · [Continue](wsgiref-handlers-read-environ.md) · [Owning module, declaration or section: wsgiref.handlers](wsgiref-handlers-cgihandler-class.md) · [Owning module, declaration or section: wsgiref.handlers.BaseHandler](wsgi-base-handler-and-cgi-environment.md) · [Owning module, declaration or section: wsgi_multiprocess](wsgi-base-handler-and-cgi-environment.md) · [Preceding source contract and version conditions](wsgi-base-handler-and-cgi-environment.md)
