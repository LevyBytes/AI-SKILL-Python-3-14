# Formatters

### Formatters

Formatter objects set the final ordering, structure, and contents of the log message. In contrast to the base [`logging.Handler`](https://docs.python.org/3.14/library/logging.html#logging.Handler) class, application code is free to instantiate formatter classes, though you would probably subclass the formatter when your application calls for special behavior. Its constructor takes three arguments that are all optional – a string for the message format, a string for the date format, and an indicator of style.

[Subject index](INDEX.md) · [Following source continuation](logging-formatter-defaults-styles-and-time-conversion.md) · [logging.Formatter.__init__: defaults, styles, versions and time conversion](logging-formatter-defaults-styles-and-time-conversion.md) · [Previous source context](handlers.md) · [Following source context](logging-formatter-defaults-styles-and-time-conversion.md)
