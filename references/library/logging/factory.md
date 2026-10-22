# logging: LogRecord factory callable signature and parameters

`factory(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)`

>

name:

The logger name.

level:

The logging level (numeric).

fn:

The full pathname of the file where the logging call was made.

lno:

The line number in the file where the logging call was made.

msg:

The logging message.

args:

The arguments for the logging message.

exc_info:

An exception tuple, or `None`.

func:

The name of the function or method which invoked the logging call.

sinfo:

A stack traceback such as is provided by [`traceback.print_stack()`](https://docs.python.org/3.14/library/traceback.html#traceback.print_stack), showing the call hierarchy.

kwargs:

Additional keyword arguments.

[Subject index](INDEX.md) · [Previous](logging-basicconfig-to-logging-setlogrecordfactory.md) · [Continue](logging-lastresort-to-logging-raiseexceptions.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Owning module, declaration or section: Module-Level Functions](logging-getlogger-to-logging-exception.md)
