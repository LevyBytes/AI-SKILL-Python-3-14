# wsgiref.handlers: `wsgiref.handlers.SimpleHandler`

*class *wsgiref.handlers.SimpleHandler(*stdin*, *stdout*, *stderr*, *environ*, *multithread=True*, *multiprocess=False*)

Comparable to `BaseCGIHandler`, yet intended for use with HTTP origin servers. When you’re implementing an HTTP server, you’ll most likely want to subclass this rather than `BaseCGIHandler`.

This class subclasses `BaseHandler`. It overrides the `__init__()`, `get_stdin()`, `get_stderr()`, `add_cgi_vars()`, `_write()`, and `_flush()` methods so that the environment and streams can be set explicitly through the constructor. The environment and streams that are supplied get held in the `stdin`, `stdout`, `stderr`, and `environ` attributes.

The [`write()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.write) method of *stdout* should commit each chunk completely, in the manner of [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase).

[Subject index](INDEX.md) · [Previous](wsgiref-handlers-basecgihandler-class.md) · [Continue](wsgi-base-handler-and-cgi-environment.md) · [Owning module, declaration or section: wsgiref.handlers](wsgiref-handlers-cgihandler-class.md)
