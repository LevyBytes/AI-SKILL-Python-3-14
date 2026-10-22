# What's New in Python 2.5 / The wsgiref package — wsgiref

### The wsgiref package

The Web Server Gateway Interface (WSGI) v1.0 sets out a standard boundary between web servers and Python web applications and is laid out in [**PEP 333**](https://peps.python.org/pep-0333/). As a reference implementation of that WSGI specification, the [`wsgiref`](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref) package is provided.

Bundled in the package is a simple HTTP server able to host a WSGI application; handy for debugging, it is not meant for production. Standing up a server needs just a handful of lines:

```python
from wsgiref import simple_server

wsgi_app = ...

host = ''
port = 8000
httpd = simple_server.make_server(host, port, wsgi_app)
httpd.serve_forever()

```

See also

[https://web.archive.org/web/20160331090247/http://wsgi.readthedocs.org/en/latest/](https://web.archive.org/web/20160331090247/http://wsgi.readthedocs.org/en/latest/)

A central web site for WSGI-related resources.

[**PEP 333**](https://peps.python.org/pep-0333/) - Python Web Server Gateway Interface v1.0

PEP written by Phillip J. Eby.

[Subject index](INDEX.md) · [Previous source section](sqlite-query-language-and-type-adapters.md) · [Next source section](build-and-c-api-changes.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
