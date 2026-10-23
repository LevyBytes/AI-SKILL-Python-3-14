# logging - Module-Level Attributes

### Module-Level Attributes

 logging.lastResort

A “handler of last resort” can be reached through this attribute. It is a [`StreamHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.StreamHandler) that writes to `sys.stderr` at a level of `WARNING`, and it steps in to handle logging events whenever no logging configuration exists. The net effect is simply to emit the message to `sys.stderr`. This supersedes the former error message that read “no handlers could be found for logger XYZ”. Should you want that former behaviour back for whatever reason, you can set `lastResort` to `None`.

Added in version 3.2.

 logging.raiseExceptions

Consulted to decide whether exceptions arising during handling get propagated.

Default: `True`.

When `raiseExceptions` is `False`, exceptions are quietly swallowed. That suits a logging system in most cases - the bulk of users won't care about faults within the logging system, being far more concerned with faults in the application.

[Subject index](INDEX.md) · [Previous](factory.md) · [Continue](logging-capturewarnings.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md)
