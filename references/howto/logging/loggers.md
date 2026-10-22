# Loggers

### Loggers

[`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) objects carry out three jobs. To begin with, they present several methods to application code so that applications can log messages while running. Next, logger objects decide which log messages to act on, judging by severity (the default filtering mechanism) or by filter objects. Lastly, logger objects forward the relevant log messages onward to every interested log handler.

The logger-object methods that see the most use split into two groups: configuration and message sending.

The configuration methods most often used are these:

- [`Logger.setLevel()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.setLevel) sets the lowest-severity log message that a logger will deal with, with debug being the lowest built-in severity level and critical being the highest built-in severity. For instance, when the severity level is INFO, the logger handles only INFO, WARNING, ERROR, and CRITICAL messages and skips DEBUG messages.

- [`Logger.addHandler()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.addHandler) and [`Logger.removeHandler()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.removeHandler) attach handler objects to, and detach them from, the logger object. Handlers get a fuller treatment in Handlers.

- [`Logger.addFilter()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.addFilter) and [`Logger.removeFilter()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.removeFilter) attach filter objects to, and detach them from, the logger object. Filters get a fuller treatment in [Filter Objects](https://docs.python.org/3.14/library/logging.html#filter).

You aren't obliged to call these methods on every single logger you make. Look at the final two paragraphs of this section.

Once the logger object is configured, these methods produce log messages:

- [`Logger.debug()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.debug), [`Logger.info()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.info), [`Logger.warning()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.warning), [`Logger.error()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.error), and [`Logger.critical()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.critical) each build log records bearing a message and a level matching their own method names. That message is in fact a format string, which can hold the usual string substitution syntax of `%s`, `%d`, `%f`, and the like. Their remaining arguments form a list of objects matched against the substitution fields inside the message. As for `**kwargs`, the only keyword the logging methods pay attention to is `exc_info`, which they read to decide whether exception information should be logged.

- [`Logger.exception()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.exception) produces a log message much like [`Logger.error()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.error). What differs is that `Logger.exception()` also emits a stack trace alongside it. Only call this method from inside an exception handler.

- [`Logger.log()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.log) accepts a log level as a direct argument. Compared with the log level convenience methods listed above, this is somewhat more verbose for logging messages, yet it is the way to log at custom log levels.

[`getLogger()`](https://docs.python.org/3.14/library/logging.html#logging.getLogger) hands back a reference to a logger instance carrying the given name when one is supplied, or to `root` otherwise. Names take the form of period-separated hierarchical structures. Calling `getLogger()` repeatedly with one and the same name yields a reference to that same logger object. Loggers positioned lower in the hierarchical list are children of those higher in the list. As an example, given a logger named `foo`, the loggers named `foo.bar`, `foo.bar.baz`, and `foo.bam` are every one of them descendants of `foo`.

There is a notion of *effective level* that loggers have. When no level is explicitly assigned to a logger, the level belonging to its parent stands in as its effective level. Should the parent carry no explicit level, then *its* parent gets inspected, and so on - the search climbs through all ancestors until one with an explicitly set level turns up. The root logger always carries an explicit level (`WARNING` by default). In deciding whether to process an event, the logger's effective level is what determines whether that event reaches the logger's handlers.

Child loggers send messages up to the handlers tied to their ancestor loggers. For that reason, there's no need to define and configure handlers for every one of the loggers an application uses. Configuring handlers on a top-level logger and spinning up child loggers as required is enough. (You can, all the same, switch propagation off by setting a logger's *propagate* attribute to `False`.)

[Subject index](INDEX.md) · [Previous source context](logging-flow.md) · [Following source context](handlers.md)
