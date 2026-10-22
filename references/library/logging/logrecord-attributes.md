# logging — LogRecord attributes

### LogRecord attributes

The LogRecord carries a number of attributes, most of them derived from the constructor's parameters. (Note that the names do not always line up exactly between the LogRecord constructor parameters and the LogRecord attributes.) You can use these attributes to merge data from the record into the format string. The table below lists (in alphabetical order) the attribute names, what they mean, and the matching placeholder in a %-style format string.

When you are using {}-formatting ([`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format)), you can put `{attrname}` as the placeholder in the format string. When you are using $-formatting ([`string.Template`](https://docs.python.org/3.14/library/string.html#string.Template)), use the form `${attrname}`. In both cases, naturally, swap `attrname` for the actual attribute name you want to use.

For {}-formatting, you can give formatting flags by placing them after the attribute name, a colon dividing them from it. As an example: a placeholder of `{msecs:03.0f}` would render a millisecond value of `4` as `004`. Turn to the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) documentation for full details on the options open to you.

| Attribute name | Format | Description |
| --- | --- | --- |
| args | You shouldn't need to format this yourself. | The tuple of arguments merged into `msg` so as to produce `message`, or else a dict whose values drive the merge (where there is a single argument and it happens to be a dictionary). |
| asctime | `%(asctime)s` | Human-readable time at which the `LogRecord` was created. By default this takes the form "2003-07-08 16:49:45,896" (whatever follows the comma being the millisecond portion of the time). |
| created | `%(created)f` | Time at which the `LogRecord` was created (the value `time.time_ns()` / 1e9 returns). |
| exc_info | You shouldn't need to format this yourself. | Exception tuple (?? la `sys.exc_info`) or, if no exception has occurred, `None`. |
| exc_text | You shouldn't need to format this yourself. | Exception information rendered into a string. `Formatter.format()` sets this on invocation, leaving it `None` where no exception has occurred. |
| filename | `%(filename)s` | Filename portion of `pathname`. |
| funcName | `%(funcName)s` | Name of function containing the logging call. |
| levelname | `%(levelname)s` | Text logging level for the message (`'DEBUG'`, `'INFO'`, `'WARNING'`, `'ERROR'`, `'CRITICAL'`). |
| levelno | `%(levelno)s` | Numeric logging level for the message (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`). |
| lineno | `%(lineno)d` | Source line number at which the logging call was issued (if available). |
| message | `%(message)s` | The logged message, worked out as `msg % args`. `Formatter.format()` sets this on invocation. |
| module | `%(module)s` | Module (name portion of `filename`). |
| msecs | `%(msecs)d` | Millisecond portion of the time when the `LogRecord` was created. |
| msg | You shouldn't need to format this yourself. | The format string handed to the original logging call. Merged with `args` so as to produce `message`, or else an arbitrary object (see Using arbitrary objects as messages). |
| name | `%(name)s` | Name of the logger used to log the call. |
| pathname | `%(pathname)s` | Full pathname of the source file at which the logging call was issued (if available). |
| process | `%(process)d` | Process ID (if available). |
| processName | `%(processName)s` | Process name (if available). |
| relativeCreated | `%(relativeCreated)d` | Time in milliseconds at which the LogRecord was created, taken relative to when the logging module was loaded. |
| stack_info | You shouldn't need to format this yourself. | Stack frame information (where available) reaching from the bottom of the current thread's stack, up to and including the stack frame of whichever logging call brought this record into being. |
| thread | `%(thread)d` | Thread ID (if available). |
| threadName | `%(threadName)s` | Thread name (if available). |
| taskName | `%(taskName)s` | `asyncio.Task` name (if available). |

Changed in version 3.1: *processName* was added.

Changed in version 3.12: *taskName* was added.

[Subject index](INDEX.md) · [Previous](logging-logrecord-getmessage.md) · [Continue](logging-loggeradapter-class.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md)
