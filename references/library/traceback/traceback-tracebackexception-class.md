# traceback: `traceback.TracebackException`

### `TracebackException` Objects

Added in version 3.5.

`TracebackException` objects are built from real exceptions in order to record the data needed for printing afterwards. They give you a lighter-weight way to keep that data around, since they avoid holding handles on [traceback](https://docs.python.org/3.14/reference/datamodel.html#traceback-objects) and [frame](https://docs.python.org/3.14/reference/datamodel.html#frame-objects) objects. On top of that, they surface more knobs for shaping the output than the module-level functions covered earlier do.

 *class *traceback.TracebackException(*exc_type*, *exc_value*, *exc_traceback*, ***, *limit=None*, *lookup_lines=True*, *capture_locals=False*, *compact=False*, *max_group_width=15*, *max_group_depth=10*)

Record an exception so it can be rendered later. The roles of *limit*, *lookup_lines* and *capture_locals* match those in the `StackSummary` class.

When *compact* is true, the class attributes retain only the data that `TracebackException`'s [`format()`](https://docs.python.org/3.14/library/functions.html#format) method actually needs. Specifically, the `__context__` field is computed solely when `__cause__` is `None` and `__suppress_context__` is false.

Keep in mind that captured locals also appear within the traceback.

*max_group_width* and *max_group_depth* govern how exception groups are formatted (see [`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup)). Depth points to how far the group is nested, while width points to how many exceptions sit in one exception group's exceptions array. Once either ceiling is passed, the formatted output is cut short.

Changed in version 3.10: Added the *compact* parameter.

Changed in version 3.11: Added the *max_group_width* and *max_group_depth* parameters.

[Subject index](INDEX.md) · [Previous](traceback-format-exception-to-traceback-walk-tb.md) · [Continue](traceback-tracebackexception-print.md) · [Owning module, declaration or section: traceback](traceback-print-or-retrieve-a-stack-traceback.md)
