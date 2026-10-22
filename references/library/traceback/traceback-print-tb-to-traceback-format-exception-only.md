# traceback: Traceback printing and exception-only formatting

### Module-Level Functions

 traceback.print_tb(*tb*, *limit=None*, *file=None*)

When *limit* is positive, emit at most *limit* stack trace entries drawn from the [traceback object](https://docs.python.org/3.14/reference/datamodel.html#traceback-objects) *tb*, beginning at the caller's frame. When it is not positive, the final `abs(limit)` entries are emitted instead. Leaving *limit* unset or as `None` causes every entry to print. With *file* left out or set to `None`, output is directed to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr); otherwise supply an open [file](https://docs.python.org/3.14/glossary.html#term-file-object) or [file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object) that will collect the output.

Note

Be aware that *limit* here does not carry the same meaning as [`sys.tracebacklimit`](https://docs.python.org/3.14/library/sys.html#sys.tracebacklimit). Supplying a negative *limit* lines up with giving `sys.tracebacklimit` a positive value, while there is no `sys.tracebacklimit` setting that reproduces what a positive *limit* does.

Changed in version 3.5: Added negative *limit* support.

 traceback.print_exception(*exc*, */*, [*value*, *tb*, ]*limit=None*, *file=None*, *chain=True*)

Send the exception details together with stack trace entries from the [traceback object](https://docs.python.org/3.14/reference/datamodel.html#traceback-objects) *tb* out to *file*. The behaviour departs from `print_tb()` on these points:

- should *tb* not be `None`, a `Traceback (most recent call last):` header is written

- after the stack trace, the exception type along with *value* gets written

- if *type(value)* is [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) and *value* is shaped suitably, the offending line is shown with a caret marking roughly where on it the error sits.

As of Python 3.10 you may hand an exception object directly as the first argument rather than supplying *value* and *tb*. Should *value* and *tb* both be present, that first argument is disregarded so older code keeps working.

Here the optional *limit* argument behaves exactly as it does for `print_tb()`. When *chain* is true (its default), the routine also prints any chained exceptions (those reachable through the [`__cause__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__cause__) or [`__context__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__context__) attributes), matching how the interpreter renders an unhandled exception.

Changed in version 3.5: The *etype* argument is disregarded; its value is instead deduced from the type of *value*.

Changed in version 3.10: The *etype* parameter now goes by the name *exc* and has become positional-only.

 traceback.print_exc(*limit=None*, *file=None*, *chain=True*)

This is a shorthand for `print_exception(sys.exception(), limit=limit, file=file, chain=chain)`.

 traceback.print_last(*limit=None*, *file=None*, *chain=True*)

This is a shorthand for `print_exception(sys.last_exc, limit=limit, file=file, chain=chain)`. As a rule it functions only once an exception has bubbled up to an interactive prompt (see [`sys.last_exc`](https://docs.python.org/3.14/library/sys.html#sys.last_exc)).

 traceback.print_stack(*f=None*, *limit=None*, *file=None*)

When *limit* is positive, emit at most *limit* stack trace entries starting at the point of the call. When it is not positive, the last `abs(limit)` entries are emitted instead. If *limit* is left out or `None`, every entry prints. You may pass the optional *f* argument to nominate a different [stack frame](https://docs.python.org/3.14/reference/datamodel.html#frame-objects) as the starting point. The optional *file* argument carries the same meaning it has for `print_tb()`.

Changed in version 3.5: Added negative *limit* support.

 traceback.extract_tb(*tb*, *limit=None*)

Hand back a `StackSummary` object that holds a list of "pre-processed" stack trace entries pulled out of the [traceback object](https://docs.python.org/3.14/reference/datamodel.html#traceback-objects) *tb*. This comes in handy when you want to format stack traces differently. The optional *limit* argument carries the same meaning it has for `print_tb()`. Each "pre-processed" stack trace entry is a `FrameSummary` object whose attributes hold the data that a stack trace normally displays.

 traceback.extract_stack(*f=None*, *limit=None*)

Pull the raw traceback out of the current [stack frame](https://docs.python.org/3.14/reference/datamodel.html#frame-objects). What it returns is shaped the same way as the output of `extract_tb()`. The optional *f* and *limit* arguments carry the same meanings they have for `print_stack()`.

 traceback.print_list(*extracted_list*, *file=None*)

Render the list of tuples handed back by `extract_tb()` or `extract_stack()` as a formatted stack trace written to the supplied file. When *file* is `None`, the output lands on [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr).

 traceback.format_list(*extracted_list*)

From a list of tuples or `FrameSummary` objects such as `extract_tb()` or `extract_stack()` produce, build a list of print-ready strings. Every string in the result lines up with the entry at the matching index in the supplied list. Each string finishes with a newline; a string may also carry newlines inside it whenever the relevant item's source text line is not `None`.

 traceback.format_exception_only(*exc*, */*, [*value*, ]***, *show_group=False*)

Format only the exception portion of a traceback from an exception value like the one [`sys.last_exc`](https://docs.python.org/3.14/library/sys.html#sys.last_exc) supplies. It returns a list of strings, every one finishing with a newline. That list holds the exception's message, ordinarily a lone string; for [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) exceptions, though, it spans multiple lines that lay out (once printed) precise detail about where the syntax error happened. After the message, the list carries the exception's [`notes`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__notes__).

As of Python 3.10 an exception object may be passed as the first argument rather than supplying *value*. When *value* is present, that first argument is disregarded so older code keeps working.

If *show_group* is set to `True` and the exception happens to be a [`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup), then its nested exceptions are folded in too, descending recursively, each indented according to how deeply it is nested.

Changed in version 3.10: The *etype* parameter now goes by the name *exc* and has become positional-only.

Changed in version 3.11: Any [`notes`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__notes__) bound to the exception are now part of the returned list.

Changed in version 3.13: *show_group* parameter was added.

[Subject index](INDEX.md) · [Previous](traceback-print-or-retrieve-a-stack-traceback.md) · [Continue](traceback-format-exception-to-traceback-walk-tb.md) · [Owning module, declaration or section: traceback](traceback-print-or-retrieve-a-stack-traceback.md)
