# wsgiref.headers: `wsgiref.headers.Headers`

### `wsgiref.headers` – WSGI response header tools

A lone class, `Headers`, is what this module exposes, offering a mapping-style interface for working conveniently with WSGI response headers.

 *class *wsgiref.headers.Headers([*headers*])

Build a mapping-style object that wraps *headers*, which has to be a list of header name/value tuples in the form described by [**PEP 3333**](https://peps.python.org/pep-3333/). By default, *headers* is an empty list.

The usual mapping operations work on `Headers` objects, namely [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__), [`get()`](https://docs.python.org/3.14/library/stdtypes.html#dict.get), [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__), [`setdefault()`](https://docs.python.org/3.14/library/stdtypes.html#dict.setdefault), [`__delitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delitem__) and [`__contains__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__contains__). With each one, the header name (matched without regard to case) serves as the key, and the value is the first value tied to that header name. Assigning a header removes whatever values that header already had, then appends a fresh value at the tail of the wrapped header list. The pre-existing order of headers is largely preserved, while new headers go onto the end of the wrapped list.

In contrast to a dictionary, `Headers` objects raise no error when you attempt to fetch or remove a key absent from the wrapped header list. Fetching a header that doesn’t exist simply yields `None`, and removing one that doesn’t exist has no effect.

`Headers` objects additionally support the `keys()`, `values()`, and `items()` methods. A given key can show up more than once in the lists from `keys()` and `items()` when a header carries multiple values. A `Headers` object’s `len()` matches the length of its `items()`, which matches the length of the wrapped header list. In fact, `items()` merely hands back a copy of the wrapped header list.

Invoking `bytes()` on a `Headers` object yields a formatted bytestring ready to be sent as HTTP response headers. Every header occupies a line alongside its value, the two parted by a colon and a space. A carriage return and line feed close each line, and a blank line closes the bytestring.

On top of their mapping interface and formatting capabilities, `Headers` objects expose the methods below for inspecting and appending multi-valued headers, and for appending headers carrying MIME parameters:

[Subject index](INDEX.md) · [Previous](../wsgiref-util/wsgiref-util-filewrapper-class.md) · [Continue](wsgi-response-header-access-and-addition.md)
