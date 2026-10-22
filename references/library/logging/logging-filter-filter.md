# logging.Filter: `filter()`

filter(*record*)

Is the given record to be logged? Returns false for no, true for yes. Filters may either alter log records in-place or return a wholly different record instance that will take the place of the original log record in any later processing of the event.

Note that handler-attached filters are consulted before the handler emits an event, while logger-attached filters are consulted at the moment an event is logged (using `debug()`, `info()`, etc.), prior to dispatching an event to handlers. The upshot is that events coming from descendant loggers escape a logger's filter setting, unless that filter has been applied to those descendant loggers too.

You do not actually have to subclass `Filter`: you can hand over any instance that has a `filter` method with the same semantics.

Changed in version 3.2: There is no need to build specialized `Filter` classes, nor to use other classes carrying a `filter` method: a function (or other callable) can act as a filter. The filtering logic checks whether the filter object owns a `filter` attribute: where it does, the object is taken to be a `Filter` and its `filter()` method runs. Otherwise, the object is taken to be a callable and is called with the record as its lone parameter. Whatever it returns should match what `filter()` returns.

Changed in version 3.12: From a filter you may now return a `LogRecord` instance to replace the log record instead of altering it in place. This lets filters attached to a `Handler` alter the log record ahead of its emission, with no side effects on other handlers.

Even though filters serve mainly to filter records against criteria more sophisticated than levels, they get to see every record processed by the handler or logger they are attached to: this can prove handy when you want to do things like tallying how many records a particular logger or handler processed, or adding, changing or removing attributes on the `LogRecord` under processing. Plainly, changing the LogRecord calls for some care, yet it does permit the injection of contextual information into logs (see [Using Filters to impart contextual information](https://docs.python.org/3.14/howto/logging-cookbook.html#filters-contextual)).

[Subject index](INDEX.md) · [Previous](logging-filter-class.md) · [Continue](logging-logrecord-class.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Owning module, declaration or section: logging.Filter](logging-filter-class.md) · [Owning module, declaration or section: Filter Objects](logging-filter-class.md)
