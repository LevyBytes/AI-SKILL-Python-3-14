# LoggerWriter file-like adapter and stdout/stderr routing

### How to treat a logger like an output stream

On occasion you must talk to a third-party API that wants a file-like object to write into, yet you would rather route that API's output toward a logger. A class that wraps a logger behind a file-like API achieves this. The brief script below demonstrates one such class:

```python
import logging

class LoggerWriter:
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def write(self, message):
        if message != '\n':  # avoid printing bare newlines, if you like
            self.logger.log(self.level, message)

    def flush(self):
        # doesn't actually do anything, but might be expected of a file-like
        # object - so optional depending on your situation
        pass

    def close(self):
        # doesn't actually do anything, but might be expected of a file-like
        # object - so optional depending on your situation. You might want
        # to set a flag so that later calls to write raise an exception
        pass

def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('demo')
    info_fp = LoggerWriter(logger, logging.INFO)
    debug_fp = LoggerWriter(logger, logging.DEBUG)
    print('An INFO message', file=info_fp)
    print('A DEBUG message', file=debug_fp)

if __name__ == "__main__":
    main()

```

Running this script prints

```text
INFO:demo:An INFO message
DEBUG:demo:A DEBUG message

```

`LoggerWriter` can equally be used to reroute `sys.stdout` and `sys.stderr`, along these lines:

```python
import sys

sys.stdout = LoggerWriter(logger, logging.INFO)
sys.stderr = LoggerWriter(logger, logging.WARNING)

```

Carry this out *after* you have set logging up to suit your needs. The [`basicConfig()`](https://docs.python.org/3.14/library/logging.html#logging.basicConfig) call in the example above handles that (relying on the `sys.stderr` value *before* a `LoggerWriter` instance replaces it). You would then see this sort of outcome:

```pycon
>>> print('Foo')
INFO:demo:Foo
>>> print('Bar', file=sys.stderr)
WARNING:demo:Bar
>>>

```

Naturally the examples above render output in the format that [`basicConfig()`](https://docs.python.org/3.14/library/logging.html#logging.basicConfig) applies, yet a different formatter is available when you set up logging.

[Subject index](INDEX.md) · [Fragmented traceback writes and BufferingLoggerWriter correction](fragmented-traceback-buffering-writer.md) · [Previous source context](logging-to-syslog-with-rfc5424-support.md) · [Following source context](fragmented-traceback-buffering-writer.md)
