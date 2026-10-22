# logging.handlers: `logging.StreamHandler`

### StreamHandler

Found in the core [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) package, the `StreamHandler` class routes logging output to streams like *sys.stdout*, *sys.stderr* or any file-like object (or, to be more exact, any object furnishing `write()` and `flush()` methods).

 *class *logging.StreamHandler(*stream=None*)

Hands back a fresh instance of the `StreamHandler` class. When *stream* is given, the instance routes its logging output there; if not, *sys.stderr* serves instead.

[Subject index](INDEX.md) · [Previous](handler-types-overview.md) · [Continue](logging-streamhandler-emit-to-logging-streamhandler-setstream.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)
