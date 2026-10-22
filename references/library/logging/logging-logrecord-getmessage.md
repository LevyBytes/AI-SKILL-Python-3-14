# logging.LogRecord: `getMessage()`

getMessage()

Returns the message for this `LogRecord` instance once any user-supplied arguments have been merged with the message. Where the logging call's user-supplied message argument is not a string, [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) gets called on it to coerce it into a string. This permits user-defined classes to serve as messages, where their `__str__` method may hand back the actual format string that ends up used.

Changed in version 3.2: Creating a `LogRecord` has grown more configurable through a factory that is used to build the record. You can set that factory using `getLogRecordFactory()` and `setLogRecordFactory()` (consult this for the factory's signature).

This functionality lets you inject your own values into a `LogRecord` at creation time. You can apply the following pattern:

```python
old_factory = logging.getLogRecordFactory()

def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.custom_attribute = 0xdecafbad
    return record

logging.setLogRecordFactory(record_factory)

```

With this pattern, several factories could be chained, and provided they do not overwrite one another's attributes or accidentally overwrite the standard attributes listed above, there should be no surprises.

[Subject index](INDEX.md) · [Previous](logging-logrecord-class.md) · [Continue](logrecord-attributes.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Owning module, declaration or section: logging.LogRecord](logging-logrecord-class.md) · [Owning module, declaration or section: LogRecord Objects](logging-logrecord-class.md)
