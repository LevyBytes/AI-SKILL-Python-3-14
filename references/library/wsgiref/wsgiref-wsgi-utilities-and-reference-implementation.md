# wsgiref`wsgiref` - WSGI Utilities and Reference Implementation

### `wsgiref` - WSGI Utilities and Reference Implementation

**Source code:** [Lib/wsgiref](https://github.com/python/cpython/tree/3.14/Lib/wsgiref)

---

Warning

`wsgiref` serves as a reference implementation and should not be relied on in production settings. Only rudimentary security checks are performed by the module.

The Web Server Gateway Interface (WSGI) defines a common contract that connects web server software to Python-authored web applications. Because the interface is standardized, an application that speaks WSGI can be paired with many different web servers with little effort.

Every nuance and edge case of the WSGI design only matters to people who build web servers or programming frameworks. Installing a WSGI application, or writing one on top of an existing framework, requires no such deep understanding of WSGI.

As a reference implementation of the WSGI specification, `wsgiref` exists to bolt WSGI support onto a web server or framework. The package supplies helpers for manipulating WSGI environment variables and response headers, base classes from which to build WSGI servers, a demonstration HTTP server that hosts WSGI applications, types intended for static type checking, and a validation tool that audits WSGI servers and applications against the WSGI specification ([**PEP 3333**](https://peps.python.org/pep-3333/)) for conformance.

Consult [wsgi.readthedocs.io](https://wsgi.readthedocs.io/) for further details on WSGI, along with pointers to tutorials and additional resources.

[Subject index](INDEX.md) · [Continue](../wsgiref-util/wsgiref-util-guess-scheme-to-wsgiref-util-is-hop-by-hop.md)
