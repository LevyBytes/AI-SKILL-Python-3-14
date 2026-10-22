# What’s New in Python 2.7 / PEP 391: Dictionary-Based Configuration For Logging — logging, logging.config, logging.handlers, socket

### PEP 391: Dictionary-Based Configuration For Logging

The [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module is highly flexible; applications may define a tree of logging subsystems, and each logger within that tree can screen out certain messages, format them in its own way, and route messages to a varying count of handlers.

All of that flexibility can demand a great deal of configuration. You may write Python statements that create objects and set their properties, yet an elaborate set-up calls for verbose but tedious code. [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) additionally provides a [`fileConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.fileConfig) function that parses a file, but the file format offers no way to configure filters, and it is harder to produce programmatically.

Python 2.7 introduces a [`dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig) function that relies on a dictionary to configure logging. A dictionary can be produced from many sources: build one in code; parse a file holding JSON; or, if one is installed, use a YAML parsing library. See [Configuration functions](https://docs.python.org/3.14/library/logging.config.html#logging-config-api) for further details.

The example below sets up two loggers, the root logger and a logger called “network”. Messages directed to the root logger will go to the system log via the syslog protocol, while messages to the “network” logger will be written into a `network.log` file that gets rotated once the log hits 1MB.

```python
import logging
import logging.config

configdict = {
 'version': 1,    # Configuration schema in use; must be 1 for now
 'formatters': {
     'standard': {
         'format': ('%(asctime)s %(name)-15s '
                    '%(levelname)-8s %(message)s')}},

 'handlers': {'netlog': {'backupCount': 10,
                     'class': 'logging.handlers.RotatingFileHandler',
                     'filename': '/logs/network.log',
                     'formatter': 'standard',
                     'level': 'INFO',
                     'maxBytes': 1000000},
              'syslog': {'class': 'logging.handlers.SysLogHandler',
                         'formatter': 'standard',
                         'level': 'ERROR'}},

 # Specify all the subordinate loggers
 'loggers': {
             'network': {
                         'handlers': ['netlog']
             }
 },
 # Specify properties of the root logger
 'root': {
          'handlers': ['syslog']
 },
}

# Set up configuration
logging.config.dictConfig(configdict)

# As an example, log two error messages
logger = logging.getLogger('/')
logger.error('Database not found')

netlogger = logging.getLogger('network')
netlogger.error('Connection failed')

```

The [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module received three smaller enhancements, each implemented by Vinay Sajip:

- The [`SysLogHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SysLogHandler) class now permits syslogging over TCP. Its constructor takes a *socktype* parameter that gives the socket type to use, either [`socket.SOCK_DGRAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_DGRAM) for UDP or [`socket.SOCK_STREAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_STREAM) for TCP. UDP stays the default protocol.

- [`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) instances picked up a [`getChild()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.getChild) method that fetches a descendant logger by a relative path. For instance, after obtaining a logger with `log = getLogger('app')`, a call to `log.getChild('network.listen')` matches `getLogger('app.network.listen')`.

- The [`LoggerAdapter`](https://docs.python.org/3.14/library/logging.html#logging.LoggerAdapter) class picked up an [`isEnabledFor()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.isEnabledFor) method that accepts a *level* and reports whether the underlying logger would handle a message of that importance level.

See also

[**PEP 391**](https://peps.python.org/pep-0391/) - Dictionary-Based Configuration For Logging

PEP written and implemented by Vinay Sajip.

[Subject index](INDEX.md) · [Previous source section](pep-389-the-argparse-module-for-parsing-command-lines.md) · [Next source section](pep-3106-dictionary-views.md) · [Release/subject declaration](the-future-for-python-2-x.md)
