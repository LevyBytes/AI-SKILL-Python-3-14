# What's New In Python 3.2 / PEP 3333: Python Web Server Gateway Interface v1.0.1 - os, wsgiref

### PEP 3333: Python Web Server Gateway Interface v1.0.1

This informational PEP spells out the way the WSGI protocol ought to treat bytes-versus-text concerns. The difficulty is that, in Python 3, working with strings is easiest via the [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) type, whereas HTTP itself is fundamentally a bytes-oriented protocol.

The PEP draws a line between so-called *native strings*, carrying request/response headers and metadata, and *byte strings*, carrying the bodies of requests and responses.

Those *native strings* are invariably [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), yet limited to code points spanning *U+0000* up to *U+00FF*, all encodable as bytes through *Latin-1*. Such strings serve as the keys and values within the environment dictionary and as the response headers and statuses passed to the `start_response()` function. With respect to encoding they have to obey [**RFC 2616**](https://datatracker.ietf.org/doc/html/rfc2616.html); that is, they must consist of *ISO-8859-1* characters or else apply [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html) MIME encoding.

Developers moving WSGI applications over from Python 2 should note these key points:

- When the application already relied on strings for headers under Python 2, nothing needs to change.

- When the application instead encoded outgoing headers or decoded incoming ones, those headers must be re-encoded into Latin-1. As an example, an outgoing header formerly produced in utf-8 via `h.encode('utf-8')` now has to go from bytes to native strings via `h.encode('utf-8').decode('latin-1')`.

- Whatever an application yields or sends through the `write()` method has to be byte strings. Both the `start_response()` function and environ have to use native strings. You cannot blend the two.

- Server authors building CGI-to-WSGI bridges or similar CGI-style protocols have to let users reach the environment as native strings, even where the host platform follows another convention. To span that divide, the [`wsgiref`](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref) module gained a new function, [`wsgiref.handlers.read_environ()`](https://docs.python.org/3.14/library/wsgiref.html#wsgiref.handlers.read_environ), which transcodes CGI variables out of [`os.environ`](https://docs.python.org/3.14/library/os.html#os.environ) into native strings and yields a fresh dictionary.

See also

[**PEP 3333**](https://peps.python.org/pep-3333/) - Python Web Server Gateway Interface v1.0.1

PEP written by Phillip Eby.

[Subject index](INDEX.md) · [Previous source section](pep-3149-abi-version-tagged-so-files.md) · [Next source section](core-language-changes.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
