# Using a context manager for selective logging

### Using a context manager for selective logging

Occasionally it's handy to adjust the logging configuration for a moment and then put it back once you're done. A context manager is the natural fit for saving and then restoring the logging state. The straightforward context manager below lets you optionally switch the logging level and attach a logging handler only within the scope it manages:

```python
import logging
import sys

class LoggingContext:
    def __init__(self, logger, level=None, handler=None, close=True):
        self.logger = logger
        self.level = level
        self.handler = handler
        self.close = close

    def __enter__(self):
        if self.level is not None:
            self.old_level = self.logger.level
            self.logger.setLevel(self.level)
        if self.handler:
            self.logger.addHandler(self.handler)

    def __exit__(self, et, ev, tb):
        if self.level is not None:
            self.logger.setLevel(self.old_level)
        if self.handler:
            self.logger.removeHandler(self.handler)
        if self.handler and self.close:
            self.handler.close()
        # implicit return of None => don't swallow exceptions

```

Provide a level value and the logger's level is set to it for the duration of the with block that the context manager governs. Provide a handler and it gets attached to the logger when the block is entered and detached when the block ends. You may additionally request that the manager close the handler when the block exits — handy when you have no further use for it.

To show this in action, we can append the following block of code to what's above:

```python
if __name__ == '__main__':
    logger = logging.getLogger('foo')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.INFO)
    logger.info('1. This should appear just once on stderr.')
    logger.debug('2. This should not appear.')
    with LoggingContext(logger, level=logging.DEBUG):
        logger.debug('3. This should appear once on stderr.')
    logger.debug('4. This should not appear.')
    h = logging.StreamHandler(sys.stdout)
    with LoggingContext(logger, level=logging.DEBUG, handler=h, close=True):
        logger.debug('5. This should appear twice - once on stderr and once on stdout.')
    logger.info('6. This should appear just once on stderr.')
    logger.debug('7. This should not appear.')

```

To begin with, the logger's level is `INFO`, which is why message #1 shows and message #2 is suppressed. Inside the next `with` block we briefly switch the level to `DEBUG`, so message #3 appears. Once that block ends, the level reverts to `INFO`, and message #4 stays hidden. The following `with` block again sets `DEBUG`, but this time also attaches a handler targeting `sys.stdout`. As a result, message #5 shows up twice on the console (once through `stderr`, once through `stdout`). When that `with` statement finishes, things are back to how they started, so message #6 appears (just as #1 did) while message #7 does not (just as #2 didn't).

Running the resulting script gives this:

```shell
$ python logctx.py
1. This should appear just once on stderr.
3. This should appear once on stderr.
5. This should appear twice - once on stderr and once on stdout.
5. This should appear twice - once on stderr and once on stdout.
6. This should appear just once on stderr.

```

Run it a second time, but route `stderr` to `/dev/null`, and what remains is the lone message sent to `stdout`:

```shell
$ python logctx.py 2>/dev/null
5. This should appear twice - once on stderr and once on stdout.

```

Yet again, now redirecting `stdout` to `/dev/null`, we obtain:

```shell
$ python logctx.py >/dev/null
1. This should appear just once on stderr.
3. This should appear once on stderr.
5. This should appear twice - once on stderr and once on stdout.
6. This should appear just once on stderr.

```

Here, the copy of message #5 destined for `stdout` is absent, which is exactly what we'd predict.

The technique outlined here can of course be extended — for instance, to attach logging filters for a short while. Bear in mind that the preceding code runs under Python 2 just as it does under Python 3.

[Subject index](INDEX.md) · [Previous source context](formatting-times-using-utc-via-configuration.md) · [Following source context](cli-logging-dispatcher-and-common-log-level-setup.md)
