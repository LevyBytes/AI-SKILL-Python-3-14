# logging: `logging.LogRecord`

### LogRecord Objects

`LogRecord` instances get created automatically by the `Logger` each time something is logged, and can be created by hand via `makeLogRecord()` (for example, from a pickled event received over the wire).

 *class *logging.LogRecord(*name*, *level*, *pathname*, *lineno*, *msg*, *args*, *exc_info*, *func=None*, *sinfo=None*)

Contains all the information pertinent to the event being logged.

The primary information arrives in *msg* and *args*, which are combined via `msg % args` to form the record's `message` attribute.

Parameters:

- **name** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)): The name of the logger that logged the event this `LogRecord` stands for. Note that the logger name carried on the `LogRecord` always holds this value, even though a handler attached to a different (ancestor) logger may be the one to emit it.

- **level** ([*int*](https://docs.python.org/3.14/library/functions.html#int)): The logging event's numeric level (for example `10` for `DEBUG`, `20` for `INFO`, etc). Note that this splits into *two* attributes on the LogRecord: `levelno` for the numeric value and `levelname` for the matching level name.

- **pathname** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)): The full string path of the source file in which the logging call occurred.

- **lineno** ([*int*](https://docs.python.org/3.14/library/functions.html#int)): The line number within the source file at which the logging call occurred.

- **msg** ([*Any*](https://docs.python.org/3.14/library/typing.html#typing.Any)): The event description message, which may be a %-format string carrying placeholders for variable data, or else an arbitrary object (see [Using arbitrary objects as messages](https://docs.python.org/3.14/howto/logging.html#arbitrary-object-messages)).

- **args** ([*tuple*](https://docs.python.org/3.14/library/stdtypes.html#tuple)* | *[*dict*](https://docs.python.org/3.14/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3.14/library/stdtypes.html#str)*, *[*Any*](https://docs.python.org/3.14/library/typing.html#typing.Any)*]*): Variable data to fold into the *msg* argument so as to arrive at the event description.

- **exc_info** ([*tuple*](https://docs.python.org/3.14/library/stdtypes.html#tuple)*[*[*type*](https://docs.python.org/3.14/library/functions.html#type)*[*[*BaseException*](https://docs.python.org/3.14/library/exceptions.html#BaseException)*]**, **BaseException**, *[*types.TracebackType*](https://docs.python.org/3.14/library/types.html#types.TracebackType)*] **| **None*): An exception tuple holding the current exception information, the way [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) returns it, or `None` where no exception information is on hand.

- **func** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)* | **None*): The name of the function or method out of which the logging call was invoked.

- **sinfo** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)* | **None*): A text string conveying stack information reaching from the base of the current thread's stack, up to the logging call.

[Subject index](INDEX.md) · [Previous](logging-filter-filter.md) · [Continue](logging-logrecord-getmessage.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md)
