# urllib.request — OpenerDirector Objects

### OpenerDirector Objects

`OpenerDirector` instances have the following methods:

 OpenerDirector.add_handler(*handler*)

*handler* should be an instance of `BaseHandler`. Each of the methods below is looked for and folded into the candidate chains (bear in mind that HTTP errors get special treatment). Bear in mind that, throughout what follows, you substitute the real protocol being handled for *protocol* — say, `http_response()` for the HTTP protocol response handler. Likewise, you substitute the real HTTP code for *type* — say, `http_error_404()` to take on HTTP 404 errors.

- `<protocol>_open()` — marks the handler as capable of opening *protocol* URLs.

See `BaseHandler.<protocol>_open()` for more information.

- `http_error_<type>()` — marks the handler as capable of dealing with HTTP errors that carry HTTP error code *type*.

See `BaseHandler.http_error_<nnn>()` for more information.

- `<protocol>_error()` — marks the handler as capable of dealing with errors arising from (non-`http`) *protocol*.

- `<protocol>_request()` — marks the handler as capable of pre-processing *protocol* requests.

See `BaseHandler.<protocol>_request()` for more information.

- `<protocol>_response()` — marks the handler as capable of post-processing *protocol* responses.

See `BaseHandler.<protocol>_response()` for more information.

 OpenerDirector.open(*url*, *data=None*[, *timeout*])

Open the supplied *url* (a request object or a string will both work), optionally handing along the supplied *data*. The arguments, the values returned, and the exceptions thrown line up with those of `urlopen()` (which just invokes the `open()` method on the global `OpenerDirector` that is presently installed). The optional *timeout* parameter sets, in seconds, how long blocking operations such as the connection attempt may run (when it is left unset, the setting for the global default timeout applies). Realistically the timeout behavior applies solely to HTTP, HTTPS and FTP connections.

 OpenerDirector.error(*proto*, **args*)

Deal with an error belonging to the named protocol. Doing so invokes the error handlers registered for that protocol, passing along the supplied arguments (which vary by protocol). HTTP stands apart here, as it relies on the HTTP response code to pick out the right error handler; see the `http_error_<type>()` methods on the handler classes.

Return values and exceptions raised are the same as those of `urlopen()`.

OpenerDirector objects open URLs in three stages:

Sorting the handler instances fixes the sequence in which these methods get invoked inside each stage.

1.

Each handler that owns a method named like `<protocol>_request()` gets that method invoked so the request can be pre-processed.

2.

Handlers owning a method named like `<protocol>_open()` get invoked to service the request. This stage wraps up once a handler either gives back a non-[`None`](https://docs.python.org/3.14/library/constants.html#None) value (ie. a response) or throws an exception (typically [`URLError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.URLError)). Exceptions are free to propagate upward.

As it happens, the algorithm above is attempted first against methods called `default_open()`. When all of those methods give back [`None`](https://docs.python.org/3.14/library/constants.html#None), the same procedure runs again for methods named like `<protocol>_open()`. Should all of those likewise give back `None`, the procedure runs once more against methods called `unknown_open()`.

Bear in mind that how these methods are implemented may entail invoking the parent `OpenerDirector` instance’s `open()` and `error()` methods.

3.

Each handler that owns a method named like `<protocol>_response()` gets that method invoked so the response can be post-processed.

[Subject index](INDEX.md) · [Previous](request-get-header-to-request-header-items.md) · [Continue](basehandler-add-parent-to-basehandler-unknown-open.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)
