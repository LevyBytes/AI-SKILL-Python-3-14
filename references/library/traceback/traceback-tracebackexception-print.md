# traceback.TracebackException: `from_exception()`, `print()`

__cause__

A `TracebackException` of the original [`__cause__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__cause__).

 __context__

A `TracebackException` of the original [`__context__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__context__).

 exceptions

When `self` stands for an [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup), this field carries a list of `TracebackException` instances standing for the nested exceptions. In every other case it is `None`.

Added in version 3.11.

 __suppress_context__

The [`__suppress_context__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__suppress_context__) value from the original exception.

 __notes__

The [`__notes__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__notes__) value taken from the original exception, or `None` when that exception carries no notes. Whenever it is not `None`, it is rendered in the traceback following the exception string.

Added in version 3.11.

 stack

A `StackSummary` representing the traceback.

 exc_type

The class of the original exception.

Deprecated since version 3.13.

 exc_type_str

String display of the class of the original exception.

Added in version 3.13.

 filename

For syntax errors - the file name where the error occurred.

 lineno

For syntax errors - the line number where the error occurred.

 end_lineno

For syntax errors - the ending line number at which the error arose. May be `None` when absent.

Added in version 3.10.

 text

For syntax errors - the text where the error occurred.

 offset

For syntax errors - the offset into the text where the error occurred.

 end_offset

For syntax errors - the ending offset within the text at which the error arose. May be `None` when absent.

Added in version 3.10.

 msg

For syntax errors - the compiler error message.

 *classmethod *`from_exception(*exc*, ***, *limit=None*, *lookup_lines=True*, *capture_locals=False*, *compact=False*, *max_group_width=15*, *max_group_depth=10*)`

Record an exception so it can be rendered later. *limit*, *lookup_lines* and *capture_locals* match those in the `StackSummary` class.

Keep in mind that captured locals also appear within the traceback.

 print(***, *file=None*, *chain=True*)

Write to *file* (defaulting to `sys.stderr`) the exception details produced by [`format()`](https://docs.python.org/3.14/library/functions.html#format).

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](traceback-tracebackexception-class.md) · [Continue](traceback-exception-formatting.md) · [Owning module, declaration or section: traceback](traceback-print-or-retrieve-a-stack-traceback.md) · [Owning module, declaration or section: traceback.TracebackException](traceback-tracebackexception-class.md) · [Owning module, declaration or section: `TracebackException` Objects](traceback-tracebackexception-class.md)
