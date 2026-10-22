# Adding handlers other than `NullHandler` to a logger in a library

### Adding handlers other than [`NullHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.NullHandler) to a logger in a library

Setting up logging by attaching handlers, formatters and filters falls to the application developer, not to the library developer. As the maintainer of a library, make sure you attach no handlers to any of your loggers apart from a [`NullHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.NullHandler) instance.

[Subject index](INDEX.md) · [Previous source context](logger-attributes-and-parameter-misuse.md) · [Following source context](creating-a-lot-of-loggers.md)
