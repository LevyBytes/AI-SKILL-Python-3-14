# What’s New in Python 2.3 / PEP 282: The logging Package — logging

### PEP 282: The logging Package

Python 2.3 gained [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging), a standard package for keeping logs. It delivers a capable, adaptable means of producing logging output that you can then filter and handle in numerous fashions. A program’s logging behavior can be governed through a configuration file laid out in a standard format. The handlers Python provides can write log records to standard error, to a file, or to a socket, dispatch them to the system log, or even e-mail them off to some address; naturally, writing handler classes of your own is an option too.

The class that matters most is [`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger). The bulk of application code works with one or more `Logger` objects, each tied to some particular subsystem of the application. A name identifies every `Logger`, and those names form a hierarchy with `.` acting as the component separator. You might, for example, hold `Logger` instances called `server`, `server.auth` and `server.network`. Within the hierarchy, the latter two sit beneath `server`. Consequently, raising the verbosity on `server` or routing `server` messages off to another handler also takes effect on records logged to `server.auth` and `server.network`. A root `Logger` exists as well, standing as the parent above every other logger.

When your needs are simple, the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) package offers a handful of convenience functions that always operate on the root log:

```python
import logging

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

```

The output this yields is as follows:

```python
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down

```

Out of the box, the informational and debugging messages are held back while output goes to standard error. To switch on the showing of informational and debugging messages, call the [`setLevel()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.setLevel) method on the root logger.

Observe how the [`warning()`](https://docs.python.org/3.14/library/logging.html#logging.warning) call relies on string formatting operators; the whole family of message-logging functions accepts the arguments `(msg, arg1, arg2, ...)` and logs the text that results from `msg % (arg1, arg2, ...)`.

An [`exception()`](https://docs.python.org/3.14/library/logging.html#logging.exception) function is on offer as well, and it logs the latest traceback. Any of the remaining functions will likewise log the traceback once you hand a true value to the keyword argument *exc_info*.

```python
def f():
    try:    1/0
    except: logging.exception('Problem recorded')

f()

```

The output this yields is as follows:

```python
ERROR:root:Problem recorded
Traceback (most recent call last):
  File "t.py", line 6, in f
    1/0
ZeroDivisionError: integer division or modulo by zero

```

Programs of somewhat greater sophistication will reach for a logger besides the root one. To fetch a specific log — creating it on the spot if it is not there yet — you call the `getLogger(name)` function. The root logger is what `getLogger(None)` returns.

```python
log = logging.getLogger('server')
 ...
log.info('Listening on port %i', port)
 ...
log.critical('Disk full')
 ...

```

Because log records normally travel up the hierarchy, a message logged to `server.auth` reaches `server` and `root` as well, though a [`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) can stop that by setting its [`propagate`](https://docs.python.org/3.14/library/logging.html#logging.Logger.propagate) attribute to [`False`](https://docs.python.org/3.14/library/constants.html#False).

The [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) package supplies still more classes open to customization. Once a [`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) instance is asked to log a message, it produces a [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) instance, which then travels to however many separate [`Handler`](https://docs.python.org/3.14/library/logging.html#logging.Handler) instances there may be. Both loggers and handlers may carry an attached list of filters, and any filter can either drop the `LogRecord` or alter the record before sending it onward. At the point of final output, a [`Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter) class turns `LogRecord` instances into text. Every one of these classes can give way to specially written classes of your own.

Given the whole of these capabilities, the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) package ought to be flexible enough to satisfy all but the most intricate applications. What appears here is merely a partial survey of what it can do, so do turn to the package’s reference documentation for every detail. It will also pay to read [**PEP 282**](https://peps.python.org/pep-0282/).

See also

[**PEP 282**](https://peps.python.org/pep-0282/) - A Logging System

Written by Vinay Sajip and Trent Mick; implemented by Vinay Sajip.

[Subject index](INDEX.md) · [Previous source section](pep-279-enumerate.md) · [Next source section](pep-285-a-boolean-type.md) · [Release/subject declaration](standard-set-type.md)
