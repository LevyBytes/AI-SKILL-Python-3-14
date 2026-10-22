# logging / Logger Objects: `addFilter()`, `removeFilter()`, `filter()`, `addHandler()`, `removeHandler()`, `findCaller()`, `handle()`, `makeRecord()`, `hasHandlers()`

addFilter(*filter*)

Adds the specified filter *filter* to this logger.

 removeFilter(*filter*)

Removes the specified filter *filter* from this logger.

 filter(*record*)

Run this logger's filters against the record and hand back `True` when the record is to be processed. The filters are consulted one after another, until one of them yields a false value. When none yield a false value, the record will be processed (passed to handlers). When one yields a false value, no further processing of the record takes place.

 addHandler(*hdlr*)

Adds the specified handler *hdlr* to this logger.

 removeHandler(*hdlr*)

Removes the specified handler *hdlr* from this logger.

 findCaller(*stack_info=False*, *stacklevel=1*)

Locates the caller's source filename and line number. Returns a 4-element tuple holding the filename, the line number, the function name, plus stack information. That stack information comes back as `None` unless *stack_info* is `True`.

The *stacklevel* parameter arrives from code calling the `debug()` and other APIs. When it exceeds 1, the surplus serves to skip stack frames ahead of working out the values to be returned. This is generally helpful when logging APIs are called from helper/wrapper code, so that the information in the event log points not to the helper/wrapper code, but to the code that invokes it.

 handle(*record*)

Handles a record by passing it to every handler tied to this logger and its ancestors (up until a false value of *propagate* turns up). This method serves both unpickled records arriving from a socket and those built locally. Logger-level filtering is applied through `filter()`.

 makeRecord(*name*, *level*, *fn*, *lno*, *msg*, *args*, *exc_info*, *func=None*, *extra=None*, *sinfo=None*)

This is a factory method, overridable in subclasses, for building specialized `LogRecord` instances.

 hasHandlers()

Checks whether this logger has any handlers configured. It does so by looking for handlers across this logger and its parents in the logger hierarchy. Hands back `True` when a handler was found, otherwise `False`. The method gives up searching up the hierarchy as soon as a logger whose ‘propagate’ attribute is set to false turns up — that becomes the final logger inspected for the presence of handlers.

Added in version 3.2.

Changed in version 3.7: Loggers can now be pickled and unpickled.

[Subject index](INDEX.md) · [Previous](logging-logger-debug-to-logging-logger-exception.md) · [Continue](logging-levels.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Owning module, declaration or section: logging.Logger; name](logging-logger-class.md) · [Owning module, declaration or section: Logger Objects](logging-logger-class.md)
