# 11.5. Logging

### 11.5. Logging

A flexible, fully featured logging facility is exposed by the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module. In the most basic case, log entries land in a file or go to `sys.stderr`:

```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

```

The output that results is:

```none
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down

```

Out of the box, debug and informational entries are held back and everything emitted goes to standard error. Alternative destinations include sending entries by email, over datagrams, through sockets, or to an HTTP Server. You can add new filters that pick a destination according to message priority: [`DEBUG`](https://docs.python.org/3.14/library/logging.html#logging.DEBUG), [`INFO`](https://docs.python.org/3.14/library/logging.html#logging.INFO), [`WARNING`](https://docs.python.org/3.14/library/logging.html#logging.WARNING), [`ERROR`](https://docs.python.org/3.14/library/logging.html#logging.ERROR), and [`CRITICAL`](https://docs.python.org/3.14/library/logging.html#logging.CRITICAL).

You may set up the logging system straight from Python, or load it from a configuration file the user can edit, letting you customize logging without touching the application.

[Subject index](INDEX.md) · [Previous source section](multi-threading.md) · [Following source section](weak-references.md)
