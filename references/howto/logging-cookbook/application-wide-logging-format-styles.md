# Using particular formatting styles throughout your application

### Using particular formatting styles throughout your application

With Python 3.2, the [`Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter) acquired a `style` keyword parameter that, though it defaults to `%` for backward compatibility, permitted choosing `{` or `$` to enable the formatting techniques offered by [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) and [`string.Template`](https://docs.python.org/3.14/library/string.html#string.Template). Keep in mind this controls how logging messages are formatted for the final output to logs, and is entirely independent of how any single logging message gets constructed.

Logging calls ([`debug()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.debug), [`info()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.info) etc.) accept positional parameters solely for the logging message itself, while keyword parameters serve only to set options for how the logging call is handled (for example, the `exc_info` keyword parameter signalling that traceback information ought to be logged, or the `extra` keyword parameter signalling extra contextual information to attach to the log). Consequently you can't make logging calls directly in [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) or [`string.Template`](https://docs.python.org/3.14/library/string.html#string.Template) syntax, since under the hood the logging package applies %-formatting to combine the format string with the variable arguments. Altering this while keeping backward compatibility is impossible, given that every logging call already present in existing code relies on %-format strings.

People have proposed tying format styles to particular loggers, but that route too hits backward compatibility trouble, because any existing code might already use a given logger name together with %-formatting.

So that logging interoperates between any third-party libraries and your own code, formatting choices have to be made at the granularity of each individual logging call. That leaves a couple of avenues by which alternative formatting styles can be supported.

[Subject index](INDEX.md) · [Previous source context](handler-factory-version-and-external-name-configuration.md) · [Following source context](using-logrecord-factories.md)
