# logging: `logging.log()`, `logging.disable()`, `logging.addLevelName()`, `logging.getLevelNamesMapping()`, `logging.getLevelName()`, `logging.getHandlerByName()`, `logging.getHandlerNames()`, `logging.makeLogRecord()`

Emits a message at the `ERROR` level on the root logger. Aside from that level, its arguments and semantics match those of `debug()`. Exception details are appended to the log message. Restrict calls to this function to within an exception handler.

 logging.log(*level*, *msg*, **args*, ***kwargs*)

Emits a message at the level *level* on the root logger. Apart from that, its arguments and semantics match those of `debug()`.

 logging.disable(*level=CRITICAL*)

Establishes an override level *level* spanning every logger, and this override wins out over each logger's individual level. This call comes in handy whenever you want to dial back logging output briefly across the entire application. What it does is suppress every logging call whose severity is *level* or lower, meaning that passing INFO would drop both INFO and DEBUG events, while WARNING and higher severities still get handled per the logger's effective level. Calling `logging.disable(logging.NOTSET)` clears the override entirely, returning logging output to depend once more on each individual logger's effective level.

Be aware that should you have created any custom logging level above `CRITICAL` (a practice we discourage), the default value for the *level* parameter won't be safe to depend on, and you'll need to pass a fitting value yourself.

Changed in version 3.7: The *level* parameter was given the default `CRITICAL`. Consult [bpo-28524](https://bugs.python.org/issue?@action=redirect&bpo=28524) for further details on this revision.

 logging.addLevelName(*level*, *levelName*)

Binds level *level* to the text *levelName* inside an internal dictionary, which serves to translate numeric levels into a textual form, such as when a `Formatter` renders a message. You can likewise leverage this function to declare custom levels of your own. The sole restrictions are that every level in use has to be registered through this function, that levels be positive integers, and that they grow in step with increasing severity.

Note

Should you be considering custom levels of your own, do consult the [Custom Levels](https://docs.python.org/3.14/howto/logging.html#custom-levels) section.

 logging.getLevelNamesMapping()

Hands back a mapping that pairs level names with the logging levels they denote. So, for instance, the string “CRITICAL” resolves to `CRITICAL`. Each invocation of this function produces a fresh copy of that mapping from an internal one.

Added in version 3.11.

 logging.getLevelName(*level*)

Hands back either the textual or numeric form of the logging level *level*.

When *level* is among the built-in levels `CRITICAL`, `ERROR`, `WARNING`, `INFO` or `DEBUG`, you receive the matching string. Where you have paired levels with names through `addLevelName()`, the name you tied to *level* comes back. Should a numeric value matching one of the established levels be supplied, its corresponding string form is what you get.

This *level* parameter will additionally take a string form of the level, for instance ‘INFO’. Given that input, this function hands back the matching numeric value of the level.

Where no matching numeric or string value is provided, the string ‘Level %s’ % level comes back.

Note

Internally, levels are integers (since the logging logic has to compare them). This function exists to translate back and forth between an integer level and the level name shown in the formatted log output by way of the `%(levelname)s` format specifier (refer to LogRecord attributes), and the reverse direction too.

Changed in version 3.4: With Python releases predating 3.4, this function would also accept a text level and hand back the level's matching numeric value. That undocumented behaviour was judged a mistake and dropped in Python 3.4, then brought back in 3.4.2 to keep backward compatibility intact.

 logging.getHandlerByName(*name*)

Hands back a handler bearing the given *name*, or `None` when no handler carries that name.

Added in version 3.12.

 logging.getHandlerNames()

Hands back an immutable set holding every known handler name.

Added in version 3.12.

 logging.makeLogRecord(*attrdict*)

Builds and hands back a fresh `LogRecord` instance with attributes drawn from *attrdict*. The function proves handy when you take a pickled `LogRecord` attribute dictionary, delivered across a socket, and rebuild it as a `LogRecord` instance on the receiving side.

[Subject index](INDEX.md) · [Continue](logging-basicconfig-to-logging-setlogrecordfactory.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Owning module, declaration or section: Module-Level Functions](logging-getlogger-to-logging-exception.md) · [Owning module, declaration or section: logging.exception](logging-getlogger-to-logging-exception.md) · [Preceding source contract and version conditions](logging-getlogger-to-logging-exception.md)
