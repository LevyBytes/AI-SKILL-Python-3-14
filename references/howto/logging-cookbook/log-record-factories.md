# LogRecord creation and factories

### Customizing `LogRecord`

A [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) instance stands in for each logging event. Once an event is logged and a logger's level does not screen it out, a `LogRecord` gets built, filled with details about that event, and then handed off to the handlers belonging to that logger (plus its ancestors, climbing the hierarchy up to and including the logger at which onward propagation is switched off). Prior to Python 3.2, this construction happened in only two spots:

- [`Logger.makeRecord()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.makeRecord), invoked during the regular course of logging an event. It called [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) straight away to build an instance.

- [`makeLogRecord()`](https://docs.python.org/3.14/library/logging.html#logging.makeLogRecord), to which you hand a dictionary of attributes for adding to the LogRecord. The usual trigger is the arrival of a fitting dictionary over the network (say, in pickle form through a [`SocketHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SocketHandler), or in JSON form through an [`HTTPHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.HTTPHandler)).

As a rule, that has meant that doing anything out of the ordinary with a [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) forced you into one of the options below.

- Write your own [`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) subclass that overrides [`Logger.makeRecord()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.makeRecord), and register it via [`setLoggerClass()`](https://docs.python.org/3.14/library/logging.html#logging.setLoggerClass) ahead of instantiating any loggers you care about.

- Attach a [`Filter`](https://docs.python.org/3.14/library/logging.html#logging.Filter) to a logger or handler that performs the special manipulation you require whenever its [`filter()`](https://docs.python.org/3.14/library/logging.html#logging.Filter.filter) method runs.

Where, for instance, multiple libraries each wanted to do something different, the first approach would prove somewhat awkward. Every one of them would try to register its own [`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) subclass, and whichever did so last would prevail.

Though the second approach copes well enough across many situations, it stops you from, say, employing a specialized subclass of [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord). Library authors can place a suitable filter on their loggers, but they would need to remember doing so each time they brought in a new logger (which they would do merely by adding fresh packages or modules and writing

```python
logger = logging.getLogger(__name__)

```

at module level). That is likely one detail too many to keep track of. Developers might instead attach the filter to a [`NullHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.NullHandler) bound to their top-level logger, yet it would go uninvoked should an application developer bind a handler to a lower-level library logger — meaning that handler's output would not honor what the library developer intended.

From Python 3.2 onward, a factory you can nominate handles [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) creation. That factory is simply a callable you register through [`setLogRecordFactory()`](https://docs.python.org/3.14/library/logging.html#logging.setLogRecordFactory) and query through [`getLogRecordFactory()`](https://docs.python.org/3.14/library/logging.html#logging.getLogRecordFactory). It gets called with the very signature of the `LogRecord` constructor, since [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) is the factory's default.

With this approach a custom factory governs every facet of LogRecord creation. You might, for instance, hand back a subclass, or simply tack on a few extra attributes to the record after it is built, following a pattern along these lines:

```python
old_factory = logging.getLogRecordFactory()

def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.custom_attribute = 0xdecafbad
    return record

logging.setLogRecordFactory(record_factory)

```

Such a pattern lets various libraries link factories one after another, and provided they neither clobber one another's attributes nor accidentally clobber the attributes supplied as standard, nothing unexpected should occur. Do keep in mind, though, that every link in the chain piles run-time overhead onto all logging operations, so reach for the technique only where a [`Filter`](https://docs.python.org/3.14/library/logging.html#logging.Filter) fails to deliver what you want.

The Python snippets use `import logging`.

[Subject index](INDEX.md).
