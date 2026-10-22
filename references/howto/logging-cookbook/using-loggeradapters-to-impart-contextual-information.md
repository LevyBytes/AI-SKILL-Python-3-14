# Using LoggerAdapters to impart contextual information

### Using LoggerAdapters to impart contextual information

A straightforward route for attaching contextual information so it accompanies the logged event data is the [`LoggerAdapter`](https://docs.python.org/3.14/library/logging.html#logging.LoggerAdapter) class. It's built to resemble a [`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger), letting you invoke [`debug()`](https://docs.python.org/3.14/library/logging.html#logging.debug), [`info()`](https://docs.python.org/3.14/library/logging.html#logging.info), [`warning()`](https://docs.python.org/3.14/library/logging.html#logging.warning), [`error()`](https://docs.python.org/3.14/library/logging.html#logging.error), [`exception()`](https://docs.python.org/3.14/library/logging.html#logging.exception), [`critical()`](https://docs.python.org/3.14/library/logging.html#logging.critical) and [`log()`](https://docs.python.org/3.14/library/logging.html#logging.log). Because these carry the same signatures as the matching methods on `Logger`, the two kinds of instances can be swapped for one another.

To build an instance of [`LoggerAdapter`](https://docs.python.org/3.14/library/logging.html#logging.LoggerAdapter), you hand it a [`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) instance together with a dict-like object holding your contextual information. Whenever you invoke one of the logging methods on a `LoggerAdapter` instance, it forwards the call to the underlying `Logger` instance that was given to its constructor, and sees to it that the contextual information rides along in the forwarded call. Below is an excerpt from the `LoggerAdapter` source:

```python
def debug(self, msg, /, *args, **kwargs):
    """
    Delegate a debug call to the underlying logger, after adding
    contextual information from this adapter instance.
    """
    msg, kwargs = self.process(msg, kwargs)
    self.logger.debug(msg, *args, **kwargs)

```

It's the [`process()`](https://docs.python.org/3.14/library/logging.html#logging.LoggerAdapter.process) method on [`LoggerAdapter`](https://docs.python.org/3.14/library/logging.html#logging.LoggerAdapter) that merges the contextual information into the logging output. This method receives the message plus the keyword arguments from the logging call and returns (possibly) altered versions of both for use in the call to the underlying logger. By default the implementation leaves the message untouched, but it adds an 'extra' entry to the keyword arguments whose value is the dict-like object that was handed to the constructor. Naturally, if you happened to supply an 'extra' keyword argument when calling the adapter, it gets quietly overwritten.

The benefit of relying on 'extra' is that the entries from the dict-like object are folded into the [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) instance's __dict__, which lets you employ customized strings with your [`Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter) instances that recognize the keys of the dict-like object. Should you require a different approach — for instance if you'd like to add the contextual information before or after the message string — all you have to do is subclass [`LoggerAdapter`](https://docs.python.org/3.14/library/logging.html#logging.LoggerAdapter) and override [`process()`](https://docs.python.org/3.14/library/logging.html#logging.LoggerAdapter.process) to behave as you need. Here's a small example:

```python
class CustomAdapter(logging.LoggerAdapter):
    """
    This example adapter expects the passed in dict-like object to have a
    'connid' key, whose value in brackets is prepended to the log message.
    """
    def process(self, msg, kwargs):
        return '[%s] %s' % (self.extra['connid'], msg), kwargs

```

and here is how you'd put it to use:

```python
logger = logging.getLogger(__name__)
adapter = CustomAdapter(logger, {'connid': some_conn_id})

```

From then on, every event you send to the adapter will carry the value of `some_conn_id` prepended to its log messages.

[Subject index](INDEX.md) · [Previous source context](adding-contextual-information-to-your-logging-output.md) · [Following source context](using-objects-other-than-dicts-to-pass-contextual-information.md)
