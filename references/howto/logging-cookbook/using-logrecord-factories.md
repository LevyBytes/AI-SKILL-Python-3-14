# Using LogRecord factories

### Using LogRecord factories

In Python 3.2, alongside the [`Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter) changes noted above, the logging package picked up the capability to let users register their own [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) subclasses, by way of the [`setLogRecordFactory()`](https://docs.python.org/3.14/library/logging.html#logging.setLogRecordFactory) function. This lets you install your own subclass of `LogRecord` that does the Right Thing by overriding the [`getMessage()`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord.getMessage) method. The base class's version of this method is where the `msg % args` formatting takes place, and where you can drop in your alternate formatting; even so, take care to handle every formatting style and keep %-formatting as the default, so as to ensure interoperability with other code. You should also be careful to invoke `str(self.msg)`, exactly as the base implementation does.

See the reference documentation for [`setLogRecordFactory()`](https://docs.python.org/3.14/library/logging.html#logging.setLogRecordFactory) and [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) for further details.

[Subject index](INDEX.md) · [Previous source context](application-wide-logging-format-styles.md) · [Following source context](using-custom-message-objects.md)
