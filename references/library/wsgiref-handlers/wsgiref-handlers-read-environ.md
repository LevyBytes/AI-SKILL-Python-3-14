# wsgiref.handlers: `wsgiref.handlers.read_environ()`

wsgiref.handlers.read_environ()

Converts CGI variables out of `os.environ` into [**PEP 3333**](https://peps.python.org/pep-3333/) “bytes in unicode” strings and returns them as a fresh dictionary. Both `CGIHandler` and `IISCGIHandler` call on this function rather than reaching straight into `os.environ`, which under Python 3 is not guaranteed to be WSGI-compliant on every platform and web server — chiefly those where the OS environment itself is Unicode (Windows, that is), or those where the environment is bytes yet Python decodes it with a system encoding other than ISO-8859-1 (such as Unix systems running UTF-8).

Should you be writing a CGI-based handler of your own, you very likely want to lean on this routine instead of lifting values straight out of `os.environ`.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](wsgi-handler-scheme-and-file-transfer.md) · [Continue](../wsgiref-types/wsgi-response-and-application-type-protocols.md) · [Owning module, declaration or section: wsgiref.handlers](wsgiref-handlers-cgihandler-class.md)
