# logging: `logging.basicConfig()`, `logging.shutdown()`, `logging.setLoggerClass()`, `logging.setLogRecordFactory()`

logging.basicConfig(***kwargs*)

Performs the elementary setup of the logging system, building a [`StreamHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.StreamHandler) with a default `Formatter` and attaching it to the root logger. Should no handlers be set up for the root logger, the functions `debug()`, `info()`, `warning()`, `error()` and `critical()` invoke `basicConfig()` on their own.

Where the root logger already carries configured handlers, this function takes no action, save when the keyword argument *force* has been set to `True`.

Note

Invoke this function from the main thread, before any further threads get going. Across Python releases before 2.7.1 and 3.2, invoking this function from several threads makes it possible (though seldom) for a handler to land on the root logger more than once, which produces surprising outcomes like repeated messages in the log.

Listed below are the keyword arguments that are accepted.

| Format | Description |
| --- | --- |
| *filename* | Asks that a `FileHandler` be built, using the given filename, in place of a `StreamHandler`. |
| *filemode* | Where *filename* is given, open that file under this mode. The fallback is `'a'`. |
| *format* | Apply the given format string for the handler. The fallback combines attributes `levelname`, `name` and `message` joined by colons. |
| *datefmt* | Apply the given date/time format, in the form `time.strftime()` accepts. |
| *style* | When *format* is given, apply this style to the format string. Pick `'%'`, `'{'` or `'$'` to mean printf-style, `str.format()` or `string.Template` in turn. The fallback is `'%'`. |
| *level* | Fix the root logger level at the given level. |
| *stream* | Apply the given stream when setting up the `StreamHandler`. Mind that this argument clashes with *filename* - supplying both triggers a `ValueError`. |
| *handlers* | When given, this should be an iterable of handlers already built to attach to the root logger. Whichever handlers lack a formatter get assigned the default one this function builds. Mind that this argument clashes with *filename* or *stream* - supplying both triggers a `ValueError`. |
| *force* | Where this keyword argument is given as true, every handler presently attached to the root logger gets removed and closed first, before the configuration proceeds per the other arguments. |
| *encoding* | Where this keyword argument accompanies *filename*, its value applies when the `FileHandler` is built, and hence when opening the output file. |
| *errors* | Where this keyword argument accompanies *filename*, its value applies when the `FileHandler` is built, and hence when opening the output file. Absent it, the value ‘backslashreplace’ applies. Mind that passing `None` forwards it straight to `open()`, where it gets handled just like passing ‘errors’. |

Changed in version 3.2: The *style* argument was introduced.

Changed in version 3.3: The *handlers* argument was introduced. Further checks were added to flag cases where clashing arguments get supplied (for instance *handlers* alongside *stream* or *filename*, or *stream* alongside *filename*).

Changed in version 3.8: The *force* argument was introduced.

Changed in version 3.9: The *encoding* and *errors* arguments were introduced.

 logging.shutdown()

Directs the logging system to carry out a tidy shutdown by flushing and closing every handler. Reserve this call for application exit, and refrain from any further use of the logging system once it has run.

As the logging module loads, it enrolls this function as an exit handler (refer to [`atexit`](https://docs.python.org/3.14/library/atexit.html#module-atexit)), so ordinarily you needn't arrange that by hand.

 logging.setLoggerClass(*klass*)

Instructs the logging system to employ the class *klass* whenever it builds a logger. That class ought to define `__init__()` so that a name argument alone is needed, and its `__init__()` ought to invoke `Logger.__init__()`. Applications that require custom logger behavior typically place this call ahead of building any loggers. Following this call, as at every other moment, refrain from building loggers directly from the subclass: keep on using the `logging.getLogger()` API to obtain your loggers.

 logging.setLogRecordFactory(*factory*)

Registers a callable used to build a `LogRecord`.

Parameters:

**factory** – The factory callable that will be employed to build a log record.

Added in version 3.2: This function, together with `getLogRecordFactory()`, was added to give developers greater control over the construction of the `LogRecord` standing in for a logging event.

The factory has the following signature:

[Subject index](INDEX.md) · [Previous](logging-log-to-logging-makelogrecord.md) · [Continue](factory.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Owning module, declaration or section: Module-Level Functions](logging-getlogger-to-logging-exception.md)
