# urllib.request: `BaseHandler.http_error_default()`

BaseHandler.http_error_default(*req*, *fp*, *code*, *msg*, *hdrs*)

`BaseHandler` does *not* define this method, though subclasses ought to override it when they aim to supply a catch-all for HTTP errors that go otherwise unhandled. The `OpenerDirector` that receives the error calls it for you, and it normally should not be called in any other situation.

`OpenerDirector` will call this method with five positional arguments:

1.

a `Request` object,

2.

a file-like object with the HTTP error body,

3.

the three-digit code of the error, as a string,

4.

the user-visible explanation of the code, as a string, and

5.

the headers of the error, as a mapping object.

Return values and exceptions raised should be the same as those of `urlopen()`.

 BaseHandler.http_error_&lt;nnn&gt;(req, fp, code, msg, hdrs)

*nnn* should be a three-digit HTTP error code. This method is likewise not defined within `BaseHandler`, but it will be invoked, where it exists, on an instance of a subclass whenever an HTTP error carrying code *nnn* arises.

Subclasses should override this method to handle specific HTTP errors.

Arguments, return values and exceptions raised should be the same as for `http_error_default()`.

 BaseHandler.&lt;protocol&gt;_request(req)

`BaseHandler` does *not* define this method, though subclasses ought to define it when they wish to pre-process requests carrying the given protocol.

Whenever it is defined, the parent `OpenerDirector` invokes this method. *req* will be a `Request` object. The return value should be a `Request` object.

 BaseHandler.&lt;protocol&gt;_response(req, response)

`BaseHandler` does *not* define this method, though subclasses ought to define it when they wish to post-process responses carrying the given protocol.

Whenever it is defined, the parent `OpenerDirector` invokes this method. Here *req* will be a `Request` object, and *response* will be an object whose interface matches that of what `urlopen()` returns. Likewise, what this method gives back ought to expose the same interface that `urlopen()`'s return value does.

[Subject index](INDEX.md) · [Previous](basehandler-add-parent-to-basehandler-unknown-open.md) · [Continue](http-redirect-request-and-status-handling.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md) · [Owning module, declaration or section: BaseHandler Objects](basehandler-add-parent-to-basehandler-unknown-open.md)
