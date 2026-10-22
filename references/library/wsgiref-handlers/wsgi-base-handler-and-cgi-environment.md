# wsgiref.handlers: `wsgiref.handlers.BaseHandler`, `run()`, `_write()`, `_flush()`, `get_stdin()`, `get_stderr()`, `add_cgi_vars()`

*class *wsgiref.handlers.BaseHandler

Here is an abstract base class for running WSGI applications. A single HTTP request is handled by each instance, though in theory you could write a subclass reusable across multiple requests.

`BaseHandler` instances expose just one method meant for outside use:

 run(*app*)

Run the given WSGI application, *app*.

This method drives all the other `BaseHandler` methods as it runs the application, so those methods exist chiefly to let you customize the process.

A subclass MUST override the following methods:

 _write(*data*)

Buffer the bytes *data* awaiting transmission to the client. It’s fine if this method really does send the data; `BaseHandler` simply keeps write and flush apart to gain efficiency where the underlying system genuinely draws such a distinction.

 _flush()

Compel buffered data out to the client. It’s fine if this method does nothing (that is, if `_write()` actually sends the data).

 get_stdin()

Return an object compatible with `InputStream` fit to serve as the `wsgi.input` of the request being processed at the moment.

 get_stderr()

Return an object compatible with `ErrorStream` fit to serve as the `wsgi.errors` of the request being processed at the moment.

 add_cgi_vars()

Add CGI variables for the current request to the `environ` attribute.

Below are some further methods and attributes you might wish to override. This list is merely a summary, however, and leaves out some methods that can be overridden. Before you set about creating a customized `BaseHandler` subclass, you should review the docstrings and source code for more details.

Attributes and methods for customizing the WSGI environment:

 wsgi_multithread

The value to use for the `wsgi.multithread` environment variable. In `BaseHandler` it defaults to true, but the other subclasses may default it differently (or set it through the constructor).

 wsgi_multiprocess

[Subject index](INDEX.md) · [Previous](wsgiref-handlers-simplehandler-class.md) · [Owning module, declaration or section: wsgiref.handlers](wsgiref-handlers-cgihandler-class.md) · [Required continuation of the source contract](wsgi-handler-scheme-and-file-transfer.md)
