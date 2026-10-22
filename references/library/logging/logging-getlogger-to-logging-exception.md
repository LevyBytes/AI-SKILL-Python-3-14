# logging: `logging.getLogger()`, `logging.getLoggerClass()`, `logging.getLogRecordFactory()`, `logging.debug()`, `logging.info()`, `logging.warning()`, `logging.error()`, `logging.critical()`, `logging.exception()`

### Module-Level Functions

Alongside the classes described above, a number of module-level functions exist.

 logging.getLogger(*name=None*)

Return a logger bearing the given name or, when name is `None`, return the hierarchy's root logger. When supplied, the name is usually a hierarchical, dot-separated name such as *"a"*, *"a.b"* or *"a.b.c.d"*. The choice of these names rests entirely with the developer who is using logging, though using `__name__` is recommended unless you have a specific reason not to, which Logger Objects covers.

Every call to this function with a given name returns the same logger instance. This means logger instances never need to be passed between the different parts of an application.

 logging.getLoggerClass()

Return either the standard `Logger` class, or the most recent class passed to `setLoggerClass()`. You may call this function from inside a new class definition, so as to ensure that installing a customized `Logger` class leaves intact any customizations other code has already put in place. For example:

```python
class MyLogger(logging.getLoggerClass()):
    # ... override behaviour here

```

 logging.getLogRecordFactory()

Return a callable which is used to create a `LogRecord`.

Added in version 3.2: This function, together with `setLogRecordFactory()`, was supplied to give developers more say over the way the `LogRecord` standing for a logging event gets constructed.

See `setLogRecordFactory()` for more information about the how the factory is called.

 logging.debug(*msg*, **args*, ***kwargs*)

This convenience function invokes `Logger.debug()` on the root logger. Argument handling matches, in every respect, what that method lays out.

The one difference: where the root logger holds no handlers, `basicConfig()` runs first, before `debug` is called on the root logger.

Across very short scripts or quick demonstrations of `logging` facilities, `debug` along with the other module-level functions may prove convenient. Yet most programs will want to govern the logging configuration carefully and explicitly, and should therefore lean toward building a module-level logger and invoking `Logger.debug()` (or other level-specific methods) upon it, just as the opening of this documentation lays out.

 logging.info(*msg*, **args*, ***kwargs*)

Logs a message at level `INFO` on the root logger. In every other respect the arguments and behavior match `debug()`.

 logging.warning(*msg*, **args*, ***kwargs*)

Logs a message at level `WARNING` on the root logger. Apart from that, the arguments and behavior are identical to `debug()`.

Note

An obsolete function `warn` exists whose behavior is functionally identical to `warning`. Since `warn` is deprecated, please refrain from using it - reach for `warning` instead.

 logging.error(*msg*, **args*, ***kwargs*)

Logs a message at level `ERROR` on the root logger. Otherwise its arguments and behavior coincide with those of `debug()`.

 logging.critical(*msg*, **args*, ***kwargs*)

Logs a message at level `CRITICAL` on the root logger. In all other respects the arguments and behavior follow `debug()`.

 logging.exception(*msg*, **args*, ***kwargs*)

[Subject index](INDEX.md) · [Previous](thread-safety.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Required continuation of the source contract](logging-log-to-logging-makelogrecord.md)
