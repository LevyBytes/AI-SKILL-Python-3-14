# logging: `logging.Logger`

### Logger Objects

These attributes and methods belong to Loggers. Be aware that Loggers should *NEVER* be instantiated directly; instead always go through the module-level function `logging.getLogger(name)`. Repeated calls to `getLogger()` using the same name will invariably hand back a reference to the very same Logger object.

The `name` may well be a period-separated hierarchical value, like `foo.bar.baz` (although it might equally be just plain `foo`, for instance). Loggers situated further down the hierarchical list count as children of the loggers above them in the list. To illustrate, given a logger whose name is `foo`, loggers whose names are `foo.bar`, `foo.bar.baz`, and `foo.bam` are all descendants of `foo`. On top of that, every logger descends from the root logger. The logger name hierarchy parallels the Python package hierarchy, and matches it exactly when you arrange your loggers on a per-module basis using the recommended construction `logging.getLogger(__name__)`. That holds because within a module, `__name__` is the module's name in the Python package namespace.

 *class *logging.Logger

 name

This is the logger's name, the very value handed to `getLogger()` to fetch the logger.

Note

This attribute should be treated as read-only.

[Subject index](INDEX.md) · [Previous](logging-logging-facility-for-python.md) · [Continue](logging-logger-setlevel-to-logging-logger-getchildren.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md)
