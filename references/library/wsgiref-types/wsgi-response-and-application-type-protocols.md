# wsgiref.types: `wsgiref.types.StartResponse`, `wsgiref.types.WSGIEnvironment`, `wsgiref.types.WSGIApplication`

### `wsgiref.types` – WSGI types for static type checking

For the sake of static type checking, this module supplies a range of types in the manner [**PEP 3333**](https://peps.python.org/pep-3333/) sets out.

Added in version 3.11.

 *class *wsgiref.types.StartResponse

A [`typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol) that characterizes [**start_response()**](https://peps.python.org/pep-3333/#the-start-response-callable) callables ([**PEP 3333**](https://peps.python.org/pep-3333/)).

 wsgiref.types.WSGIEnvironment

A type alias that characterizes a WSGI environment dictionary.

 wsgiref.types.WSGIApplication

A type alias that characterizes a WSGI application callable.

[Subject index](INDEX.md) · [Previous](../wsgiref-handlers/wsgiref-handlers-read-environ.md) · [Continue](wsgiref-types-inputstream-class.md)
