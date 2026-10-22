# Handlers

### Handlers

[`Handler`](https://docs.python.org/3.14/library/logging.html#logging.Handler) objects bear responsibility for delivering the right log messages (according to the log messages' severity) to the destination the handler has been given. [`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) objects may attach zero or more handler objects to themselves through an [`addHandler()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.addHandler) method. To take an example scenario, an application might wish to route every log message to a log file, every log message of error or above to stdout, and every critical message to an email address. That scenario calls for three separate handlers, with each handler tasked with delivering messages of one particular severity to one particular location.

The standard library ships with a fair number of handler types (see Useful Handlers); throughout its examples the tutorials rely chiefly on [`StreamHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.StreamHandler) and [`FileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.FileHandler).

A handler holds very few methods that application developers need to worry about. For application developers who work with the built-in handler objects (in other words, who don't write custom handlers), the only handler methods that appear pertinent are these configuration methods:

- The [`setLevel()`](https://docs.python.org/3.14/library/logging.html#logging.Handler.setLevel) method, exactly as with logger objects, sets the lowest severity that will be sent on to the proper destination. Why do two `setLevel()` methods exist? The level on the logger governs which severity of messages it forwards to its handlers. The level on each handler governs which messages that handler passes along.

- [`setFormatter()`](https://docs.python.org/3.14/library/logging.html#logging.Handler.setFormatter) picks a Formatter object for this handler to apply.

- [`addFilter()`](https://docs.python.org/3.14/library/logging.html#logging.Handler.addFilter) and [`removeFilter()`](https://docs.python.org/3.14/library/logging.html#logging.Handler.removeFilter) respectively set up and tear down filter objects on handlers.

Application code ought not to instantiate and use [`Handler`](https://docs.python.org/3.14/library/logging.html#logging.Handler) instances directly. Rather, the `Handler` class serves as a base class that lays out the interface every handler ought to have and sets up some default behavior for child classes to adopt (or override).

[Subject index](INDEX.md) · [Previous source context](loggers.md) · [Following source context](formatters.md)
