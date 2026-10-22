# logging.handlers.BaseRotatingHandler: `rotation_filename()`, `rotate()`

namer

When this attribute is set to a callable, the `rotation_filename()` method hands off to that callable. The parameters fed to the callable are the ones fed to `rotation_filename()`.

Note

The namer function gets called a fair number of times during rollover, so keep it as plain and as fast as you can. It should likewise yield identical output every time for a given input, or else the rollover behaviour may not act as expected.

It's also worth pointing out that you should take care, when using a namer, to keep certain attributes in the filename that are relied on during rotation. For instance, `RotatingFileHandler` counts on having a set of log files whose names carry consecutive integers, so that rotation behaves as expected, while `TimedRotatingFileHandler` removes old log files (based on the `backupCount` parameter handed to the handler's initializer) by working out the oldest files to remove. For that to happen, the filenames must be sortable by the date/time portion of the filename, and a namer has to honor this. (Should you want a namer that doesn't honor this scheme, it will have to be used within a subclass of `TimedRotatingFileHandler` that overrides the `getFilesToDelete()` method to suit the custom naming scheme.)

Added in version 3.3.

 rotator

When this attribute is set to a callable, the `rotate()` method hands off to that callable. The parameters fed to the callable are the ones fed to `rotate()`.

Added in version 3.3.

 rotation_filename(*default_name*)

Modify the filename of a log file when rotating.

This is supplied so that a custom filename can be provided.

The default implementation invokes the 'namer' attribute of the handler, when it's callable, passing it the default name. Should the attribute not be callable (with `None` as the default), the name comes back unchanged.

Parameters:

**default_name** – The default name for the log file.

Added in version 3.3.

 rotate(*source*, *dest*)

When rotating, rotate the current log.

The default implementation invokes the 'rotator' attribute of the handler, when it's callable, passing it the source and dest arguments. Should the attribute not be callable (with `None` as the default), the source is simply renamed to the destination.

Parameters:

- **source** – The source filename. Typically this is the base filename, e.g. ‘test.log’.

- **dest** – The destination filename. Typically this is whatever the source rotates to, e.g. ‘test.log.1’.

Added in version 3.3.

These attributes exist to spare you from subclassing — you can reuse the same callables for instances of `RotatingFileHandler` and `TimedRotatingFileHandler`. Should either the namer or rotator callable raise an exception, it gets handled just like any other exception during an `emit()` call, that is, by way of the handler's `handleError()` method.

When you need to make more substantial changes to rotation processing, you can override the methods.

For an illustration, see [Using a rotator and namer to customize log rotation processing](https://docs.python.org/3.14/howto/logging-cookbook.html#cookbook-rotator-namer).

[Subject index](INDEX.md) · [Previous](logging-handlers-baserotatinghandler-class.md) · [Continue](logging-handlers-rotatingfilehandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.handlers.BaseRotatingHandler](logging-handlers-baserotatinghandler-class.md) · [Owning module, declaration or section: BaseRotatingHandler](logging-handlers-baserotatinghandler-class.md)
