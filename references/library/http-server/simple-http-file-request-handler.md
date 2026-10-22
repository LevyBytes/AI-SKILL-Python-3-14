# http.server / HTTP servers: `http.server.SimpleHTTPRequestHandler`, `do_HEAD()`, `do_GET()`

*class *http.server.SimpleHTTPRequestHandler(*request*, *client_address*, *server*, *directory=None*)

This class delivers files from *directory* and its subtree, or from the current directory when *directory* is not supplied, mapping the directory structure straight onto HTTP requests.

Changed in version 3.7: Added the *directory* parameter.

Changed in version 3.9: The *directory* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Much of the effort, including parsing the request, falls to the base class `BaseHTTPRequestHandler`. This class supplies the `do_GET()` and `do_HEAD()` functions.

These are declared as class-level attributes on `SimpleHTTPRequestHandler`:

 server_version

This becomes `"SimpleHTTP/" + __version__`, with `__version__` declared at the module level.

 extensions_map

A dictionary that maps suffixes onto MIME types, holding custom overrides for the default system mappings. Because the mapping is applied case-insensitively, it should hold only lower-cased keys.

Changed in version 3.9: Rather than being populated with the default system mappings, this dictionary now holds overrides alone.

These methods are defined by the `SimpleHTTPRequestHandler` class:

 do_HEAD()

This method handles the `'HEAD'` request type: it emits the headers it would emit for the matching `GET` request. Consult the `do_GET()` method for a fuller account of the headers that may appear.

 do_GET()

The request maps to a local file by treating the request as a path relative to the current working directory.

When the request mapped to a directory, that directory is examined for a file called `index.html` or `index.htm` (in that sequence). If one exists, the file's contents are returned; otherwise the `list_directory()` method is invoked to produce a directory listing. That method calls [`os.listdir()`](https://docs.python.org/3.14/library/os.html#os.listdir) to scan the directory and returns a `404` error response should the `listdir()` fail.

When the request mapped to a file, it gets opened. Any [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception while opening the requested file becomes a `404`, `'File not found'` error. When the request carried an `'If-Modified-Since'` header and the file went unchanged after that time, a `304`, `'Not Modified'` response is returned. Otherwise the content type is determined through the `guess_type()` method, which itself consults the *extensions_map* variable, and the file contents are returned.

A `'Content-type:'` header holding the guessed content type is emitted, then a `'Content-Length:'` header carrying the file's size and a `'Last-Modified:'` header carrying the file's modification time.

A blank line follows to mark the end of the headers, after which the file's contents are emitted.

For a usage example, look at the implementation of the `test` function within [Lib/http/server.py](https://github.com/python/cpython/tree/3.14/Lib/http/server.py).

Changed in version 3.7: Support of the `'If-Modified-Since'` header.

The `SimpleHTTPRequestHandler` class can serve to build a very simple webserver delivering files relative to the current directory, like so:

```python
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

```

You can also subclass `SimpleHTTPRequestHandler` to refine its behavior — for example, choosing alternate index file names by overriding the class attribute `index_pages`.

[Subject index](INDEX.md) · [Previous](http-server-basehttprequesthandler-address-string.md) · [Continue](cgi-request-handler-and-post.md) · [Owning module, declaration or section: http.server](http-server-httpserver-class.md)
