# Complete conditional logging decorator demonstration

What the script does is set things up so that `foo` is wrapped by a decorator that performs the conditional logging we need. That decorator accepts a logger argument and, while the wrapped function runs, hooks up a memory handler. You can further configure the decorator by supplying a target handler, the level that triggers a flush, and how many records the buffer can hold before flushing. When omitted, these fall back to a [`StreamHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.StreamHandler) that emits to `sys.stderr`, `logging.ERROR` and `100` in that order.

Here's the script:

```python
import logging
from logging.handlers import MemoryHandler
import sys

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def log_if_errors(logger, target_handler=None, flush_level=None, capacity=None):
    if target_handler is None:
        target_handler = logging.StreamHandler()
    if flush_level is None:
        flush_level = logging.ERROR
    if capacity is None:
        capacity = 100
    handler = MemoryHandler(capacity, flushLevel=flush_level, target=target_handler)

    def decorator(fn):
        def wrapper(*args, **kwargs):
            logger.addHandler(handler)
            try:
                return fn(*args, **kwargs)
            except Exception:
                logger.exception('call failed')
                raise
            finally:
                super(MemoryHandler, handler).flush()
                logger.removeHandler(handler)
        return wrapper

    return decorator

def write_line(s):
    sys.stderr.write('%s\n' % s)

def foo(fail=False):
    write_line('about to log at DEBUG ...')
    logger.debug('Actually logged at DEBUG')
    write_line('about to log at INFO ...')
    logger.info('Actually logged at INFO')
    write_line('about to log at WARNING ...')
    logger.warning('Actually logged at WARNING')
    if fail:
        write_line('about to log at ERROR ...')
        logger.error('Actually logged at ERROR')
        write_line('about to log at CRITICAL ...')
        logger.critical('Actually logged at CRITICAL')
    return fail

decorated_foo = log_if_errors(logger)(foo)

if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)
    write_line('Calling undecorated foo with False')
    assert not foo(False)
    write_line('Calling undecorated foo with True')
    assert foo(True)
    write_line('Calling decorated foo with False')
    assert not decorated_foo(False)
    write_line('Calling decorated foo with True')
    assert decorated_foo(True)

```

[Subject index](INDEX.md) · [Previous source owning section](buffering-logging-messages-and-outputting-them-conditionally.md) · [Conditional buffer flush output and decorator syntax](conditional-buffer-flush-output-and-decorator-syntax.md) · [Following source context](conditional-buffer-flush-output-and-decorator-syntax.md)
