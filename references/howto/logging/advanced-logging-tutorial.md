# Advanced Logging Tutorial

### Advanced Logging Tutorial

The logging library is built in a modular fashion and supplies several kinds of components: loggers, handlers, filters, and formatters.

- Loggers present the interface that application code calls directly.

- Handlers route the log records (produced by loggers) to wherever they belong.

- Filters offer a more fine-grained means of deciding which log records get emitted.

- Formatters dictate how log records are laid out in the final output.

Information about a log event travels among loggers, handlers, filters and formatters within a [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) instance.

You carry out logging by invoking methods on instances of the [`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) class (referred to from here on as *loggers*). Every instance carries a name, and conceptually they sit in a namespace hierarchy where dots (periods) act as separators. As an example, a logger called ‘scan’ serves as the parent of the loggers ‘scan.text’, ‘scan.html’ and ‘scan.pdf’. You can name loggers however you like, with the name signaling which part of an application a logged message comes from.

A solid convention when naming loggers is to keep a module-level logger in every module that does logging, named in this way:

```python
logger = logging.getLogger(__name__)

```

What this gives you is logger names that follow the package/module hierarchy, so it's plainly obvious from the logger name alone where events get logged.

At the top of the logger hierarchy sits the root logger. It is the very logger that the functions [`debug()`](https://docs.python.org/3.14/library/logging.html#logging.debug), [`info()`](https://docs.python.org/3.14/library/logging.html#logging.info), [`warning()`](https://docs.python.org/3.14/library/logging.html#logging.warning), [`error()`](https://docs.python.org/3.14/library/logging.html#logging.error) and [`critical()`](https://docs.python.org/3.14/library/logging.html#logging.critical) employ, since they merely invoke the identically named method on the root logger. Both the functions and the methods share the same signatures. In the logged output the root logger's name shows up as ‘root’.

Naturally, you can send log messages to a variety of destinations. The package has built-in support for delivering log messages to files, to HTTP GET/POST locations, to email over SMTP, to generic sockets, to queues, or to OS-specific logging facilities like syslog or the Windows NT event log. Those destinations are handled by *handler* classes. If your needs aren't covered by any of the built-in handler classes, you can write your own log destination class.

By default, no logging message has any destination assigned. You set a destination (the console or a file, say) with [`basicConfig()`](https://docs.python.org/3.14/library/logging.html#logging.basicConfig), just as the tutorial examples do. When you invoke the functions [`debug()`](https://docs.python.org/3.14/library/logging.html#logging.debug), [`info()`](https://docs.python.org/3.14/library/logging.html#logging.info), [`warning()`](https://docs.python.org/3.14/library/logging.html#logging.warning), [`error()`](https://docs.python.org/3.14/library/logging.html#logging.error) and [`critical()`](https://docs.python.org/3.14/library/logging.html#logging.critical), they will test whether a destination has been assigned; finding none, they will assign the console (`sys.stderr`) as the destination together with a default format for the shown message, then hand off to the root logger to carry out the actual message output.

Here is the default message format that [`basicConfig()`](https://docs.python.org/3.14/library/logging.html#logging.basicConfig) applies:

```none
severity:logger name:message

```

To alter this, pass a format string into [`basicConfig()`](https://docs.python.org/3.14/library/logging.html#logging.basicConfig) using the *format* keyword argument. For every option on how to build a format string, refer to [Formatter Objects](https://docs.python.org/3.14/library/logging.html#formatter-objects).

[Subject index](INDEX.md) · [Previous source context](next-steps.md) · [Following source context](logging-flow.md)
