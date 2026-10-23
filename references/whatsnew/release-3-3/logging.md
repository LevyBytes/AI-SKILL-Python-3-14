# What's New In Python 3.3 / logging - logging, logging.handlers

### logging

An optional `handlers` argument now reaches the [`basicConfig()`](https://docs.python.org/3.14/library/logging.html#logging.basicConfig) function, accepting an iterable of handlers to attach to the root logger.

[`SysLogHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SysLogHandler) picks up a class level attribute named `append_nul` so you can decide whether the `NUL` (`\000`) byte is tacked onto syslog records; certain daemons demand it while others simply forward it into the log.

[Subject index](INDEX.md) · [Previous source section](itertools.md) · [Next source section](math.md) · [Release/subject declaration](summary-release-highlights.md)
