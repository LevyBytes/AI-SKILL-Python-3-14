# logging.LoggerAdapter: `process()`

process(*msg*, *kwargs*)

Alters the message and/or keyword arguments handed to a logging call so as to insert contextual information. This implementation takes whatever object was passed as *extra* to the constructor and adds it to *kwargs* under the key "extra". The return value is a (*msg*, *kwargs*) tuple holding the (possibly altered) versions of the arguments passed in.

 manager

Delegates to the underlying `manager` on *logger*.

 _log

Delegates to the underlying `_log()` method on *logger*.

Beyond the above, `LoggerAdapter` supports the following methods of `Logger`: `debug()`, `info()`, `warning()`, `error()`, `exception()`, `critical()`, `log()`, `isEnabledFor()`, `getEffectiveLevel()`, `setLevel()` and `hasHandlers()`. These methods carry the same signatures as their counterparts in `Logger`, so the two kinds of instances are interchangeable.

Changed in version 3.2: `LoggerAdapter` gained the `isEnabledFor()`, `getEffectiveLevel()`, `setLevel()` and `hasHandlers()` methods. Each of these methods delegates to the underlying logger.

Changed in version 3.6: The `manager` attribute and the `_log()` method were added; both delegate to the underlying logger and make it possible to nest adapters.

Changed in version 3.10: The *extra* argument is now optional.

Changed in version 3.13: The *merge_extra* parameter was added.

[Subject index](INDEX.md) · [Previous](logging-loggeradapter-class.md) · [Continue](thread-safety.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Owning module, declaration or section: logging.LoggerAdapter](logging-loggeradapter-class.md) · [Owning module, declaration or section: LoggerAdapter Objects](logging-loggeradapter-class.md)
