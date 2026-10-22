# wsgiref.handlers: `wsgiref.handlers.BaseCGIHandler`

*class *wsgiref.handlers.BaseCGIHandler(*stdin*, *stdout*, *stderr*, *environ*, *multithread=True*, *multiprocess=False*)

Comparable to `CGIHandler`, except that rather than relying on the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) and [`os`](https://docs.python.org/3.14/library/os.html#module-os) modules, the CGI environment and I/O streams are given explicitly. The *multithread* and *multiprocess* values serve to set the `wsgi.multithread` and `wsgi.multiprocess` flags for any application the handler instance runs.

This class subclasses `SimpleHandler` and is meant for use with software other than HTTP “origin servers”. When you’re implementing a gateway protocol (CGI, FastCGI, SCGI, and so on) that relies on a `Status:` header to convey an HTTP status, you’ll likely want to subclass this rather than `SimpleHandler`.

[Subject index](INDEX.md) · [Previous](wsgiref-handlers-iiscgihandler-class.md) · [Continue](wsgiref-handlers-simplehandler-class.md) · [Owning module, declaration or section: wsgiref.handlers](wsgiref-handlers-cgihandler-class.md)
